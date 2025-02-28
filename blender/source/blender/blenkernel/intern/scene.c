/*
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 *
 * The Original Code is Copyright (C) 2001-2002 by NaN Holding BV.
 * All rights reserved.
 */

/** \file
 * \ingroup bke
 */

/* Allow using deprecated functionality for .blend file I/O. */
#define DNA_DEPRECATED_ALLOW

#include <stddef.h>
#include <stdio.h>
#include <string.h>

#include "MEM_guardedalloc.h"

#include "DNA_anim_types.h"
#include "DNA_collection_types.h"
#include "DNA_curveprofile_types.h"
#include "DNA_defaults.h"
#include "DNA_gpencil_types.h"
#include "DNA_linestyle_types.h"
#include "DNA_mask_types.h"
#include "DNA_material_types.h"
#include "DNA_mesh_types.h"
#include "DNA_node_types.h"
#include "DNA_object_types.h"
#include "DNA_rigidbody_types.h"
#include "DNA_scene_types.h"
#include "DNA_screen_types.h"
#include "DNA_sequence_types.h"
#include "DNA_sound_types.h"
#include "DNA_space_types.h"
#include "DNA_text_types.h"
#include "DNA_vfont_types.h"
#include "DNA_view3d_types.h"
#include "DNA_windowmanager_types.h"
#include "DNA_workspace_types.h"
#include "DNA_world_types.h"

#include "BKE_callbacks.h"
#include "BLI_blenlib.h"
#include "BLI_math.h"
#include "BLI_string.h"
#include "BLI_string_utils.h"
#include "BLI_task.h"
#include "BLI_threads.h"
#include "BLI_utildefines.h"

#include "BLT_translation.h"

#include "BKE_action.h"
#include "BKE_anim_data.h"
#include "BKE_animsys.h"
#include "BKE_armature.h"
#include "BKE_cachefile.h"
#include "BKE_collection.h"
#include "BKE_colortools.h"
#include "BKE_curveprofile.h"
#include "BKE_duplilist.h"
#include "BKE_editmesh.h"
#include "BKE_effect.h"
#include "BKE_fcurve.h"
#include "BKE_freestyle.h"
#include "BKE_gpencil.h"
#include "BKE_icons.h"
#include "BKE_idprop.h"
#include "BKE_idtype.h"
#include "BKE_image.h"
#include "BKE_layer.h"
#include "BKE_lib_id.h"
#include "BKE_lib_query.h"
#include "BKE_lib_remap.h"
#include "BKE_linestyle.h"
#include "BKE_main.h"
#include "BKE_mask.h"
#include "BKE_node.h"
#include "BKE_object.h"
#include "BKE_paint.h"
#include "BKE_pointcache.h"
#include "BKE_rigidbody.h"
#include "BKE_scene.h"
#include "BKE_screen.h"
#include "BKE_sound.h"
#include "BKE_unit.h"
#include "BKE_workspace.h"
#include "BKE_world.h"

#include "DEG_depsgraph.h"
#include "DEG_depsgraph_build.h"
#include "DEG_depsgraph_debug.h"
#include "DEG_depsgraph_query.h"

#include "RE_engine.h"

#include "SEQ_edit.h"
#include "SEQ_iterator.h"
#include "SEQ_modifier.h"
#include "SEQ_proxy.h"
#include "SEQ_relations.h"
#include "SEQ_sequencer.h"
#include "SEQ_sound.h"

#include "BLO_read_write.h"

#include "engines/eevee/eevee_lightcache.h"

#include "PIL_time.h"

#include "IMB_colormanagement.h"
#include "IMB_imbuf.h"

#include "bmesh.h"

static void scene_init_data(ID *id)
{
  Scene *scene = (Scene *)id;
  const char *colorspace_name;
  SceneRenderView *srv;
  CurveMapping *mblur_shutter_curve;

  BLI_assert(MEMCMP_STRUCT_AFTER_IS_ZERO(scene, id));

  MEMCPY_STRUCT_AFTER(scene, DNA_struct_default_get(Scene), id);

  BLI_strncpy(scene->r.bake.filepath, U.renderdir, sizeof(scene->r.bake.filepath));

  mblur_shutter_curve = &scene->r.mblur_shutter_curve;
  BKE_curvemapping_set_defaults(mblur_shutter_curve, 1, 0.0f, 0.0f, 1.0f, 1.0f);
  BKE_curvemapping_init(mblur_shutter_curve);
  BKE_curvemap_reset(mblur_shutter_curve->cm,
                     &mblur_shutter_curve->clipr,
                     CURVE_PRESET_MAX,
                     CURVEMAP_SLOPE_POS_NEG);

  scene->toolsettings = DNA_struct_default_alloc(ToolSettings);

  scene->toolsettings->autokey_mode = (uchar)U.autokey_mode;

  /* grease pencil multiframe falloff curve */
  scene->toolsettings->gp_sculpt.cur_falloff = BKE_curvemapping_add(1, 0.0f, 0.0f, 1.0f, 1.0f);
  CurveMapping *gp_falloff_curve = scene->toolsettings->gp_sculpt.cur_falloff;
  BKE_curvemapping_init(gp_falloff_curve);
  BKE_curvemap_reset(
      gp_falloff_curve->cm, &gp_falloff_curve->clipr, CURVE_PRESET_GAUSS, CURVEMAP_SLOPE_POSITIVE);

  scene->toolsettings->gp_sculpt.cur_primitive = BKE_curvemapping_add(1, 0.0f, 0.0f, 1.0f, 1.0f);
  CurveMapping *gp_primitive_curve = scene->toolsettings->gp_sculpt.cur_primitive;
  BKE_curvemapping_init(gp_primitive_curve);
  BKE_curvemap_reset(gp_primitive_curve->cm,
                     &gp_primitive_curve->clipr,
                     CURVE_PRESET_BELL,
                     CURVEMAP_SLOPE_POSITIVE);

  scene->unit.system = USER_UNIT_METRIC;
  scene->unit.scale_length = 1.0f;
  scene->unit.length_unit = (uchar)BKE_unit_base_of_type_get(USER_UNIT_METRIC, B_UNIT_LENGTH);
  scene->unit.mass_unit = (uchar)BKE_unit_base_of_type_get(USER_UNIT_METRIC, B_UNIT_MASS);
  scene->unit.time_unit = (uchar)BKE_unit_base_of_type_get(USER_UNIT_METRIC, B_UNIT_TIME);
  scene->unit.temperature_unit = (uchar)BKE_unit_base_of_type_get(USER_UNIT_METRIC,
                                                                  B_UNIT_TEMPERATURE);

  /* Anti-Aliasing threshold. */
  scene->grease_pencil_settings.smaa_threshold = 1.0f;

  {
    ParticleEditSettings *pset;
    pset = &scene->toolsettings->particle;
    for (size_t i = 1; i < ARRAY_SIZE(pset->brush); i++) {
      pset->brush[i] = pset->brush[0];
    }
    pset->brush[PE_BRUSH_CUT].strength = 1.0f;
  }

  BLI_strncpy(scene->r.engine, RE_engine_id_BLENDER_EEVEE, sizeof(scene->r.engine));

  BLI_strncpy(scene->r.pic, U.renderdir, sizeof(scene->r.pic));

  /* Note; in header_info.c the scene copy happens...,
   * if you add more to renderdata it has to be checked there. */

  /* multiview - stereo */
  BKE_scene_add_render_view(scene, STEREO_LEFT_NAME);
  srv = scene->r.views.first;
  BLI_strncpy(srv->suffix, STEREO_LEFT_SUFFIX, sizeof(srv->suffix));

  BKE_scene_add_render_view(scene, STEREO_RIGHT_NAME);
  srv = scene->r.views.last;
  BLI_strncpy(srv->suffix, STEREO_RIGHT_SUFFIX, sizeof(srv->suffix));

  BKE_sound_reset_scene_runtime(scene);

  /* color management */
  colorspace_name = IMB_colormanagement_role_colorspace_name_get(COLOR_ROLE_DEFAULT_SEQUENCER);

  BKE_color_managed_display_settings_init(&scene->display_settings);
  BKE_color_managed_view_settings_init_render(
      &scene->view_settings, &scene->display_settings, "Filmic");
  BLI_strncpy(scene->sequencer_colorspace_settings.name,
              colorspace_name,
              sizeof(scene->sequencer_colorspace_settings.name));

  /* Those next two sets (render and baking settings) are not currently in use,
   * but are exposed to RNA API and hence must have valid data. */
  BKE_color_managed_display_settings_init(&scene->r.im_format.display_settings);
  BKE_color_managed_view_settings_init_render(
      &scene->r.im_format.view_settings, &scene->r.im_format.display_settings, "Filmic");

  BKE_color_managed_display_settings_init(&scene->r.bake.im_format.display_settings);
  BKE_color_managed_view_settings_init_render(
      &scene->r.bake.im_format.view_settings, &scene->r.bake.im_format.display_settings, "Filmic");

  /* Curve Profile */
  scene->toolsettings->custom_bevel_profile_preset = BKE_curveprofile_add(PROF_PRESET_LINE);
  scene->toolsettings->sequencer_tool_settings = SEQ_tool_settings_init();

  for (size_t i = 0; i < ARRAY_SIZE(scene->orientation_slots); i++) {
    scene->orientation_slots[i].index_custom = -1;
  }

  /* Master Collection */
  scene->master_collection = BKE_collection_master_add();

  BKE_view_layer_add(scene, "View Layer", NULL, VIEWLAYER_ADD_NEW);
}

static void scene_copy_markers(Scene *scene_dst, const Scene *scene_src, const int flag)
{
  BLI_duplicatelist(&scene_dst->markers, &scene_src->markers);
  LISTBASE_FOREACH (TimeMarker *, marker, &scene_dst->markers) {
    if (marker->prop != NULL) {
      marker->prop = IDP_CopyProperty_ex(marker->prop, flag);
    }
  }
}

static void scene_copy_data(Main *bmain, ID *id_dst, const ID *id_src, const int flag)
{
  Scene *scene_dst = (Scene *)id_dst;
  const Scene *scene_src = (const Scene *)id_src;
  /* We never handle usercount here for own data. */
  const int flag_subdata = flag | LIB_ID_CREATE_NO_USER_REFCOUNT;
  /* We always need allocation of our private ID data. */
  const int flag_private_id_data = flag & ~LIB_ID_CREATE_NO_ALLOCATE;

  scene_dst->ed = NULL;
  scene_dst->depsgraph_hash = NULL;
  scene_dst->fps_info = NULL;

  /* Master Collection */
  if (scene_src->master_collection) {
    BKE_id_copy_ex(bmain,
                   (ID *)scene_src->master_collection,
                   (ID **)&scene_dst->master_collection,
                   flag_private_id_data);
  }

  /* View Layers */
  BLI_duplicatelist(&scene_dst->view_layers, &scene_src->view_layers);
  for (ViewLayer *view_layer_src = scene_src->view_layers.first,
                 *view_layer_dst = scene_dst->view_layers.first;
       view_layer_src;
       view_layer_src = view_layer_src->next, view_layer_dst = view_layer_dst->next) {
    BKE_view_layer_copy_data(scene_dst, scene_src, view_layer_dst, view_layer_src, flag_subdata);
  }

  scene_copy_markers(scene_dst, scene_src, flag);

  BLI_duplicatelist(&(scene_dst->transform_spaces), &(scene_src->transform_spaces));
  BLI_duplicatelist(&(scene_dst->r.views), &(scene_src->r.views));
  BKE_keyingsets_copy(&(scene_dst->keyingsets), &(scene_src->keyingsets));

  if (scene_src->nodetree) {
    BKE_id_copy_ex(
        bmain, (ID *)scene_src->nodetree, (ID **)&scene_dst->nodetree, flag_private_id_data);
    BKE_libblock_relink_ex(bmain,
                           scene_dst->nodetree,
                           (void *)(&scene_src->id),
                           &scene_dst->id,
                           ID_REMAP_SKIP_NEVER_NULL_USAGE);
  }

  if (scene_src->rigidbody_world) {
    scene_dst->rigidbody_world = BKE_rigidbody_world_copy(scene_src->rigidbody_world,
                                                          flag_subdata);
  }

  /* copy color management settings */
  BKE_color_managed_display_settings_copy(&scene_dst->display_settings,
                                          &scene_src->display_settings);
  BKE_color_managed_view_settings_copy(&scene_dst->view_settings, &scene_src->view_settings);
  BKE_color_managed_colorspace_settings_copy(&scene_dst->sequencer_colorspace_settings,
                                             &scene_src->sequencer_colorspace_settings);

  BKE_color_managed_display_settings_copy(&scene_dst->r.im_format.display_settings,
                                          &scene_src->r.im_format.display_settings);
  BKE_color_managed_view_settings_copy(&scene_dst->r.im_format.view_settings,
                                       &scene_src->r.im_format.view_settings);

  BKE_color_managed_display_settings_copy(&scene_dst->r.bake.im_format.display_settings,
                                          &scene_src->r.bake.im_format.display_settings);
  BKE_color_managed_view_settings_copy(&scene_dst->r.bake.im_format.view_settings,
                                       &scene_src->r.bake.im_format.view_settings);

  BKE_curvemapping_copy_data(&scene_dst->r.mblur_shutter_curve, &scene_src->r.mblur_shutter_curve);

  /* tool settings */
  scene_dst->toolsettings = BKE_toolsettings_copy(scene_dst->toolsettings, flag_subdata);

  /* make a private copy of the avicodecdata */
  if (scene_src->r.avicodecdata) {
    scene_dst->r.avicodecdata = MEM_dupallocN(scene_src->r.avicodecdata);
    scene_dst->r.avicodecdata->lpFormat = MEM_dupallocN(scene_dst->r.avicodecdata->lpFormat);
    scene_dst->r.avicodecdata->lpParms = MEM_dupallocN(scene_dst->r.avicodecdata->lpParms);
  }

  if (scene_src->r.ffcodecdata.properties) {
    /* intentionally check sce_dst not sce_src. */ /* XXX ??? comment outdated... */
    scene_dst->r.ffcodecdata.properties = IDP_CopyProperty_ex(scene_src->r.ffcodecdata.properties,
                                                              flag_subdata);
  }

  if (scene_src->display.shading.prop) {
    scene_dst->display.shading.prop = IDP_CopyProperty(scene_src->display.shading.prop);
  }

  BKE_sound_reset_scene_runtime(scene_dst);

  /* Copy sequencer, this is local data! */
  if (scene_src->ed) {
    scene_dst->ed = MEM_callocN(sizeof(*scene_dst->ed), __func__);
    scene_dst->ed->seqbasep = &scene_dst->ed->seqbase;
    SEQ_sequence_base_dupli_recursive(scene_src,
                                      scene_dst,
                                      &scene_dst->ed->seqbase,
                                      &scene_src->ed->seqbase,
                                      SEQ_DUPE_ALL,
                                      flag_subdata);
  }

  if ((flag & LIB_ID_COPY_NO_PREVIEW) == 0) {
    BKE_previewimg_id_copy(&scene_dst->id, &scene_src->id);
  }
  else {
    scene_dst->preview = NULL;
  }

  BKE_scene_copy_data_eevee(scene_dst, scene_src);
}

static void scene_free_markers(Scene *scene, bool do_id_user)
{
  LISTBASE_FOREACH_MUTABLE (TimeMarker *, marker, &scene->markers) {
    if (marker->prop != NULL) {
      IDP_FreePropertyContent_ex(marker->prop, do_id_user);
      MEM_freeN(marker->prop);
    }
    MEM_freeN(marker);
  }
}

static void scene_free_data(ID *id)
{

  Scene *scene = (Scene *)id;
  const bool do_id_user = false;

  SEQ_editing_free(scene, do_id_user);

  BKE_keyingsets_free(&scene->keyingsets);

  /* is no lib link block, but scene extension */
  if (scene->nodetree) {
    ntreeFreeEmbeddedTree(scene->nodetree);
    MEM_freeN(scene->nodetree);
    scene->nodetree = NULL;
  }

  if (scene->rigidbody_world) {
    /* Prevent rigidbody freeing code to follow other IDs pointers, this should never be allowed
     * nor necessary from here, and with new undo code, those pointers may be fully invalid or
     * worse, pointing to data actually belonging to new BMain! */
    scene->rigidbody_world->constraints = NULL;
    scene->rigidbody_world->group = NULL;
    BKE_rigidbody_free_world(scene);
  }

  if (scene->r.avicodecdata) {
    free_avicodecdata(scene->r.avicodecdata);
    MEM_freeN(scene->r.avicodecdata);
    scene->r.avicodecdata = NULL;
  }
  if (scene->r.ffcodecdata.properties) {
    IDP_FreeProperty(scene->r.ffcodecdata.properties);
    scene->r.ffcodecdata.properties = NULL;
  }

  scene_free_markers(scene, do_id_user);
  BLI_freelistN(&scene->transform_spaces);
  BLI_freelistN(&scene->r.views);

  BKE_toolsettings_free(scene->toolsettings);
  scene->toolsettings = NULL;

  BKE_scene_free_depsgraph_hash(scene);

  MEM_SAFE_FREE(scene->fps_info);

  BKE_sound_destroy_scene(scene);

  BKE_color_managed_view_settings_free(&scene->view_settings);

  BKE_previewimg_free(&scene->preview);
  BKE_curvemapping_free_data(&scene->r.mblur_shutter_curve);

  for (ViewLayer *view_layer = scene->view_layers.first, *view_layer_next; view_layer;
       view_layer = view_layer_next) {
    view_layer_next = view_layer->next;

    BLI_remlink(&scene->view_layers, view_layer);
    BKE_view_layer_free_ex(view_layer, do_id_user);
  }

  /* Master Collection */
  /* TODO: what to do with do_id_user? it's also true when just
   * closing the file which seems wrong? should decrement users
   * for objects directly in the master collection? then other
   * collections in the scene need to do it too? */
  if (scene->master_collection) {
    BKE_collection_free(scene->master_collection);
    MEM_freeN(scene->master_collection);
    scene->master_collection = NULL;
  }

  if (scene->eevee.light_cache_data) {
    EEVEE_lightcache_free(scene->eevee.light_cache_data);
    scene->eevee.light_cache_data = NULL;
  }

  if (scene->display.shading.prop) {
    IDP_FreeProperty(scene->display.shading.prop);
    scene->display.shading.prop = NULL;
  }

  /* These are freed on doversion. */
  BLI_assert(scene->layer_properties == NULL);
}

static void scene_foreach_rigidbodyworldSceneLooper(struct RigidBodyWorld *UNUSED(rbw),
                                                    ID **id_pointer,
                                                    void *user_data,
                                                    int cb_flag)
{
  LibraryForeachIDData *data = (LibraryForeachIDData *)user_data;
  BKE_lib_query_foreachid_process(data, id_pointer, cb_flag);
}

/**
 * This code is shared by both the regular `foreach_id` looper, and the code trying to restore or
 * preserve ID pointers like brushes across undo-steps.
 */
typedef enum eSceneForeachUndoPreserveProcess {
  /* Undo when preserving tool-settings from old scene, we also want to try to preserve that ID
   * pointer from its old scene's value. */
  SCENE_FOREACH_UNDO_RESTORE,
  /* Undo when preserving tool-settings from old scene, we want to keep the new value of that ID
   * pointer. */
  SCENE_FOREACH_UNDO_NO_RESTORE,
} eSceneForeachUndoPreserveProcess;

static void scene_foreach_toolsettings_id_pointer_process(
    ID **id_p,
    const eSceneForeachUndoPreserveProcess action,
    BlendLibReader *reader,
    ID **id_old_p,
    const uint cb_flag)
{
  switch (action) {
    case SCENE_FOREACH_UNDO_RESTORE: {
      ID *id_old = *id_old_p;
      /* Old data has not been remapped to new values of the pointers, if we want to keep the old
       * pointer here we need its new address. */
      ID *id_old_new = id_old != NULL ? BLO_read_get_new_id_address(reader, id_old->lib, id_old) :
                                        NULL;
      if (id_old_new != NULL) {
        BLI_assert(ELEM(id_old, id_old_new, id_old_new->orig_id));
        *id_old_p = id_old_new;
        if (cb_flag & IDWALK_CB_USER) {
          id_us_plus_no_lib(id_old_new);
          id_us_min(id_old);
        }
        break;
      }
      /* We failed to find a new valid pointer for the previous ID, just keep the current one as
       * if we had been under SCENE_FOREACH_UNDO_NO_RESTORE case. */
      SWAP(ID *, *id_p, *id_old_p);
      break;
    }
    case SCENE_FOREACH_UNDO_NO_RESTORE:
      /* Counteract the swap of the whole ToolSettings container struct. */
      SWAP(ID *, *id_p, *id_old_p);
      break;
  }
}

#define BKE_LIB_FOREACHID_UNDO_PRESERVE_PROCESS( \
    __data, __id, __do_undo_restore, __action, __reader, __id_old, __cb_flag) \
  { \
    if (__do_undo_restore) { \
      scene_foreach_toolsettings_id_pointer_process( \
          (ID **)&(__id), __action, __reader, (ID **)&(__id_old), __cb_flag); \
    } \
    else { \
      BKE_LIB_FOREACHID_PROCESS(__data, __id, __cb_flag); \
    } \
  } \
  (void)0

static void scene_foreach_paint(LibraryForeachIDData *data,
                                Paint *paint,
                                const bool do_undo_restore,
                                BlendLibReader *reader,
                                Paint *paint_old)
{
  BKE_LIB_FOREACHID_UNDO_PRESERVE_PROCESS(data,
                                          paint->brush,
                                          do_undo_restore,
                                          SCENE_FOREACH_UNDO_RESTORE,
                                          reader,
                                          paint_old->brush,
                                          IDWALK_CB_USER);
  for (int i = 0; i < paint_old->tool_slots_len; i++) {
    /* This is a bit tricky.
     *  - In case we do not do `undo_restore`, `paint` and `paint_old` pointers are the same, so
     *    this is equivalent to simply looping over slots from `paint`.
     *  - In case we do `undo_restore`, we only want to consider the slots from the old one, since
     *    those are the one we keep in the end.
     *    + In case the new data has less valid slots, we feed in a dummy NULL pointer.
     *    + In case the new data has more valid slots, the extra ones are ignored.
     */
    Brush *brush_tmp = NULL;
    Brush **brush_p = i < paint->tool_slots_len ? &paint->tool_slots[i].brush : &brush_tmp;
    BKE_LIB_FOREACHID_UNDO_PRESERVE_PROCESS(data,
                                            *brush_p,
                                            do_undo_restore,
                                            SCENE_FOREACH_UNDO_RESTORE,
                                            reader,
                                            paint_old->brush,
                                            IDWALK_CB_USER);
  }
  BKE_LIB_FOREACHID_UNDO_PRESERVE_PROCESS(data,
                                          paint->palette,
                                          do_undo_restore,
                                          SCENE_FOREACH_UNDO_RESTORE,
                                          reader,
                                          paint_old->palette,
                                          IDWALK_CB_USER);
}

static void scene_foreach_toolsettings(LibraryForeachIDData *data,
                                       ToolSettings *toolsett,
                                       const bool do_undo_restore,
                                       BlendLibReader *reader,
                                       ToolSettings *toolsett_old)
{
  BKE_LIB_FOREACHID_UNDO_PRESERVE_PROCESS(data,
                                          toolsett->particle.scene,
                                          do_undo_restore,
                                          SCENE_FOREACH_UNDO_NO_RESTORE,
                                          reader,
                                          toolsett_old->particle.scene,
                                          IDWALK_CB_NOP);
  BKE_LIB_FOREACHID_UNDO_PRESERVE_PROCESS(data,
                                          toolsett->particle.object,
                                          do_undo_restore,
                                          SCENE_FOREACH_UNDO_NO_RESTORE,
                                          reader,
                                          toolsett_old->particle.object,
                                          IDWALK_CB_NOP);
  BKE_LIB_FOREACHID_UNDO_PRESERVE_PROCESS(data,
                                          toolsett->particle.shape_object,
                                          do_undo_restore,
                                          SCENE_FOREACH_UNDO_NO_RESTORE,
                                          reader,
                                          toolsett_old->particle.shape_object,
                                          IDWALK_CB_NOP);

  scene_foreach_paint(
      data, &toolsett->imapaint.paint, do_undo_restore, reader, &toolsett_old->imapaint.paint);
  BKE_LIB_FOREACHID_UNDO_PRESERVE_PROCESS(data,
                                          toolsett->imapaint.stencil,
                                          do_undo_restore,
                                          SCENE_FOREACH_UNDO_RESTORE,
                                          reader,
                                          toolsett_old->imapaint.stencil,
                                          IDWALK_CB_USER);
  BKE_LIB_FOREACHID_UNDO_PRESERVE_PROCESS(data,
                                          toolsett->imapaint.clone,
                                          do_undo_restore,
                                          SCENE_FOREACH_UNDO_RESTORE,
                                          reader,
                                          toolsett_old->imapaint.clone,
                                          IDWALK_CB_USER);
  BKE_LIB_FOREACHID_UNDO_PRESERVE_PROCESS(data,
                                          toolsett->imapaint.canvas,
                                          do_undo_restore,
                                          SCENE_FOREACH_UNDO_RESTORE,
                                          reader,
                                          toolsett_old->imapaint.canvas,
                                          IDWALK_CB_USER);

  if (toolsett->vpaint) {
    scene_foreach_paint(
        data, &toolsett->vpaint->paint, do_undo_restore, reader, &toolsett_old->vpaint->paint);
  }
  if (toolsett->wpaint) {
    scene_foreach_paint(
        data, &toolsett->wpaint->paint, do_undo_restore, reader, &toolsett_old->wpaint->paint);
  }
  if (toolsett->sculpt) {
    scene_foreach_paint(
        data, &toolsett->sculpt->paint, do_undo_restore, reader, &toolsett_old->sculpt->paint);
    BKE_LIB_FOREACHID_UNDO_PRESERVE_PROCESS(data,
                                            toolsett->sculpt->gravity_object,
                                            do_undo_restore,
                                            SCENE_FOREACH_UNDO_NO_RESTORE,
                                            reader,
                                            toolsett_old->sculpt->gravity_object,
                                            IDWALK_CB_NOP);
  }
  if (toolsett->uvsculpt) {
    scene_foreach_paint(
        data, &toolsett->uvsculpt->paint, do_undo_restore, reader, &toolsett_old->uvsculpt->paint);
  }
  if (toolsett->gp_paint) {
    scene_foreach_paint(
        data, &toolsett->gp_paint->paint, do_undo_restore, reader, &toolsett_old->gp_paint->paint);
  }
  if (toolsett->gp_vertexpaint) {
    scene_foreach_paint(data,
                        &toolsett->gp_vertexpaint->paint,
                        do_undo_restore,
                        reader,
                        &toolsett_old->gp_vertexpaint->paint);
  }
  if (toolsett->gp_sculptpaint) {
    scene_foreach_paint(data,
                        &toolsett->gp_sculptpaint->paint,
                        do_undo_restore,
                        reader,
                        &toolsett_old->gp_sculptpaint->paint);
  }
  if (toolsett->gp_weightpaint) {
    scene_foreach_paint(data,
                        &toolsett->gp_weightpaint->paint,
                        do_undo_restore,
                        reader,
                        &toolsett_old->gp_weightpaint->paint);
  }

  BKE_LIB_FOREACHID_UNDO_PRESERVE_PROCESS(data,
                                          toolsett->gp_sculpt.guide.reference_object,
                                          do_undo_restore,
                                          SCENE_FOREACH_UNDO_NO_RESTORE,
                                          reader,
                                          toolsett_old->gp_sculpt.guide.reference_object,
                                          IDWALK_CB_NOP);
}

static void scene_foreach_layer_collection(LibraryForeachIDData *data, ListBase *lb)
{
  LISTBASE_FOREACH (LayerCollection *, lc, lb) {
    /* XXX This is very weak. The whole idea of keeping pointers to private IDs is very bad
     * anyway... */
    const int cb_flag = (lc->collection != NULL &&
                         (lc->collection->id.flag & LIB_EMBEDDED_DATA) != 0) ?
                            IDWALK_CB_EMBEDDED :
                            IDWALK_CB_NOP;
    BKE_LIB_FOREACHID_PROCESS(data, lc->collection, cb_flag);
    scene_foreach_layer_collection(data, &lc->layer_collections);
  }
}

static void scene_foreach_id(ID *id, LibraryForeachIDData *data)
{
  Scene *scene = (Scene *)id;

  BKE_LIB_FOREACHID_PROCESS(data, scene->camera, IDWALK_CB_NOP);
  BKE_LIB_FOREACHID_PROCESS(data, scene->world, IDWALK_CB_USER);
  BKE_LIB_FOREACHID_PROCESS(data, scene->set, IDWALK_CB_NEVER_SELF);
  BKE_LIB_FOREACHID_PROCESS(data, scene->clip, IDWALK_CB_USER);
  BKE_LIB_FOREACHID_PROCESS(data, scene->gpd, IDWALK_CB_USER);
  BKE_LIB_FOREACHID_PROCESS(data, scene->r.bake.cage_object, IDWALK_CB_NOP);
  if (scene->nodetree) {
    /* nodetree **are owned by IDs**, treat them as mere sub-data and not real ID! */
    BKE_library_foreach_ID_embedded(data, (ID **)&scene->nodetree);
  }
  if (scene->ed) {
    Sequence *seq;
    SEQ_ALL_BEGIN (scene->ed, seq) {
      BKE_LIB_FOREACHID_PROCESS(data, seq->scene, IDWALK_CB_NEVER_SELF);
      BKE_LIB_FOREACHID_PROCESS(data, seq->scene_camera, IDWALK_CB_NOP);
      BKE_LIB_FOREACHID_PROCESS(data, seq->clip, IDWALK_CB_USER);
      BKE_LIB_FOREACHID_PROCESS(data, seq->mask, IDWALK_CB_USER);
      BKE_LIB_FOREACHID_PROCESS(data, seq->sound, IDWALK_CB_USER);
      IDP_foreach_property(
          seq->prop, IDP_TYPE_FILTER_ID, BKE_lib_query_idpropertiesForeachIDLink_callback, data);
      LISTBASE_FOREACH (SequenceModifierData *, smd, &seq->modifiers) {
        BKE_LIB_FOREACHID_PROCESS(data, smd->mask_id, IDWALK_CB_USER);
      }

      if (seq->type == SEQ_TYPE_TEXT && seq->effectdata) {
        TextVars *text_data = seq->effectdata;
        BKE_LIB_FOREACHID_PROCESS(data, text_data->text_font, IDWALK_CB_USER);
      }
    }
    SEQ_ALL_END;
  }

  /* This pointer can be NULL during old files reading, better be safe than sorry. */
  if (scene->master_collection != NULL) {
    BKE_library_foreach_ID_embedded(data, (ID **)&scene->master_collection);
  }

  LISTBASE_FOREACH (ViewLayer *, view_layer, &scene->view_layers) {
    BKE_LIB_FOREACHID_PROCESS(data, view_layer->mat_override, IDWALK_CB_USER);

    LISTBASE_FOREACH (Base *, base, &view_layer->object_bases) {
      BKE_LIB_FOREACHID_PROCESS(
          data, base->object, IDWALK_CB_NOP | IDWALK_CB_OVERRIDE_LIBRARY_NOT_OVERRIDABLE);
    }

    scene_foreach_layer_collection(data, &view_layer->layer_collections);

    LISTBASE_FOREACH (FreestyleModuleConfig *, fmc, &view_layer->freestyle_config.modules) {
      if (fmc->script) {
        BKE_LIB_FOREACHID_PROCESS(data, fmc->script, IDWALK_CB_NOP);
      }
    }

    LISTBASE_FOREACH (FreestyleLineSet *, fls, &view_layer->freestyle_config.linesets) {
      if (fls->group) {
        BKE_LIB_FOREACHID_PROCESS(data, fls->group, IDWALK_CB_USER);
      }

      if (fls->linestyle) {
        BKE_LIB_FOREACHID_PROCESS(data, fls->linestyle, IDWALK_CB_USER);
      }
    }
  }

  LISTBASE_FOREACH (TimeMarker *, marker, &scene->markers) {
    BKE_LIB_FOREACHID_PROCESS(data, marker->camera, IDWALK_CB_NOP);
    IDP_foreach_property(
        marker->prop, IDP_TYPE_FILTER_ID, BKE_lib_query_idpropertiesForeachIDLink_callback, data);
  }

  ToolSettings *toolsett = scene->toolsettings;
  if (toolsett) {
    scene_foreach_toolsettings(data, toolsett, false, NULL, toolsett);
  }

  if (scene->rigidbody_world) {
    BKE_rigidbody_world_id_loop(
        scene->rigidbody_world, scene_foreach_rigidbodyworldSceneLooper, data);
  }
}

static void scene_foreach_cache(ID *id,
                                IDTypeForeachCacheFunctionCallback function_callback,
                                void *user_data)
{
  Scene *scene = (Scene *)id;
  IDCacheKey key = {
      .id_session_uuid = id->session_uuid,
      .offset_in_ID = offsetof(Scene, eevee.light_cache_data),
      .cache_v = scene->eevee.light_cache_data,
  };

  function_callback(id,
                    &key,
                    (void **)&scene->eevee.light_cache_data,
                    IDTYPE_CACHE_CB_FLAGS_PERSISTENT,
                    user_data);
}

static void scene_blend_write(BlendWriter *writer, ID *id, const void *id_address)
{
  Scene *sce = (Scene *)id;

  if (BLO_write_is_undo(writer)) {
    /* Clean up, important in undo case to reduce false detection of changed data-blocks. */
    /* XXX This UI data should not be stored in Scene at all... */
    memset(&sce->cursor, 0, sizeof(sce->cursor));
  }

  /* write LibData */
  BLO_write_id_struct(writer, Scene, id_address, &sce->id);
  BKE_id_blend_write(writer, &sce->id);

  if (sce->adt) {
    BKE_animdata_blend_write(writer, sce->adt);
  }
  BKE_keyingsets_blend_write(writer, &sce->keyingsets);

  /* direct data */
  ToolSettings *tos = sce->toolsettings;
  BLO_write_struct(writer, ToolSettings, tos);
  if (tos->vpaint) {
    BLO_write_struct(writer, VPaint, tos->vpaint);
    BKE_paint_blend_write(writer, &tos->vpaint->paint);
  }
  if (tos->wpaint) {
    BLO_write_struct(writer, VPaint, tos->wpaint);
    BKE_paint_blend_write(writer, &tos->wpaint->paint);
  }
  if (tos->sculpt) {
    BLO_write_struct(writer, Sculpt, tos->sculpt);
    BKE_paint_blend_write(writer, &tos->sculpt->paint);
  }
  if (tos->uvsculpt) {
    BLO_write_struct(writer, UvSculpt, tos->uvsculpt);
    BKE_paint_blend_write(writer, &tos->uvsculpt->paint);
  }
  if (tos->gp_paint) {
    BLO_write_struct(writer, GpPaint, tos->gp_paint);
    BKE_paint_blend_write(writer, &tos->gp_paint->paint);
  }
  if (tos->gp_vertexpaint) {
    BLO_write_struct(writer, GpVertexPaint, tos->gp_vertexpaint);
    BKE_paint_blend_write(writer, &tos->gp_vertexpaint->paint);
  }
  if (tos->gp_sculptpaint) {
    BLO_write_struct(writer, GpSculptPaint, tos->gp_sculptpaint);
    BKE_paint_blend_write(writer, &tos->gp_sculptpaint->paint);
  }
  if (tos->gp_weightpaint) {
    BLO_write_struct(writer, GpWeightPaint, tos->gp_weightpaint);
    BKE_paint_blend_write(writer, &tos->gp_weightpaint->paint);
  }
  /* write grease-pencil custom ipo curve to file */
  if (tos->gp_interpolate.custom_ipo) {
    BKE_curvemapping_blend_write(writer, tos->gp_interpolate.custom_ipo);
  }
  /* write grease-pencil multiframe falloff curve to file */
  if (tos->gp_sculpt.cur_falloff) {
    BKE_curvemapping_blend_write(writer, tos->gp_sculpt.cur_falloff);
  }
  /* write grease-pencil primitive curve to file */
  if (tos->gp_sculpt.cur_primitive) {
    BKE_curvemapping_blend_write(writer, tos->gp_sculpt.cur_primitive);
  }
  /* Write the curve profile to the file. */
  if (tos->custom_bevel_profile_preset) {
    BKE_curveprofile_blend_write(writer, tos->custom_bevel_profile_preset);
  }
  if (tos->sequencer_tool_settings) {
    BLO_write_struct(writer, SequencerToolSettings, tos->sequencer_tool_settings);
  }

  BKE_paint_blend_write(writer, &tos->imapaint.paint);

  Editing *ed = sce->ed;
  if (ed) {
    Sequence *seq;

    BLO_write_struct(writer, Editing, ed);

    /* reset write flags too */

    SEQ_ALL_BEGIN (ed, seq) {
      if (seq->strip) {
        seq->strip->done = false;
      }
      BLO_write_struct(writer, Sequence, seq);
    }
    SEQ_ALL_END;

    SEQ_ALL_BEGIN (ed, seq) {
      if (seq->strip && seq->strip->done == 0) {
        /* write strip with 'done' at 0 because readfile */

        if (seq->effectdata) {
          switch (seq->type) {
            case SEQ_TYPE_COLOR:
              BLO_write_struct(writer, SolidColorVars, seq->effectdata);
              break;
            case SEQ_TYPE_SPEED:
              BLO_write_struct(writer, SpeedControlVars, seq->effectdata);
              break;
            case SEQ_TYPE_WIPE:
              BLO_write_struct(writer, WipeVars, seq->effectdata);
              break;
            case SEQ_TYPE_GLOW:
              BLO_write_struct(writer, GlowVars, seq->effectdata);
              break;
            case SEQ_TYPE_TRANSFORM:
              BLO_write_struct(writer, TransformVars, seq->effectdata);
              break;
            case SEQ_TYPE_GAUSSIAN_BLUR:
              BLO_write_struct(writer, GaussianBlurVars, seq->effectdata);
              break;
            case SEQ_TYPE_TEXT:
              BLO_write_struct(writer, TextVars, seq->effectdata);
              break;
            case SEQ_TYPE_COLORMIX:
              BLO_write_struct(writer, ColorMixVars, seq->effectdata);
              break;
          }
        }

        BLO_write_struct(writer, Stereo3dFormat, seq->stereo3d_format);

        Strip *strip = seq->strip;
        BLO_write_struct(writer, Strip, strip);
        if (strip->crop) {
          BLO_write_struct(writer, StripCrop, strip->crop);
        }
        if (strip->transform) {
          BLO_write_struct(writer, StripTransform, strip->transform);
        }
        if (strip->proxy) {
          BLO_write_struct(writer, StripProxy, strip->proxy);
        }
        if (seq->type == SEQ_TYPE_IMAGE) {
          BLO_write_struct_array(writer,
                                 StripElem,
                                 MEM_allocN_len(strip->stripdata) / sizeof(struct StripElem),
                                 strip->stripdata);
        }
        else if (ELEM(seq->type, SEQ_TYPE_MOVIE, SEQ_TYPE_SOUND_RAM, SEQ_TYPE_SOUND_HD)) {
          BLO_write_struct(writer, StripElem, strip->stripdata);
        }

        strip->done = true;
      }

      if (seq->prop) {
        IDP_BlendWrite(writer, seq->prop);
      }

      SEQ_modifier_blend_write(writer, &seq->modifiers);
    }
    SEQ_ALL_END;

    /* new; meta stack too, even when its nasty restore code */
    LISTBASE_FOREACH (MetaStack *, ms, &ed->metastack) {
      BLO_write_struct(writer, MetaStack, ms);
    }
  }

  if (sce->r.avicodecdata) {
    BLO_write_struct(writer, AviCodecData, sce->r.avicodecdata);
    if (sce->r.avicodecdata->lpFormat) {
      BLO_write_raw(writer, (size_t)sce->r.avicodecdata->cbFormat, sce->r.avicodecdata->lpFormat);
    }
    if (sce->r.avicodecdata->lpParms) {
      BLO_write_raw(writer, (size_t)sce->r.avicodecdata->cbParms, sce->r.avicodecdata->lpParms);
    }
  }
  if (sce->r.ffcodecdata.properties) {
    IDP_BlendWrite(writer, sce->r.ffcodecdata.properties);
  }

  /* writing dynamic list of TimeMarkers to the blend file */
  LISTBASE_FOREACH (TimeMarker *, marker, &sce->markers) {
    BLO_write_struct(writer, TimeMarker, marker);

    if (marker->prop != NULL) {
      IDP_BlendWrite(writer, marker->prop);
    }
  }

  /* writing dynamic list of TransformOrientations to the blend file */
  LISTBASE_FOREACH (TransformOrientation *, ts, &sce->transform_spaces) {
    BLO_write_struct(writer, TransformOrientation, ts);
  }

  /* writing MultiView to the blend file */
  LISTBASE_FOREACH (SceneRenderView *, srv, &sce->r.views) {
    BLO_write_struct(writer, SceneRenderView, srv);
  }

  if (sce->nodetree) {
    BLO_write_struct(writer, bNodeTree, sce->nodetree);
    ntreeBlendWrite(writer, sce->nodetree);
  }

  BKE_color_managed_view_settings_blend_write(writer, &sce->view_settings);

  /* writing RigidBodyWorld data to the blend file */
  if (sce->rigidbody_world) {
    /* Set deprecated pointers to prevent crashes of older Blenders */
    sce->rigidbody_world->pointcache = sce->rigidbody_world->shared->pointcache;
    sce->rigidbody_world->ptcaches = sce->rigidbody_world->shared->ptcaches;
    BLO_write_struct(writer, RigidBodyWorld, sce->rigidbody_world);

    BLO_write_struct(writer, RigidBodyWorld_Shared, sce->rigidbody_world->shared);
    BLO_write_struct(writer, EffectorWeights, sce->rigidbody_world->effector_weights);
    BKE_ptcache_blend_write(writer, &(sce->rigidbody_world->shared->ptcaches));
  }

  BKE_previewimg_blend_write(writer, sce->preview);
  BKE_curvemapping_curves_blend_write(writer, &sce->r.mblur_shutter_curve);

  LISTBASE_FOREACH (ViewLayer *, view_layer, &sce->view_layers) {
    BKE_view_layer_blend_write(writer, view_layer);
  }

  if (sce->master_collection) {
    BLO_write_struct(writer, Collection, sce->master_collection);
    BKE_collection_blend_write_nolib(writer, sce->master_collection);
  }

  /* Eevee Lightcache */
  if (sce->eevee.light_cache_data && !BLO_write_is_undo(writer)) {
    BLO_write_struct(writer, LightCache, sce->eevee.light_cache_data);
    EEVEE_lightcache_blend_write(writer, sce->eevee.light_cache_data);
  }

  BKE_screen_view3d_shading_blend_write(writer, &sce->display.shading);

  /* Freed on doversion. */
  BLI_assert(sce->layer_properties == NULL);
}

static void direct_link_paint_helper(BlendDataReader *reader, const Scene *scene, Paint **paint)
{
  /* TODO. is this needed */
  BLO_read_data_address(reader, paint);

  if (*paint) {
    BKE_paint_blend_read_data(reader, scene, *paint);
  }
}

static void link_recurs_seq(BlendDataReader *reader, ListBase *lb)
{
  BLO_read_list(reader, lb);

  LISTBASE_FOREACH (Sequence *, seq, lb) {
    if (seq->seqbase.first) {
      link_recurs_seq(reader, &seq->seqbase);
    }
  }
}

static void scene_blend_read_data(BlendDataReader *reader, ID *id)
{
  Scene *sce = (Scene *)id;

  sce->depsgraph_hash = NULL;
  sce->fps_info = NULL;

  memset(&sce->customdata_mask, 0, sizeof(sce->customdata_mask));
  memset(&sce->customdata_mask_modal, 0, sizeof(sce->customdata_mask_modal));

  BKE_sound_reset_scene_runtime(sce);

  /* set users to one by default, not in lib-link, this will increase it for compo nodes */
  id_us_ensure_real(&sce->id);

  BLO_read_list(reader, &(sce->base));

  BLO_read_data_address(reader, &sce->adt);
  BKE_animdata_blend_read_data(reader, sce->adt);

  BLO_read_list(reader, &sce->keyingsets);
  BKE_keyingsets_blend_read_data(reader, &sce->keyingsets);

  BLO_read_data_address(reader, &sce->basact);

  BLO_read_data_address(reader, &sce->toolsettings);
  if (sce->toolsettings) {

    /* Reset last_location and last_hit, so they are not remembered across sessions. In some files
     * these are also NaN, which could lead to crashes in painting. */
    struct UnifiedPaintSettings *ups = &sce->toolsettings->unified_paint_settings;
    zero_v3(ups->last_location);
    ups->last_hit = 0;

    direct_link_paint_helper(reader, sce, (Paint **)&sce->toolsettings->sculpt);
    direct_link_paint_helper(reader, sce, (Paint **)&sce->toolsettings->vpaint);
    direct_link_paint_helper(reader, sce, (Paint **)&sce->toolsettings->wpaint);
    direct_link_paint_helper(reader, sce, (Paint **)&sce->toolsettings->uvsculpt);
    direct_link_paint_helper(reader, sce, (Paint **)&sce->toolsettings->gp_paint);
    direct_link_paint_helper(reader, sce, (Paint **)&sce->toolsettings->gp_vertexpaint);
    direct_link_paint_helper(reader, sce, (Paint **)&sce->toolsettings->gp_sculptpaint);
    direct_link_paint_helper(reader, sce, (Paint **)&sce->toolsettings->gp_weightpaint);

    BKE_paint_blend_read_data(reader, sce, &sce->toolsettings->imapaint.paint);

    sce->toolsettings->particle.paintcursor = NULL;
    sce->toolsettings->particle.scene = NULL;
    sce->toolsettings->particle.object = NULL;
    sce->toolsettings->gp_sculpt.paintcursor = NULL;

    /* relink grease pencil interpolation curves */
    BLO_read_data_address(reader, &sce->toolsettings->gp_interpolate.custom_ipo);
    if (sce->toolsettings->gp_interpolate.custom_ipo) {
      BKE_curvemapping_blend_read(reader, sce->toolsettings->gp_interpolate.custom_ipo);
    }
    /* relink grease pencil multiframe falloff curve */
    BLO_read_data_address(reader, &sce->toolsettings->gp_sculpt.cur_falloff);
    if (sce->toolsettings->gp_sculpt.cur_falloff) {
      BKE_curvemapping_blend_read(reader, sce->toolsettings->gp_sculpt.cur_falloff);
    }
    /* relink grease pencil primitive curve */
    BLO_read_data_address(reader, &sce->toolsettings->gp_sculpt.cur_primitive);
    if (sce->toolsettings->gp_sculpt.cur_primitive) {
      BKE_curvemapping_blend_read(reader, sce->toolsettings->gp_sculpt.cur_primitive);
    }

    /* Relink toolsettings curve profile */
    BLO_read_data_address(reader, &sce->toolsettings->custom_bevel_profile_preset);
    if (sce->toolsettings->custom_bevel_profile_preset) {
      BKE_curveprofile_blend_read(reader, sce->toolsettings->custom_bevel_profile_preset);
    }

    BLO_read_data_address(reader, &sce->toolsettings->sequencer_tool_settings);
  }

  if (sce->ed) {
    ListBase *old_seqbasep = &sce->ed->seqbase;

    BLO_read_data_address(reader, &sce->ed);
    Editing *ed = sce->ed;

    BLO_read_data_address(reader, &ed->act_seq);
    ed->cache = NULL;
    ed->prefetch_job = NULL;

    /* recursive link sequences, lb will be correctly initialized */
    link_recurs_seq(reader, &ed->seqbase);

    Sequence *seq;
    SEQ_ALL_BEGIN (ed, seq) {
      /* Do as early as possible, so that other parts of reading can rely on valid session UUID. */
      SEQ_relations_session_uuid_generate(seq);

      BLO_read_data_address(reader, &seq->seq1);
      BLO_read_data_address(reader, &seq->seq2);
      BLO_read_data_address(reader, &seq->seq3);

      /* a patch: after introduction of effects with 3 input strips */
      if (seq->seq3 == NULL) {
        seq->seq3 = seq->seq2;
      }

      BLO_read_data_address(reader, &seq->effectdata);
      BLO_read_data_address(reader, &seq->stereo3d_format);

      if (seq->type & SEQ_TYPE_EFFECT) {
        seq->flag |= SEQ_EFFECT_NOT_LOADED;
      }

      if (seq->type == SEQ_TYPE_SPEED) {
        SpeedControlVars *s = seq->effectdata;
        s->frameMap = NULL;
      }

      if (seq->type == SEQ_TYPE_TEXT) {
        TextVars *t = seq->effectdata;
        t->text_blf_id = SEQ_FONT_NOT_LOADED;
      }

      BLO_read_data_address(reader, &seq->prop);
      IDP_BlendDataRead(reader, &seq->prop);

      BLO_read_data_address(reader, &seq->strip);
      if (seq->strip && seq->strip->done == 0) {
        seq->strip->done = true;

        if (ELEM(seq->type,
                 SEQ_TYPE_IMAGE,
                 SEQ_TYPE_MOVIE,
                 SEQ_TYPE_SOUND_RAM,
                 SEQ_TYPE_SOUND_HD)) {
          BLO_read_data_address(reader, &seq->strip->stripdata);
        }
        else {
          seq->strip->stripdata = NULL;
        }
        BLO_read_data_address(reader, &seq->strip->crop);
        BLO_read_data_address(reader, &seq->strip->transform);
        BLO_read_data_address(reader, &seq->strip->proxy);
        if (seq->strip->proxy) {
          seq->strip->proxy->anim = NULL;
        }
        else if (seq->flag & SEQ_USE_PROXY) {
          SEQ_proxy_set(seq, true);
        }

        /* need to load color balance to it could be converted to modifier */
        BLO_read_data_address(reader, &seq->strip->color_balance);
      }

      SEQ_modifier_blend_read_data(reader, &seq->modifiers);
    }
    SEQ_ALL_END;

    /* link metastack, slight abuse of structs here,
     * have to restore pointer to internal part in struct */
    {
      Sequence temp;
      void *poin;
      intptr_t offset;

      offset = ((intptr_t) & (temp.seqbase)) - ((intptr_t)&temp);

      /* root pointer */
      if (ed->seqbasep == old_seqbasep) {
        ed->seqbasep = &ed->seqbase;
      }
      else {
        poin = POINTER_OFFSET(ed->seqbasep, -offset);

        poin = BLO_read_get_new_data_address(reader, poin);

        if (poin) {
          ed->seqbasep = (ListBase *)POINTER_OFFSET(poin, offset);
        }
        else {
          ed->seqbasep = &ed->seqbase;
        }
      }
      /* stack */
      BLO_read_list(reader, &(ed->metastack));

      LISTBASE_FOREACH (MetaStack *, ms, &ed->metastack) {
        BLO_read_data_address(reader, &ms->parseq);

        if (ms->oldbasep == old_seqbasep) {
          ms->oldbasep = &ed->seqbase;
        }
        else {
          poin = POINTER_OFFSET(ms->oldbasep, -offset);
          poin = BLO_read_get_new_data_address(reader, poin);
          if (poin) {
            ms->oldbasep = (ListBase *)POINTER_OFFSET(poin, offset);
          }
          else {
            ms->oldbasep = &ed->seqbase;
          }
        }
      }
    }
  }

#ifdef DURIAN_CAMERA_SWITCH
  /* Runtime */
  sce->r.mode &= ~R_NO_CAMERA_SWITCH;
#endif

  BLO_read_data_address(reader, &sce->r.avicodecdata);
  if (sce->r.avicodecdata) {
    BLO_read_data_address(reader, &sce->r.avicodecdata->lpFormat);
    BLO_read_data_address(reader, &sce->r.avicodecdata->lpParms);
  }
  if (sce->r.ffcodecdata.properties) {
    BLO_read_data_address(reader, &sce->r.ffcodecdata.properties);
    IDP_BlendDataRead(reader, &sce->r.ffcodecdata.properties);
  }

  BLO_read_list(reader, &(sce->markers));
  LISTBASE_FOREACH (TimeMarker *, marker, &sce->markers) {
    BLO_read_data_address(reader, &marker->prop);
    IDP_BlendDataRead(reader, &marker->prop);
  }

  BLO_read_list(reader, &(sce->transform_spaces));
  BLO_read_list(reader, &(sce->r.layers));
  BLO_read_list(reader, &(sce->r.views));

  LISTBASE_FOREACH (SceneRenderLayer *, srl, &sce->r.layers) {
    BLO_read_data_address(reader, &srl->prop);
    IDP_BlendDataRead(reader, &srl->prop);
    BLO_read_list(reader, &(srl->freestyleConfig.modules));
    BLO_read_list(reader, &(srl->freestyleConfig.linesets));
  }

  BKE_color_managed_view_settings_blend_read_data(reader, &sce->view_settings);

  BLO_read_data_address(reader, &sce->rigidbody_world);
  RigidBodyWorld *rbw = sce->rigidbody_world;
  if (rbw) {
    BLO_read_data_address(reader, &rbw->shared);

    if (rbw->shared == NULL) {
      /* Link deprecated caches if they exist, so we can use them for versioning.
       * We should only do this when rbw->shared == NULL, because those pointers
       * are always set (for compatibility with older Blenders). We mustn't link
       * the same pointcache twice. */
      BKE_ptcache_blend_read_data(reader, &rbw->ptcaches, &rbw->pointcache, false);

      /* make sure simulation starts from the beginning after loading file */
      if (rbw->pointcache) {
        rbw->ltime = (float)rbw->pointcache->startframe;
      }
    }
    else {
      /* must nullify the reference to physics sim object, since it no-longer exist
       * (and will need to be recalculated)
       */
      rbw->shared->physics_world = NULL;

      /* link caches */
      BKE_ptcache_blend_read_data(reader, &rbw->shared->ptcaches, &rbw->shared->pointcache, false);

      /* make sure simulation starts from the beginning after loading file */
      if (rbw->shared->pointcache) {
        rbw->ltime = (float)rbw->shared->pointcache->startframe;
      }
    }
    rbw->objects = NULL;
    rbw->numbodies = 0;

    /* set effector weights */
    BLO_read_data_address(reader, &rbw->effector_weights);
    if (!rbw->effector_weights) {
      rbw->effector_weights = BKE_effector_add_weights(NULL);
    }
  }

  BLO_read_data_address(reader, &sce->preview);
  BKE_previewimg_blend_read(reader, sce->preview);

  BKE_curvemapping_blend_read(reader, &sce->r.mblur_shutter_curve);

#ifdef USE_COLLECTION_COMPAT_28
  /* this runs before the very first doversion */
  if (sce->collection) {
    BLO_read_data_address(reader, &sce->collection);
    BKE_collection_compat_blend_read_data(reader, sce->collection);
  }
#endif

  /* insert into global old-new map for reading without UI (link_global accesses it again) */
  BLO_read_glob_list(reader, &sce->view_layers);
  LISTBASE_FOREACH (ViewLayer *, view_layer, &sce->view_layers) {
    BKE_view_layer_blend_read_data(reader, view_layer);
  }

  if (BLO_read_data_is_undo(reader)) {
    /* If it's undo do nothing here, caches are handled by higher-level generic calling code. */
  }
  else {
    /* else try to read the cache from file. */
    BLO_read_data_address(reader, &sce->eevee.light_cache_data);
    if (sce->eevee.light_cache_data) {
      EEVEE_lightcache_blend_read_data(reader, sce->eevee.light_cache_data);
    }
  }
  EEVEE_lightcache_info_update(&sce->eevee);

  BKE_screen_view3d_shading_blend_read_data(reader, &sce->display.shading);

  BLO_read_data_address(reader, &sce->layer_properties);
  IDP_BlendDataRead(reader, &sce->layer_properties);
}

/* patch for missing scene IDs, can't be in do-versions */
static void composite_patch(bNodeTree *ntree, Scene *scene)
{
  LISTBASE_FOREACH (bNode *, node, &ntree->nodes) {
    if (node->id == NULL &&
        ((node->type == CMP_NODE_R_LAYERS) ||
         (node->type == CMP_NODE_CRYPTOMATTE && node->custom1 == CMP_CRYPTOMATTE_SRC_RENDER))) {
      node->id = &scene->id;
    }
  }
}

static void scene_blend_read_lib(BlendLibReader *reader, ID *id)
{
  Scene *sce = (Scene *)id;

  BKE_keyingsets_blend_read_lib(reader, &sce->id, &sce->keyingsets);

  BLO_read_id_address(reader, sce->id.lib, &sce->camera);
  BLO_read_id_address(reader, sce->id.lib, &sce->world);
  BLO_read_id_address(reader, sce->id.lib, &sce->set);
  BLO_read_id_address(reader, sce->id.lib, &sce->gpd);

  BKE_paint_blend_read_lib(reader, sce, &sce->toolsettings->imapaint.paint);
  if (sce->toolsettings->sculpt) {
    BKE_paint_blend_read_lib(reader, sce, &sce->toolsettings->sculpt->paint);
  }
  if (sce->toolsettings->vpaint) {
    BKE_paint_blend_read_lib(reader, sce, &sce->toolsettings->vpaint->paint);
  }
  if (sce->toolsettings->wpaint) {
    BKE_paint_blend_read_lib(reader, sce, &sce->toolsettings->wpaint->paint);
  }
  if (sce->toolsettings->uvsculpt) {
    BKE_paint_blend_read_lib(reader, sce, &sce->toolsettings->uvsculpt->paint);
  }
  if (sce->toolsettings->gp_paint) {
    BKE_paint_blend_read_lib(reader, sce, &sce->toolsettings->gp_paint->paint);
  }
  if (sce->toolsettings->gp_vertexpaint) {
    BKE_paint_blend_read_lib(reader, sce, &sce->toolsettings->gp_vertexpaint->paint);
  }
  if (sce->toolsettings->gp_sculptpaint) {
    BKE_paint_blend_read_lib(reader, sce, &sce->toolsettings->gp_sculptpaint->paint);
  }
  if (sce->toolsettings->gp_weightpaint) {
    BKE_paint_blend_read_lib(reader, sce, &sce->toolsettings->gp_weightpaint->paint);
  }

  if (sce->toolsettings->sculpt) {
    BLO_read_id_address(reader, sce->id.lib, &sce->toolsettings->sculpt->gravity_object);
  }

  if (sce->toolsettings->imapaint.stencil) {
    BLO_read_id_address(reader, sce->id.lib, &sce->toolsettings->imapaint.stencil);
  }

  if (sce->toolsettings->imapaint.clone) {
    BLO_read_id_address(reader, sce->id.lib, &sce->toolsettings->imapaint.clone);
  }

  if (sce->toolsettings->imapaint.canvas) {
    BLO_read_id_address(reader, sce->id.lib, &sce->toolsettings->imapaint.canvas);
  }

  BLO_read_id_address(reader, sce->id.lib, &sce->toolsettings->particle.shape_object);

  BLO_read_id_address(reader, sce->id.lib, &sce->toolsettings->gp_sculpt.guide.reference_object);

  LISTBASE_FOREACH_MUTABLE (Base *, base_legacy, &sce->base) {
    BLO_read_id_address(reader, sce->id.lib, &base_legacy->object);

    if (base_legacy->object == NULL) {
      BLO_reportf_wrap(BLO_read_lib_reports(reader),
                       RPT_WARNING,
                       TIP_("LIB: object lost from scene: '%s'"),
                       sce->id.name + 2);
      BLI_remlink(&sce->base, base_legacy);
      if (base_legacy == sce->basact) {
        sce->basact = NULL;
      }
      MEM_freeN(base_legacy);
    }
  }

  Sequence *seq;
  SEQ_ALL_BEGIN (sce->ed, seq) {
    IDP_BlendReadLib(reader, seq->prop);

    if (seq->ipo) {
      BLO_read_id_address(
          reader, sce->id.lib, &seq->ipo); /* XXX deprecated - old animation system */
    }
    seq->scene_sound = NULL;
    if (seq->scene) {
      BLO_read_id_address(reader, sce->id.lib, &seq->scene);
      seq->scene_sound = NULL;
    }
    if (seq->clip) {
      BLO_read_id_address(reader, sce->id.lib, &seq->clip);
    }
    if (seq->mask) {
      BLO_read_id_address(reader, sce->id.lib, &seq->mask);
    }
    if (seq->scene_camera) {
      BLO_read_id_address(reader, sce->id.lib, &seq->scene_camera);
    }
    if (seq->sound) {
      seq->scene_sound = NULL;
      if (seq->type == SEQ_TYPE_SOUND_HD) {
        seq->type = SEQ_TYPE_SOUND_RAM;
      }
      else {
        BLO_read_id_address(reader, sce->id.lib, &seq->sound);
      }
      if (seq->sound) {
        id_us_plus_no_lib((ID *)seq->sound);
        seq->scene_sound = NULL;
      }
    }
    if (seq->type == SEQ_TYPE_TEXT) {
      TextVars *t = seq->effectdata;
      BLO_read_id_address(reader, sce->id.lib, &t->text_font);
    }
    BLI_listbase_clear(&seq->anims);

    SEQ_modifier_blend_read_lib(reader, sce, &seq->modifiers);
  }
  SEQ_ALL_END;

  LISTBASE_FOREACH (TimeMarker *, marker, &sce->markers) {
    IDP_BlendReadLib(reader, marker->prop);

    if (marker->camera) {
      BLO_read_id_address(reader, sce->id.lib, &marker->camera);
    }
  }

  /* rigidbody world relies on its linked collections */
  if (sce->rigidbody_world) {
    RigidBodyWorld *rbw = sce->rigidbody_world;
    if (rbw->group) {
      BLO_read_id_address(reader, sce->id.lib, &rbw->group);
    }
    if (rbw->constraints) {
      BLO_read_id_address(reader, sce->id.lib, &rbw->constraints);
    }
    if (rbw->effector_weights) {
      BLO_read_id_address(reader, sce->id.lib, &rbw->effector_weights->group);
    }
  }

  if (sce->nodetree) {
    composite_patch(sce->nodetree, sce);
  }

  LISTBASE_FOREACH (SceneRenderLayer *, srl, &sce->r.layers) {
    BLO_read_id_address(reader, sce->id.lib, &srl->mat_override);
    LISTBASE_FOREACH (FreestyleModuleConfig *, fmc, &srl->freestyleConfig.modules) {
      BLO_read_id_address(reader, sce->id.lib, &fmc->script);
    }
    LISTBASE_FOREACH (FreestyleLineSet *, fls, &srl->freestyleConfig.linesets) {
      BLO_read_id_address(reader, sce->id.lib, &fls->linestyle);
      BLO_read_id_address(reader, sce->id.lib, &fls->group);
    }
  }
  /* Motion Tracking */
  BLO_read_id_address(reader, sce->id.lib, &sce->clip);

#ifdef USE_COLLECTION_COMPAT_28
  if (sce->collection) {
    BKE_collection_compat_blend_read_lib(reader, sce->id.lib, sce->collection);
  }
#endif

  LISTBASE_FOREACH (ViewLayer *, view_layer, &sce->view_layers) {
    BKE_view_layer_blend_read_lib(reader, sce->id.lib, view_layer);
  }

  if (sce->r.bake.cage_object) {
    BLO_read_id_address(reader, sce->id.lib, &sce->r.bake.cage_object);
  }

#ifdef USE_SETSCENE_CHECK
  if (sce->set != NULL) {
    sce->flag |= SCE_READFILE_LIBLINK_NEED_SETSCENE_CHECK;
  }
#endif
}

static void scene_blend_read_expand(BlendExpander *expander, ID *id)
{
  Scene *sce = (Scene *)id;

  LISTBASE_FOREACH (Base *, base_legacy, &sce->base) {
    BLO_expand(expander, base_legacy->object);
  }
  BLO_expand(expander, sce->camera);
  BLO_expand(expander, sce->world);

  BKE_keyingsets_blend_read_expand(expander, &sce->keyingsets);

  if (sce->set) {
    BLO_expand(expander, sce->set);
  }

  LISTBASE_FOREACH (SceneRenderLayer *, srl, &sce->r.layers) {
    BLO_expand(expander, srl->mat_override);
    LISTBASE_FOREACH (FreestyleModuleConfig *, module, &srl->freestyleConfig.modules) {
      if (module->script) {
        BLO_expand(expander, module->script);
      }
    }
    LISTBASE_FOREACH (FreestyleLineSet *, lineset, &srl->freestyleConfig.linesets) {
      if (lineset->group) {
        BLO_expand(expander, lineset->group);
      }
      BLO_expand(expander, lineset->linestyle);
    }
  }

  LISTBASE_FOREACH (ViewLayer *, view_layer, &sce->view_layers) {
    IDP_BlendReadExpand(expander, view_layer->id_properties);

    LISTBASE_FOREACH (FreestyleModuleConfig *, module, &view_layer->freestyle_config.modules) {
      if (module->script) {
        BLO_expand(expander, module->script);
      }
    }

    LISTBASE_FOREACH (FreestyleLineSet *, lineset, &view_layer->freestyle_config.linesets) {
      if (lineset->group) {
        BLO_expand(expander, lineset->group);
      }
      BLO_expand(expander, lineset->linestyle);
    }
  }

  if (sce->gpd) {
    BLO_expand(expander, sce->gpd);
  }

  if (sce->ed) {
    Sequence *seq;

    SEQ_ALL_BEGIN (sce->ed, seq) {
      IDP_BlendReadExpand(expander, seq->prop);

      if (seq->scene) {
        BLO_expand(expander, seq->scene);
      }
      if (seq->scene_camera) {
        BLO_expand(expander, seq->scene_camera);
      }
      if (seq->clip) {
        BLO_expand(expander, seq->clip);
      }
      if (seq->mask) {
        BLO_expand(expander, seq->mask);
      }
      if (seq->sound) {
        BLO_expand(expander, seq->sound);
      }

      if (seq->type == SEQ_TYPE_TEXT && seq->effectdata) {
        TextVars *data = seq->effectdata;
        BLO_expand(expander, data->text_font);
      }
    }
    SEQ_ALL_END;
  }

  if (sce->rigidbody_world) {
    BLO_expand(expander, sce->rigidbody_world->group);
    BLO_expand(expander, sce->rigidbody_world->constraints);
  }

  LISTBASE_FOREACH (TimeMarker *, marker, &sce->markers) {
    IDP_BlendReadExpand(expander, marker->prop);

    if (marker->camera) {
      BLO_expand(expander, marker->camera);
    }
  }

  BLO_expand(expander, sce->clip);

#ifdef USE_COLLECTION_COMPAT_28
  if (sce->collection) {
    BKE_collection_compat_blend_read_expand(expander, sce->collection);
  }
#endif

  if (sce->r.bake.cage_object) {
    BLO_expand(expander, sce->r.bake.cage_object);
  }
}

static void scene_undo_preserve(BlendLibReader *reader, ID *id_new, ID *id_old)
{
  Scene *scene_new = (Scene *)id_new;
  Scene *scene_old = (Scene *)id_old;

  SWAP(View3DCursor, scene_old->cursor, scene_new->cursor);
  if (scene_new->toolsettings != NULL && scene_old->toolsettings != NULL) {
    /* First try to restore ID pointers that can be and should be preserved (like brushes or
     * palettes), and counteract the swap of the whole ToolSettings structs below for the others
     * (like object ones). */
    scene_foreach_toolsettings(
        NULL, scene_new->toolsettings, true, reader, scene_old->toolsettings);
    SWAP(ToolSettings, *scene_old->toolsettings, *scene_new->toolsettings);
  }
}

static void scene_lib_override_apply_post(ID *id_dst, ID *UNUSED(id_src))
{
  Scene *scene = (Scene *)id_dst;

  if (scene->rigidbody_world != NULL) {
    PTCacheID pid;
    BKE_ptcache_id_from_rigidbody(&pid, NULL, scene->rigidbody_world);
    LISTBASE_FOREACH (PointCache *, point_cache, pid.ptcaches) {
      point_cache->flag |= PTCACHE_FLAG_INFO_DIRTY;
    }
  }
}

IDTypeInfo IDType_ID_SCE = {
    .id_code = ID_SCE,
    .id_filter = FILTER_ID_SCE,
    .main_listbase_index = INDEX_ID_SCE,
    .struct_size = sizeof(Scene),
    .name = "Scene",
    .name_plural = "scenes",
    .translation_context = BLT_I18NCONTEXT_ID_SCENE,
    .flags = 0,

    .init_data = scene_init_data,
    .copy_data = scene_copy_data,
    .free_data = scene_free_data,
    /* For now default `BKE_lib_id_make_local_generic()` should work, may need more work though to
     * support all possible corner cases. */
    .make_local = NULL,
    .foreach_id = scene_foreach_id,
    .foreach_cache = scene_foreach_cache,
    .owner_get = NULL,

    .blend_write = scene_blend_write,
    .blend_read_data = scene_blend_read_data,
    .blend_read_lib = scene_blend_read_lib,
    .blend_read_expand = scene_blend_read_expand,

    .blend_read_undo_preserve = scene_undo_preserve,

    .lib_override_apply_post = scene_lib_override_apply_post,
};

const char *RE_engine_id_BLENDER_EEVEE = "BLENDER_EEVEE";
const char *RE_engine_id_BLENDER_WORKBENCH = "BLENDER_WORKBENCH";
const char *RE_engine_id_CYCLES = "CYCLES";
const char *RE_engine_id_OCTANE = "octane";

void free_avicodecdata(AviCodecData *acd)
{
  if (acd) {
    if (acd->lpFormat) {
      MEM_freeN(acd->lpFormat);
      acd->lpFormat = NULL;
      acd->cbFormat = 0;
    }
    if (acd->lpParms) {
      MEM_freeN(acd->lpParms);
      acd->lpParms = NULL;
      acd->cbParms = 0;
    }
  }
}

static void remove_sequencer_fcurves(Scene *sce)
{
  AnimData *adt = BKE_animdata_from_id(&sce->id);

  if (adt && adt->action) {
    FCurve *fcu, *nextfcu;

    for (fcu = adt->action->curves.first; fcu; fcu = nextfcu) {
      nextfcu = fcu->next;

      if ((fcu->rna_path) && strstr(fcu->rna_path, "sequences_all")) {
        action_groups_remove_channel(adt->action, fcu);
        BKE_fcurve_free(fcu);
      }
    }
  }
}

/* flag -- copying options (see BKE_lib_id.h's LIB_ID_COPY_... flags for more). */
ToolSettings *BKE_toolsettings_copy(ToolSettings *toolsettings, const int flag)
{
  if (toolsettings == NULL) {
    return NULL;
  }
  ToolSettings *ts = MEM_dupallocN(toolsettings);
  if (ts->vpaint) {
    ts->vpaint = MEM_dupallocN(ts->vpaint);
    BKE_paint_copy(&ts->vpaint->paint, &ts->vpaint->paint, flag);
  }
  if (ts->wpaint) {
    ts->wpaint = MEM_dupallocN(ts->wpaint);
    BKE_paint_copy(&ts->wpaint->paint, &ts->wpaint->paint, flag);
  }
  if (ts->sculpt) {
    ts->sculpt = MEM_dupallocN(ts->sculpt);
    BKE_paint_copy(&ts->sculpt->paint, &ts->sculpt->paint, flag);
  }
  if (ts->uvsculpt) {
    ts->uvsculpt = MEM_dupallocN(ts->uvsculpt);
    BKE_paint_copy(&ts->uvsculpt->paint, &ts->uvsculpt->paint, flag);
  }
  if (ts->gp_paint) {
    ts->gp_paint = MEM_dupallocN(ts->gp_paint);
    BKE_paint_copy(&ts->gp_paint->paint, &ts->gp_paint->paint, flag);
  }
  if (ts->gp_vertexpaint) {
    ts->gp_vertexpaint = MEM_dupallocN(ts->gp_vertexpaint);
    BKE_paint_copy(&ts->gp_vertexpaint->paint, &ts->gp_vertexpaint->paint, flag);
  }
  if (ts->gp_sculptpaint) {
    ts->gp_sculptpaint = MEM_dupallocN(ts->gp_sculptpaint);
    BKE_paint_copy(&ts->gp_sculptpaint->paint, &ts->gp_sculptpaint->paint, flag);
  }
  if (ts->gp_weightpaint) {
    ts->gp_weightpaint = MEM_dupallocN(ts->gp_weightpaint);
    BKE_paint_copy(&ts->gp_weightpaint->paint, &ts->gp_weightpaint->paint, flag);
  }

  BKE_paint_copy(&ts->imapaint.paint, &ts->imapaint.paint, flag);
  ts->particle.paintcursor = NULL;
  ts->particle.scene = NULL;
  ts->particle.object = NULL;

  /* duplicate Grease Pencil interpolation curve */
  ts->gp_interpolate.custom_ipo = BKE_curvemapping_copy(ts->gp_interpolate.custom_ipo);
  /* Duplicate Grease Pencil multiframe falloff. */
  ts->gp_sculpt.cur_falloff = BKE_curvemapping_copy(ts->gp_sculpt.cur_falloff);
  ts->gp_sculpt.cur_primitive = BKE_curvemapping_copy(ts->gp_sculpt.cur_primitive);

  ts->custom_bevel_profile_preset = BKE_curveprofile_copy(ts->custom_bevel_profile_preset);

  ts->sequencer_tool_settings = SEQ_tool_settings_copy(ts->sequencer_tool_settings);
  return ts;
}

void BKE_toolsettings_free(ToolSettings *toolsettings)
{
  if (toolsettings == NULL) {
    return;
  }
  if (toolsettings->vpaint) {
    BKE_paint_free(&toolsettings->vpaint->paint);
    MEM_freeN(toolsettings->vpaint);
  }
  if (toolsettings->wpaint) {
    BKE_paint_free(&toolsettings->wpaint->paint);
    MEM_freeN(toolsettings->wpaint);
  }
  if (toolsettings->sculpt) {
    BKE_paint_free(&toolsettings->sculpt->paint);
    MEM_freeN(toolsettings->sculpt);
  }
  if (toolsettings->uvsculpt) {
    BKE_paint_free(&toolsettings->uvsculpt->paint);
    MEM_freeN(toolsettings->uvsculpt);
  }
  if (toolsettings->gp_paint) {
    BKE_paint_free(&toolsettings->gp_paint->paint);
    MEM_freeN(toolsettings->gp_paint);
  }
  if (toolsettings->gp_vertexpaint) {
    BKE_paint_free(&toolsettings->gp_vertexpaint->paint);
    MEM_freeN(toolsettings->gp_vertexpaint);
  }
  if (toolsettings->gp_sculptpaint) {
    BKE_paint_free(&toolsettings->gp_sculptpaint->paint);
    MEM_freeN(toolsettings->gp_sculptpaint);
  }
  if (toolsettings->gp_weightpaint) {
    BKE_paint_free(&toolsettings->gp_weightpaint->paint);
    MEM_freeN(toolsettings->gp_weightpaint);
  }
  BKE_paint_free(&toolsettings->imapaint.paint);

  /* free Grease Pencil interpolation curve */
  if (toolsettings->gp_interpolate.custom_ipo) {
    BKE_curvemapping_free(toolsettings->gp_interpolate.custom_ipo);
  }
  /* free Grease Pencil multiframe falloff curve */
  if (toolsettings->gp_sculpt.cur_falloff) {
    BKE_curvemapping_free(toolsettings->gp_sculpt.cur_falloff);
  }
  if (toolsettings->gp_sculpt.cur_primitive) {
    BKE_curvemapping_free(toolsettings->gp_sculpt.cur_primitive);
  }

  if (toolsettings->custom_bevel_profile_preset) {
    BKE_curveprofile_free(toolsettings->custom_bevel_profile_preset);
  }

  if (toolsettings->sequencer_tool_settings) {
    SEQ_tool_settings_free(toolsettings->sequencer_tool_settings);
  }

  MEM_freeN(toolsettings);
}

void BKE_scene_copy_data_eevee(Scene *sce_dst, const Scene *sce_src)
{
  /* Copy eevee data between scenes. */
  sce_dst->eevee = sce_src->eevee;
  sce_dst->eevee.light_cache_data = NULL;
  sce_dst->eevee.light_cache_info[0] = '\0';
  /* TODO Copy the cache. */
}

Scene *BKE_scene_duplicate(Main *bmain, Scene *sce, eSceneCopyMethod type)
{
  Scene *sce_copy;

  /* TODO this should/could most likely be replaced by call to more generic code at some point...
   * But for now, let's keep it well isolated here. */
  if (type == SCE_COPY_EMPTY) {
    ListBase rv;

    sce_copy = BKE_scene_add(bmain, sce->id.name + 2);

    rv = sce_copy->r.views;
    BKE_curvemapping_free_data(&sce_copy->r.mblur_shutter_curve);
    sce_copy->r = sce->r;
    sce_copy->r.views = rv;
    sce_copy->unit = sce->unit;
    sce_copy->physics_settings = sce->physics_settings;
    sce_copy->audio = sce->audio;
    BKE_scene_copy_data_eevee(sce_copy, sce);

    if (sce->id.properties) {
      sce_copy->id.properties = IDP_CopyProperty(sce->id.properties);
    }

    BKE_sound_destroy_scene(sce_copy);

    /* copy color management settings */
    BKE_color_managed_display_settings_copy(&sce_copy->display_settings, &sce->display_settings);
    BKE_color_managed_view_settings_copy(&sce_copy->view_settings, &sce->view_settings);
    BKE_color_managed_colorspace_settings_copy(&sce_copy->sequencer_colorspace_settings,
                                               &sce->sequencer_colorspace_settings);

    BKE_color_managed_display_settings_copy(&sce_copy->r.im_format.display_settings,
                                            &sce->r.im_format.display_settings);
    BKE_color_managed_view_settings_copy(&sce_copy->r.im_format.view_settings,
                                         &sce->r.im_format.view_settings);

    BKE_color_managed_display_settings_copy(&sce_copy->r.bake.im_format.display_settings,
                                            &sce->r.bake.im_format.display_settings);
    BKE_color_managed_view_settings_copy(&sce_copy->r.bake.im_format.view_settings,
                                         &sce->r.bake.im_format.view_settings);

    BKE_curvemapping_copy_data(&sce_copy->r.mblur_shutter_curve, &sce->r.mblur_shutter_curve);

    /* viewport display settings */
    sce_copy->display = sce->display;

    /* tool settings */
    BKE_toolsettings_free(sce_copy->toolsettings);
    sce_copy->toolsettings = BKE_toolsettings_copy(sce->toolsettings, 0);

    /* make a private copy of the avicodecdata */
    if (sce->r.avicodecdata) {
      sce_copy->r.avicodecdata = MEM_dupallocN(sce->r.avicodecdata);
      sce_copy->r.avicodecdata->lpFormat = MEM_dupallocN(sce_copy->r.avicodecdata->lpFormat);
      sce_copy->r.avicodecdata->lpParms = MEM_dupallocN(sce_copy->r.avicodecdata->lpParms);
    }

    if (sce->r.ffcodecdata.properties) { /* intentionally check scen not sce. */
      sce_copy->r.ffcodecdata.properties = IDP_CopyProperty(sce->r.ffcodecdata.properties);
    }

    BKE_sound_reset_scene_runtime(sce_copy);

    /* grease pencil */
    sce_copy->gpd = NULL;

    sce_copy->preview = NULL;

    return sce_copy;
  }

  eDupli_ID_Flags duplicate_flags = U.dupflag | USER_DUP_OBJECT;

  sce_copy = (Scene *)BKE_id_copy(bmain, (ID *)sce);
  id_us_min(&sce_copy->id);
  id_us_ensure_real(&sce_copy->id);

  BKE_animdata_duplicate_id_action(bmain, &sce_copy->id, duplicate_flags);

  /* Extra actions, most notably SCE_FULL_COPY also duplicates several 'children' datablocks. */

  if (type == SCE_COPY_FULL) {
    /* Scene duplication is always root of duplication currently. */
    const bool is_subprocess = false;

    if (!is_subprocess) {
      BKE_main_id_tag_all(bmain, LIB_TAG_NEW, false);
      BKE_main_id_clear_newpoins(bmain);
      /* In case root duplicated ID is linked, assume we want to get a local copy of it and
       * duplicate all expected linked data. */
      if (ID_IS_LINKED(sce)) {
        duplicate_flags |= USER_DUP_LINKED_ID;
      }
    }

    /* Copy Freestyle LineStyle datablocks. */
    LISTBASE_FOREACH (ViewLayer *, view_layer_dst, &sce_copy->view_layers) {
      LISTBASE_FOREACH (FreestyleLineSet *, lineset, &view_layer_dst->freestyle_config.linesets) {
        BKE_id_copy_for_duplicate(bmain, (ID *)lineset->linestyle, duplicate_flags);
      }
    }

    /* Full copy of world (included animations) */
    BKE_id_copy_for_duplicate(bmain, (ID *)sce->world, duplicate_flags);

    /* Full copy of GreasePencil. */
    BKE_id_copy_for_duplicate(bmain, (ID *)sce->gpd, duplicate_flags);

    /* Deep-duplicate collections and objects (using preferences' settings for which sub-data to
     * duplicate along the object itself). */
    BKE_collection_duplicate(
        bmain, NULL, sce_copy->master_collection, duplicate_flags, LIB_ID_DUPLICATE_IS_SUBPROCESS);

    if (!is_subprocess) {
      /* This code will follow into all ID links using an ID tagged with LIB_TAG_NEW.*/
      BKE_libblock_relink_to_newid(&sce_copy->id);

#ifndef NDEBUG
      /* Call to `BKE_libblock_relink_to_newid` above is supposed to have cleared all those
       * flags. */
      ID *id_iter;
      FOREACH_MAIN_ID_BEGIN (bmain, id_iter) {
        BLI_assert((id_iter->tag & LIB_TAG_NEW) == 0);
      }
      FOREACH_MAIN_ID_END;
#endif

      /* Cleanup. */
      BKE_main_id_tag_all(bmain, LIB_TAG_NEW, false);
      BKE_main_id_clear_newpoins(bmain);

      BKE_main_collection_sync(bmain);
    }
  }
  else {
    /* Remove sequencer if not full copy */
    /* XXX Why in Hell? :/ */
    remove_sequencer_fcurves(sce_copy);
    SEQ_editing_free(sce_copy, true);
  }

  return sce_copy;
}

void BKE_scene_groups_relink(Scene *sce)
{
  if (sce->rigidbody_world) {
    BKE_rigidbody_world_groups_relink(sce->rigidbody_world);
  }
}

bool BKE_scene_can_be_removed(const Main *bmain, const Scene *scene)
{
  /* Linked scenes can always be removed. */
  if (ID_IS_LINKED(scene)) {
    return true;
  }
  /* Local scenes can only be removed, when there is at least one local scene left. */
  LISTBASE_FOREACH (Scene *, other_scene, &bmain->scenes) {
    if (other_scene != scene && !ID_IS_LINKED(other_scene)) {
      return true;
    }
  }
  return false;
}

Scene *BKE_scene_add(Main *bmain, const char *name)
{
  Scene *sce;

  sce = BKE_id_new(bmain, ID_SCE, name);
  id_us_min(&sce->id);
  id_us_ensure_real(&sce->id);

  return sce;
}

/**
 * Check if there is any instance of the object in the scene
 */
bool BKE_scene_object_find(Scene *scene, Object *ob)
{
  LISTBASE_FOREACH (ViewLayer *, view_layer, &scene->view_layers) {
    if (BLI_findptr(&view_layer->object_bases, ob, offsetof(Base, object))) {
      return true;
    }
  }
  return false;
}

Object *BKE_scene_object_find_by_name(const Scene *scene, const char *name)
{
  LISTBASE_FOREACH (ViewLayer *, view_layer, &scene->view_layers) {
    LISTBASE_FOREACH (Base *, base, &view_layer->object_bases) {
      if (STREQ(base->object->id.name + 2, name)) {
        return base->object;
      }
    }
  }
  return NULL;
}

/**
 * Sets the active scene, mainly used when running in background mode
 * (``--scene`` command line argument).
 * This is also called to set the scene directly, bypassing windowing code.
 * Otherwise #WM_window_set_active_scene is used when changing scenes by the user.
 */
void BKE_scene_set_background(Main *bmain, Scene *scene)
{
  Object *ob;

  /* check for cyclic sets, for reading old files but also for definite security (py?) */
  BKE_scene_validate_setscene(bmain, scene);

  /* deselect objects (for dataselect) */
  for (ob = bmain->objects.first; ob; ob = ob->id.next) {
    ob->flag &= ~SELECT;
  }

  /* copy layers and flags from bases to objects */
  LISTBASE_FOREACH (ViewLayer *, view_layer, &scene->view_layers) {
    LISTBASE_FOREACH (Base *, base, &view_layer->object_bases) {
      ob = base->object;
      /* collection patch... */
      BKE_scene_object_base_flag_sync_from_base(base);
    }
  }
  /* No full animation update, this to enable render code to work
   * (render code calls own animation updates). */
}

/* called from creator_args.c */
Scene *BKE_scene_set_name(Main *bmain, const char *name)
{
  Scene *sce = (Scene *)BKE_libblock_find_name(bmain, ID_SCE, name);
  if (sce) {
    BKE_scene_set_background(bmain, sce);
    printf("Scene switch for render: '%s' in file: '%s'\n", name, BKE_main_blendfile_path(bmain));
    return sce;
  }

  printf("Can't find scene: '%s' in file: '%s'\n", name, BKE_main_blendfile_path(bmain));
  return NULL;
}

/* Used by meta-balls, return *all* objects (including duplis)
 * existing in the scene (including scene's sets). */
int BKE_scene_base_iter_next(
    Depsgraph *depsgraph, SceneBaseIter *iter, Scene **scene, int val, Base **base, Object **ob)
{
  bool run_again = true;

  /* init */
  if (val == 0) {
    iter->phase = F_START;
    iter->dupob = NULL;
    iter->duplilist = NULL;
    iter->dupli_refob = NULL;
  }
  else {
    /* run_again is set when a duplilist has been ended */
    while (run_again) {
      run_again = false;

      /* the first base */
      if (iter->phase == F_START) {
        ViewLayer *view_layer = (depsgraph) ? DEG_get_evaluated_view_layer(depsgraph) :
                                              BKE_view_layer_context_active_PLACEHOLDER(*scene);
        *base = view_layer->object_bases.first;
        if (*base) {
          *ob = (*base)->object;
          iter->phase = F_SCENE;
        }
        else {
          /* exception: empty scene layer */
          while ((*scene)->set) {
            (*scene) = (*scene)->set;
            ViewLayer *view_layer_set = BKE_view_layer_default_render((*scene));
            if (view_layer_set->object_bases.first) {
              *base = view_layer_set->object_bases.first;
              *ob = (*base)->object;
              iter->phase = F_SCENE;
              break;
            }
          }
        }
      }
      else {
        if (*base && iter->phase != F_DUPLI) {
          *base = (*base)->next;
          if (*base) {
            *ob = (*base)->object;
          }
          else {
            if (iter->phase == F_SCENE) {
              /* (*scene) is finished, now do the set */
              while ((*scene)->set) {
                (*scene) = (*scene)->set;
                ViewLayer *view_layer_set = BKE_view_layer_default_render((*scene));
                if (view_layer_set->object_bases.first) {
                  *base = view_layer_set->object_bases.first;
                  *ob = (*base)->object;
                  break;
                }
              }
            }
          }
        }
      }

      if (*base == NULL) {
        iter->phase = F_START;
      }
      else {
        if (iter->phase != F_DUPLI) {
          if (depsgraph && (*base)->object->transflag & OB_DUPLI) {
            /* Collections cannot be duplicated for meta-balls yet,
             * this enters eternal loop because of
             * makeDispListMBall getting called inside of collection_duplilist */
            if ((*base)->object->instance_collection == NULL) {
              iter->duplilist = object_duplilist(depsgraph, (*scene), (*base)->object);

              iter->dupob = iter->duplilist->first;

              if (!iter->dupob) {
                free_object_duplilist(iter->duplilist);
                iter->duplilist = NULL;
              }
              iter->dupli_refob = NULL;
            }
          }
        }
        /* handle dupli's */
        if (iter->dupob) {
          (*base)->flag_legacy |= OB_FROMDUPLI;
          *ob = iter->dupob->ob;
          iter->phase = F_DUPLI;

          if (iter->dupli_refob != *ob) {
            if (iter->dupli_refob) {
              /* Restore previous object's real matrix. */
              copy_m4_m4(iter->dupli_refob->obmat, iter->omat);
            }
            /* Backup new object's real matrix. */
            iter->dupli_refob = *ob;
            copy_m4_m4(iter->omat, iter->dupli_refob->obmat);
          }
          copy_m4_m4((*ob)->obmat, iter->dupob->mat);

          iter->dupob = iter->dupob->next;
        }
        else if (iter->phase == F_DUPLI) {
          iter->phase = F_SCENE;
          (*base)->flag_legacy &= ~OB_FROMDUPLI;

          if (iter->dupli_refob) {
            /* Restore last object's real matrix. */
            copy_m4_m4(iter->dupli_refob->obmat, iter->omat);
            iter->dupli_refob = NULL;
          }

          free_object_duplilist(iter->duplilist);
          iter->duplilist = NULL;
          run_again = true;
        }
      }
    }
  }

  return iter->phase;
}

bool BKE_scene_has_view_layer(const Scene *scene, const ViewLayer *layer)
{
  return BLI_findindex(&scene->view_layers, layer) != -1;
}

Scene *BKE_scene_find_from_collection(const Main *bmain, const Collection *collection)
{
  for (Scene *scene = bmain->scenes.first; scene; scene = scene->id.next) {
    LISTBASE_FOREACH (ViewLayer *, layer, &scene->view_layers) {
      if (BKE_view_layer_has_collection(layer, collection)) {
        return scene;
      }
    }
  }

  return NULL;
}

#ifdef DURIAN_CAMERA_SWITCH
Object *BKE_scene_camera_switch_find(Scene *scene)
{
  if (scene->r.mode & R_NO_CAMERA_SWITCH) {
    return NULL;
  }

  const int cfra = ((scene->r.images == scene->r.framapto) ?
                        scene->r.cfra :
                        (int)(scene->r.cfra *
                              ((float)scene->r.framapto / (float)scene->r.images)));
  int frame = -(MAXFRAME + 1);
  int min_frame = MAXFRAME + 1;
  Object *camera = NULL;
  Object *first_camera = NULL;

  LISTBASE_FOREACH (TimeMarker *, m, &scene->markers) {
    if (m->camera && (m->camera->restrictflag & OB_RESTRICT_RENDER) == 0) {
      if ((m->frame <= cfra) && (m->frame > frame)) {
        camera = m->camera;
        frame = m->frame;

        if (frame == cfra) {
          break;
        }
      }

      if (m->frame < min_frame) {
        first_camera = m->camera;
        min_frame = m->frame;
      }
    }
  }

  if (camera == NULL) {
    /* If there's no marker to the left of current frame,
     * use camera from left-most marker to solve all sort
     * of Schrodinger uncertainties.
     */
    return first_camera;
  }

  return camera;
}
#endif

bool BKE_scene_camera_switch_update(Scene *scene)
{
#ifdef DURIAN_CAMERA_SWITCH
  Object *camera = BKE_scene_camera_switch_find(scene);
  if (camera && (camera != scene->camera)) {
    scene->camera = camera;
    DEG_id_tag_update(&scene->id, ID_RECALC_COPY_ON_WRITE);
    return true;
  }
#else
  (void)scene;
#endif
  return false;
}

const char *BKE_scene_find_marker_name(const Scene *scene, int frame)
{
  const ListBase *markers = &scene->markers;
  const TimeMarker *m1, *m2;

  /* search through markers for match */
  for (m1 = markers->first, m2 = markers->last; m1 && m2; m1 = m1->next, m2 = m2->prev) {
    if (m1->frame == frame) {
      return m1->name;
    }

    if (m1 == m2) {
      break;
    }

    if (m2->frame == frame) {
      return m2->name;
    }
  }

  return NULL;
}

/* return the current marker for this frame,
 * we can have more than 1 marker per frame, this just returns the first :/ */
const char *BKE_scene_find_last_marker_name(const Scene *scene, int frame)
{
  const TimeMarker *marker, *best_marker = NULL;
  int best_frame = -MAXFRAME * 2;
  for (marker = scene->markers.first; marker; marker = marker->next) {
    if (marker->frame == frame) {
      return marker->name;
    }

    if (marker->frame > best_frame && marker->frame < frame) {
      best_marker = marker;
      best_frame = marker->frame;
    }
  }

  return best_marker ? best_marker->name : NULL;
}

int BKE_scene_frame_snap_by_seconds(Scene *scene, double interval_in_seconds, int cfra)
{
  const int fps = round_db_to_int(FPS * interval_in_seconds);
  const int second_prev = cfra - mod_i(cfra, fps);
  const int second_next = second_prev + fps;
  const int delta_prev = cfra - second_prev;
  const int delta_next = second_next - cfra;
  return (delta_prev < delta_next) ? second_prev : second_next;
}

void BKE_scene_remove_rigidbody_object(struct Main *bmain,
                                       Scene *scene,
                                       Object *ob,
                                       const bool free_us)
{
  /* remove rigid body constraint from world before removing object */
  if (ob->rigidbody_constraint) {
    BKE_rigidbody_remove_constraint(bmain, scene, ob, free_us);
  }
  /* remove rigid body object from world before removing object */
  if (ob->rigidbody_object) {
    BKE_rigidbody_remove_object(bmain, scene, ob, free_us);
  }
}

/* checks for cycle, returns 1 if it's all OK */
bool BKE_scene_validate_setscene(Main *bmain, Scene *sce)
{
  Scene *sce_iter;
  int a, totscene;

  if (sce->set == NULL) {
    return true;
  }
  totscene = BLI_listbase_count(&bmain->scenes);

  for (a = 0, sce_iter = sce; sce_iter->set; sce_iter = sce_iter->set, a++) {
    /* more iterations than scenes means we have a cycle */
    if (a > totscene) {
      /* the tested scene gets zero'ed, that's typically current scene */
      sce->set = NULL;
      return false;
    }
  }

  return true;
}

/**
 * This function is needed to cope with fractional frames, needed for motion blur & physics.
 */
float BKE_scene_frame_get(const Scene *scene)
{
  return BKE_scene_frame_to_ctime(scene, scene->r.cfra);
}

/* This function is used to obtain arbitrary fractional frames */
float BKE_scene_frame_to_ctime(const Scene *scene, const float frame)
{
  float ctime = frame;
  ctime += scene->r.subframe;
  ctime *= scene->r.framelen;

  return ctime;
}
/**
 * Sets the frame int/float components.
 */
void BKE_scene_frame_set(struct Scene *scene, double cfra)
{
  double intpart;
  scene->r.subframe = modf(cfra, &intpart);
  scene->r.cfra = (int)intpart;
}

/* -------------------------------------------------------------------- */
/** \name Scene Orientation Slots
 * \{ */

TransformOrientationSlot *BKE_scene_orientation_slot_get(Scene *scene, int slot_index)
{
  if ((scene->orientation_slots[slot_index].flag & SELECT) == 0) {
    slot_index = SCE_ORIENT_DEFAULT;
  }
  return &scene->orientation_slots[slot_index];
}

TransformOrientationSlot *BKE_scene_orientation_slot_get_from_flag(Scene *scene, int flag)
{
  BLI_assert(flag && !(flag & ~(V3D_GIZMO_SHOW_OBJECT_TRANSLATE | V3D_GIZMO_SHOW_OBJECT_ROTATE |
                                V3D_GIZMO_SHOW_OBJECT_SCALE)));
  int slot_index = SCE_ORIENT_DEFAULT;
  if (flag & V3D_GIZMO_SHOW_OBJECT_TRANSLATE) {
    slot_index = SCE_ORIENT_TRANSLATE;
  }
  else if (flag & V3D_GIZMO_SHOW_OBJECT_ROTATE) {
    slot_index = SCE_ORIENT_ROTATE;
  }
  else if (flag & V3D_GIZMO_SHOW_OBJECT_SCALE) {
    slot_index = SCE_ORIENT_SCALE;
  }
  return BKE_scene_orientation_slot_get(scene, slot_index);
}

/**
 * Activate a transform orientation in a 3D view based on an enum value.
 *
 * \param orientation: If this is #V3D_ORIENT_CUSTOM or greater, the custom transform orientation
 * with index \a orientation - #V3D_ORIENT_CUSTOM gets activated.
 */
void BKE_scene_orientation_slot_set_index(TransformOrientationSlot *orient_slot, int orientation)
{
  const bool is_custom = orientation >= V3D_ORIENT_CUSTOM;
  orient_slot->type = is_custom ? V3D_ORIENT_CUSTOM : orientation;
  orient_slot->index_custom = is_custom ? (orientation - V3D_ORIENT_CUSTOM) : -1;
}

int BKE_scene_orientation_slot_get_index(const TransformOrientationSlot *orient_slot)
{
  return (orient_slot->type == V3D_ORIENT_CUSTOM) ?
             (orient_slot->type + orient_slot->index_custom) :
             orient_slot->type;
}

int BKE_scene_orientation_get_index(Scene *scene, int slot_index)
{
  TransformOrientationSlot *orient_slot = BKE_scene_orientation_slot_get(scene, slot_index);
  return BKE_scene_orientation_slot_get_index(orient_slot);
}

int BKE_scene_orientation_get_index_from_flag(Scene *scene, int flag)
{
  TransformOrientationSlot *orient_slot = BKE_scene_orientation_slot_get_from_flag(scene, flag);
  return BKE_scene_orientation_slot_get_index(orient_slot);
}

/** \} */

static bool check_rendered_viewport_visible(Main *bmain)
{
  wmWindowManager *wm = bmain->wm.first;
  wmWindow *window;
  for (window = wm->windows.first; window != NULL; window = window->next) {
    const bScreen *screen = BKE_workspace_active_screen_get(window->workspace_hook);
    Scene *scene = window->scene;
    RenderEngineType *type = RE_engines_find(scene->r.engine);

    if (type->draw_engine || !type->render) {
      continue;
    }

    for (ScrArea *area = screen->areabase.first; area != NULL; area = area->next) {
      View3D *v3d = area->spacedata.first;
      if (area->spacetype != SPACE_VIEW3D) {
        continue;
      }
      if (v3d->shading.type == OB_RENDER) {
        return true;
      }
    }
  }
  return false;
}

/* TODO(campbell): shouldn't we be able to use 'DEG_get_view_layer' here?
 * Currently this is NULL on load, so don't. */
static void prepare_mesh_for_viewport_render(Main *bmain, const ViewLayer *view_layer)
{
  /* This is needed to prepare mesh to be used by the render
   * engine from the viewport rendering. We do loading here
   * so all the objects which shares the same mesh datablock
   * are nicely tagged for update and updated.
   *
   * This makes it so viewport render engine doesn't need to
   * call loading of the edit data for the mesh objects.
   */

  Object *obedit = OBEDIT_FROM_VIEW_LAYER(view_layer);
  if (obedit) {
    Mesh *mesh = obedit->data;
    if ((obedit->type == OB_MESH) &&
        ((obedit->id.recalc & ID_RECALC_ALL) || (mesh->id.recalc & ID_RECALC_ALL))) {
      if (check_rendered_viewport_visible(bmain)) {
        BMesh *bm = mesh->edit_mesh->bm;
        BM_mesh_bm_to_me(bmain,
                         bm,
                         mesh,
                         (&(struct BMeshToMeshParams){
                             .calc_object_remap = true,
                             .update_shapekey_indices = true,
                         }));
        DEG_id_tag_update(&mesh->id, 0);
      }
    }
  }
}

void BKE_scene_update_sound(Depsgraph *depsgraph, Main *bmain)
{
  Scene *scene = DEG_get_evaluated_scene(depsgraph);
  const int recalc = scene->id.recalc;
  BKE_sound_ensure_scene(scene);
  if (recalc & ID_RECALC_AUDIO_SEEK) {
    BKE_sound_seek_scene(bmain, scene);
  }
  if (recalc & ID_RECALC_AUDIO_FPS) {
    BKE_sound_update_fps(bmain, scene);
  }
  if (recalc & ID_RECALC_AUDIO_VOLUME) {
    BKE_sound_set_scene_volume(scene, scene->audio.volume);
  }
  if (recalc & ID_RECALC_AUDIO_MUTE) {
    const bool is_mute = (scene->audio.flag & AUDIO_MUTE);
    BKE_sound_mute_scene(scene, is_mute);
  }
  if (recalc & ID_RECALC_AUDIO_LISTENER) {
    BKE_sound_update_scene_listener(scene);
  }
  BKE_sound_update_scene(depsgraph, scene);
}

void BKE_scene_update_tag_audio_volume(Depsgraph *UNUSED(depsgraph), Scene *scene)
{
  BLI_assert(DEG_is_evaluated_id(&scene->id));
  /* The volume is actually updated in BKE_scene_update_sound(), from either
   * scene_graph_update_tagged() or from BKE_scene_graph_update_for_newframe(). */
  scene->id.recalc |= ID_RECALC_AUDIO_VOLUME;
}

/* TODO(sergey): This actually should become view_layer_graph or so.
 * Same applies to update_for_newframe.
 *
 * If only_if_tagged is truth then the function will do nothing if the dependency graph is up
 * to date already.
 */
static void scene_graph_update_tagged(Depsgraph *depsgraph, Main *bmain, bool only_if_tagged)
{
  if (only_if_tagged && DEG_is_fully_evaluated(depsgraph)) {
    return;
  }

  Scene *scene = DEG_get_input_scene(depsgraph);
  ViewLayer *view_layer = DEG_get_input_view_layer(depsgraph);
  bool used_multiple_passes = false;

  bool run_callbacks = DEG_id_type_any_updated(depsgraph);
  if (run_callbacks) {
    BKE_callback_exec_id(bmain, &scene->id, BKE_CB_EVT_DEPSGRAPH_UPDATE_PRE);
  }

  for (int pass = 0; pass < 2; pass++) {
    /* (Re-)build dependency graph if needed. */
    DEG_graph_relations_update(depsgraph);
    /* Uncomment this to check if graph was properly tagged for update. */
    // DEG_debug_graph_relations_validate(depsgraph, bmain, scene);
    /* Flush editing data if needed. */
    prepare_mesh_for_viewport_render(bmain, view_layer);
    /* Update all objects: drivers, matrices, displists, etc. flags set
     * by depsgraph or manual, no layer check here, gets correct flushed. */
    DEG_evaluate_on_refresh(depsgraph);
    /* Update sound system. */
    BKE_scene_update_sound(depsgraph, bmain);
    /* Notify python about depsgraph update. */
    if (run_callbacks) {
      BKE_callback_exec_id_depsgraph(
          bmain, &scene->id, depsgraph, BKE_CB_EVT_DEPSGRAPH_UPDATE_POST);

      /* It is possible that the custom callback modified scene and removed some IDs from the main
       * database. In this case DEG_editors_update() will crash because it iterates over all IDs
       * which depsgraph was built for.
       *
       * The solution is to update relations prior to this call, avoiding access to freed IDs.
       * Should be safe because relations update is supposed to preserve flags of all IDs which are
       * still a part of the dependency graph. If an ID is kicked out of the dependency graph it
       * should also be fine because when/if it's added to another dependency graph it will need to
       * be tagged for an update anyway.
       *
       * If there are no relations changed by the callback this call will do nothing. */
      DEG_graph_relations_update(depsgraph);
    }

    /* If user callback did not tag anything for update we can skip second iteration.
     * Otherwise we update scene once again, but without running callbacks to bring
     * scene to a fully evaluated state with user modifications taken into account. */
    if (DEG_is_fully_evaluated(depsgraph)) {
      break;
    }

    /* Clear recalc flags for second pass, but back them up for editors update. */
    const bool backup = true;
    DEG_ids_clear_recalc(depsgraph, backup);
    used_multiple_passes = true;
    run_callbacks = false;
  }

  /* Inform editors about changes, using recalc flags from both passes. */
  if (used_multiple_passes) {
    DEG_ids_restore_recalc(depsgraph);
  }
  const bool is_time_update = false;
  DEG_editors_update(depsgraph, is_time_update);

  const bool backup = false;
  DEG_ids_clear_recalc(depsgraph, backup);
}

void BKE_scene_graph_update_tagged(Depsgraph *depsgraph, Main *bmain)
{
  scene_graph_update_tagged(depsgraph, bmain, false);
}

void BKE_scene_graph_evaluated_ensure(Depsgraph *depsgraph, Main *bmain)
{
  scene_graph_update_tagged(depsgraph, bmain, true);
}

/* applies changes right away, does all sets too */
void BKE_scene_graph_update_for_newframe_ex(Depsgraph *depsgraph, const bool clear_recalc)
{
  Scene *scene = DEG_get_input_scene(depsgraph);
  Main *bmain = DEG_get_bmain(depsgraph);
  bool used_multiple_passes = false;

  /* Keep this first. */
  BKE_callback_exec_id(bmain, &scene->id, BKE_CB_EVT_FRAME_CHANGE_PRE);

  for (int pass = 0; pass < 2; pass++) {
    /* Update animated image textures for particles, modifiers, gpu, etc,
     * call this at the start so modifiers with textures don't lag 1 frame.
     */
    BKE_image_editors_update_frame(bmain, scene->r.cfra);
    BKE_sound_set_cfra(scene->r.cfra);
    DEG_graph_relations_update(depsgraph);
    /* Update all objects: drivers, matrices, displists, etc. flags set
     * by depgraph or manual, no layer check here, gets correct flushed.
     *
     * NOTE: Only update for new frame on first iteration. Second iteration is for ensuring user
     * edits from callback are properly taken into account. Doing a time update on those would
     * lose any possible unkeyed changes made by the handler. */
    if (pass == 0) {
      const float ctime = BKE_scene_frame_get(scene);
      DEG_evaluate_on_framechange(depsgraph, ctime);
    }
    else {
      DEG_evaluate_on_refresh(depsgraph);
    }
    /* Update sound system animation. */
    BKE_scene_update_sound(depsgraph, bmain);

    /* Notify editors and python about recalc. */
    if (pass == 0) {
      BKE_callback_exec_id_depsgraph(bmain, &scene->id, depsgraph, BKE_CB_EVT_FRAME_CHANGE_POST);

      /* NOTE: Similar to this case in scene_graph_update_tagged(). Need to ensure that
       * DEG_editors_update() doesn't access freed memory of possibly removed ID. */
      DEG_graph_relations_update(depsgraph);
    }

    /* If user callback did not tag anything for update we can skip second iteration.
     * Otherwise we update scene once again, but without running callbacks to bring
     * scene to a fully evaluated state with user modifications taken into account. */
    if (DEG_is_fully_evaluated(depsgraph)) {
      break;
    }

    /* Clear recalc flags for second pass, but back them up for editors update. */
    const bool backup = true;
    DEG_ids_clear_recalc(depsgraph, backup);
    used_multiple_passes = true;
  }

  /* Inform editors about changes, using recalc flags from both passes. */
  if (used_multiple_passes) {
    DEG_ids_restore_recalc(depsgraph);
  }

  const bool is_time_update = true;
  DEG_editors_update(depsgraph, is_time_update);

  /* Clear recalc flags, can be skipped for e.g. renderers that will read these
   * and clear the flags later. */
  if (clear_recalc) {
    const bool backup = false;
    DEG_ids_clear_recalc(depsgraph, backup);
  }
}

void BKE_scene_graph_update_for_newframe(Depsgraph *depsgraph)
{
  BKE_scene_graph_update_for_newframe_ex(depsgraph, true);
}

/**
 * Ensures given scene/view_layer pair has a valid, up-to-date depsgraph.
 *
 * \warning Sets matching depsgraph as active,
 * so should only be called from the active editing context (usually, from operators).
 */
void BKE_scene_view_layer_graph_evaluated_ensure(Main *bmain, Scene *scene, ViewLayer *view_layer)
{
  Depsgraph *depsgraph = BKE_scene_ensure_depsgraph(bmain, scene, view_layer);
  DEG_make_active(depsgraph);
  BKE_scene_graph_update_tagged(depsgraph, bmain);
}

/* return default view */
SceneRenderView *BKE_scene_add_render_view(Scene *sce, const char *name)
{
  SceneRenderView *srv;

  if (!name) {
    name = DATA_("RenderView");
  }

  srv = MEM_callocN(sizeof(SceneRenderView), "new render view");
  BLI_strncpy(srv->name, name, sizeof(srv->name));
  BLI_uniquename(&sce->r.views,
                 srv,
                 DATA_("RenderView"),
                 '.',
                 offsetof(SceneRenderView, name),
                 sizeof(srv->name));
  BLI_addtail(&sce->r.views, srv);

  return srv;
}

bool BKE_scene_remove_render_view(Scene *scene, SceneRenderView *srv)
{
  const int act = BLI_findindex(&scene->r.views, srv);

  if (act == -1) {
    return false;
  }
  if (scene->r.views.first == scene->r.views.last) {
    /* ensure 1 view is kept */
    return false;
  }

  BLI_remlink(&scene->r.views, srv);
  MEM_freeN(srv);

  scene->r.actview = 0;

  return true;
}

/* render simplification */

int get_render_subsurf_level(const RenderData *r, int lvl, bool for_render)
{
  if (r->mode & R_SIMPLIFY) {
    if (for_render) {
      return min_ii(r->simplify_subsurf_render, lvl);
    }

    return min_ii(r->simplify_subsurf, lvl);
  }

  return lvl;
}

int get_render_child_particle_number(const RenderData *r, int num, bool for_render)
{
  if (r->mode & R_SIMPLIFY) {
    if (for_render) {
      return (int)(r->simplify_particles_render * num);
    }

    return (int)(r->simplify_particles * num);
  }

  return num;
}

/**
 * Helper function for the SETLOOPER and SETLOOPER_VIEW_LAYER macros
 *
 * It iterates over the bases of the active layer and then the bases
 * of the active layer of the background (set) scenes recursively.
 */
Base *_setlooper_base_step(Scene **sce_iter, ViewLayer *view_layer, Base *base)
{
  if (base && base->next) {
    /* Common case, step to the next. */
    return base->next;
  }
  if ((base == NULL) && (view_layer != NULL)) {
    /* First time looping, return the scenes first base. */
    /* For the first loop we should get the layer from workspace when available. */
    if (view_layer->object_bases.first) {
      return (Base *)view_layer->object_bases.first;
    }
    /* No base on this scene layer. */
    goto next_set;
  }
  else {
  next_set:
    /* Reached the end, get the next base in the set. */
    while ((*sce_iter = (*sce_iter)->set)) {
      ViewLayer *view_layer_set = BKE_view_layer_default_render((*sce_iter));
      base = (Base *)view_layer_set->object_bases.first;

      if (base) {
        return base;
      }
    }
  }

  return NULL;
}

bool BKE_scene_use_shading_nodes_custom(Scene *scene)
{
  RenderEngineType *type = RE_engines_find(scene->r.engine);
  return (type && type->flag & RE_USE_SHADING_NODES_CUSTOM);
}

bool BKE_scene_use_spherical_stereo(Scene *scene)
{
  RenderEngineType *type = RE_engines_find(scene->r.engine);
  return (type && type->flag & RE_USE_SPHERICAL_STEREO);
}

bool BKE_scene_uses_blender_eevee(const Scene *scene)
{
  return STREQ(scene->r.engine, RE_engine_id_BLENDER_EEVEE);
}

bool BKE_scene_uses_blender_workbench(const Scene *scene)
{
  return STREQ(scene->r.engine, RE_engine_id_BLENDER_WORKBENCH);
}

bool BKE_scene_uses_cycles(const Scene *scene)
{
  return STREQ(scene->r.engine, RE_engine_id_CYCLES);
}

bool BKE_scene_uses_octane(const Scene *scene)
{
  return STREQ(scene->r.engine, RE_engine_id_OCTANE);
}

void BKE_scene_base_flag_to_objects(ViewLayer *view_layer)
{
  Base *base = view_layer->object_bases.first;

  while (base) {
    BKE_scene_object_base_flag_sync_from_base(base);
    base = base->next;
  }
}

/**
 * Synchronize object base flags
 *
 * This is usually handled by the depsgraph.
 * However, in rare occasions we need to use the latest object flags
 * before depsgraph is fully updated.
 *
 * It should (ideally) only run for copy-on-written objects since this is
 * runtime data generated per-viewlayer.
 */
void BKE_scene_object_base_flag_sync_from_base(Base *base)
{
  Object *ob = base->object;
  ob->base_flag = base->flag;
}

void BKE_scene_disable_color_management(Scene *scene)
{
  ColorManagedDisplaySettings *display_settings = &scene->display_settings;
  ColorManagedViewSettings *view_settings = &scene->view_settings;
  const char *view;
  const char *none_display_name;

  none_display_name = IMB_colormanagement_display_get_none_name();

  BLI_strncpy(display_settings->display_device,
              none_display_name,
              sizeof(display_settings->display_device));

  view = IMB_colormanagement_view_get_default_name(display_settings->display_device);

  if (view) {
    BLI_strncpy(view_settings->view_transform, view, sizeof(view_settings->view_transform));
  }
}

bool BKE_scene_check_color_management_enabled(const Scene *scene)
{
  return !STREQ(scene->display_settings.display_device, "None");
}

bool BKE_scene_check_rigidbody_active(const Scene *scene)
{
  return scene && scene->rigidbody_world && scene->rigidbody_world->group &&
         !(scene->rigidbody_world->flag & RBW_FLAG_MUTED);
}

int BKE_render_num_threads(const RenderData *rd)
{
  int threads;

  /* override set from command line? */
  threads = BLI_system_num_threads_override_get();

  if (threads > 0) {
    return threads;
  }

  /* fixed number of threads specified in scene? */
  if (rd->mode & R_FIXED_THREADS) {
    threads = rd->threads;
  }
  else {
    threads = BLI_system_thread_count();
  }

  return max_ii(threads, 1);
}

int BKE_scene_num_threads(const Scene *scene)
{
  return BKE_render_num_threads(&scene->r);
}

int BKE_render_preview_pixel_size(const RenderData *r)
{
  if (r->preview_pixel_size == 0) {
    return (U.pixelsize > 1.5f) ? 2 : 1;
  }
  return r->preview_pixel_size;
}

/**
 * Apply the needed correction factor to value, based on unit_type
 * (only length-related are affected currently) and unit->scale_length.
 */
double BKE_scene_unit_scale(const UnitSettings *unit, const int unit_type, double value)
{
  if (unit->system == USER_UNIT_NONE) {
    /* Never apply scale_length when not using a unit setting! */
    return value;
  }

  switch (unit_type) {
    case B_UNIT_LENGTH:
    case B_UNIT_VELOCITY:
    case B_UNIT_ACCELERATION:
      return value * (double)unit->scale_length;
    case B_UNIT_AREA:
    case B_UNIT_POWER:
      return value * pow(unit->scale_length, 2);
    case B_UNIT_VOLUME:
      return value * pow(unit->scale_length, 3);
    case B_UNIT_MASS:
      return value * pow(unit->scale_length, 3);
    case B_UNIT_CAMERA: /* *Do not* use scene's unit scale for camera focal lens! See T42026. */
    default:
      return value;
  }
}

/******************** multiview *************************/

int BKE_scene_multiview_num_views_get(const RenderData *rd)
{
  SceneRenderView *srv;
  int totviews = 0;

  if ((rd->scemode & R_MULTIVIEW) == 0) {
    return 1;
  }

  if (rd->views_format == SCE_VIEWS_FORMAT_STEREO_3D) {
    srv = BLI_findstring(&rd->views, STEREO_LEFT_NAME, offsetof(SceneRenderView, name));
    if ((srv && srv->viewflag & SCE_VIEW_DISABLE) == 0) {
      totviews++;
    }

    srv = BLI_findstring(&rd->views, STEREO_RIGHT_NAME, offsetof(SceneRenderView, name));
    if ((srv && srv->viewflag & SCE_VIEW_DISABLE) == 0) {
      totviews++;
    }
  }
  else {
    for (srv = rd->views.first; srv; srv = srv->next) {
      if ((srv->viewflag & SCE_VIEW_DISABLE) == 0) {
        totviews++;
      }
    }
  }
  return totviews;
}

bool BKE_scene_multiview_is_stereo3d(const RenderData *rd)
{
  SceneRenderView *srv[2];

  if ((rd->scemode & R_MULTIVIEW) == 0) {
    return false;
  }

  srv[0] = (SceneRenderView *)BLI_findstring(
      &rd->views, STEREO_LEFT_NAME, offsetof(SceneRenderView, name));
  srv[1] = (SceneRenderView *)BLI_findstring(
      &rd->views, STEREO_RIGHT_NAME, offsetof(SceneRenderView, name));

  return (srv[0] && ((srv[0]->viewflag & SCE_VIEW_DISABLE) == 0) && srv[1] &&
          ((srv[1]->viewflag & SCE_VIEW_DISABLE) == 0));
}

/* return whether to render this SceneRenderView */
bool BKE_scene_multiview_is_render_view_active(const RenderData *rd, const SceneRenderView *srv)
{
  if (srv == NULL) {
    return false;
  }

  if ((rd->scemode & R_MULTIVIEW) == 0) {
    return false;
  }

  if ((srv->viewflag & SCE_VIEW_DISABLE)) {
    return false;
  }

  if (rd->views_format == SCE_VIEWS_FORMAT_MULTIVIEW) {
    return true;
  }

  /* SCE_VIEWS_SETUP_BASIC */
  if (STR_ELEM(srv->name, STEREO_LEFT_NAME, STEREO_RIGHT_NAME)) {
    return true;
  }

  return false;
}

/* return true if viewname is the first or if the name is NULL or not found */
bool BKE_scene_multiview_is_render_view_first(const RenderData *rd, const char *viewname)
{
  SceneRenderView *srv;

  if ((rd->scemode & R_MULTIVIEW) == 0) {
    return true;
  }

  if ((!viewname) || (!viewname[0])) {
    return true;
  }

  for (srv = rd->views.first; srv; srv = srv->next) {
    if (BKE_scene_multiview_is_render_view_active(rd, srv)) {
      return STREQ(viewname, srv->name);
    }
  }

  return true;
}

/* return true if viewname is the last or if the name is NULL or not found */
bool BKE_scene_multiview_is_render_view_last(const RenderData *rd, const char *viewname)
{
  SceneRenderView *srv;

  if ((rd->scemode & R_MULTIVIEW) == 0) {
    return true;
  }

  if ((!viewname) || (!viewname[0])) {
    return true;
  }

  for (srv = rd->views.last; srv; srv = srv->prev) {
    if (BKE_scene_multiview_is_render_view_active(rd, srv)) {
      return STREQ(viewname, srv->name);
    }
  }

  return true;
}

SceneRenderView *BKE_scene_multiview_render_view_findindex(const RenderData *rd, const int view_id)
{
  SceneRenderView *srv;
  size_t nr;

  if ((rd->scemode & R_MULTIVIEW) == 0) {
    return NULL;
  }

  for (srv = rd->views.first, nr = 0; srv; srv = srv->next) {
    if (BKE_scene_multiview_is_render_view_active(rd, srv)) {
      if (nr++ == view_id) {
        return srv;
      }
    }
  }
  return srv;
}

const char *BKE_scene_multiview_render_view_name_get(const RenderData *rd, const int view_id)
{
  SceneRenderView *srv = BKE_scene_multiview_render_view_findindex(rd, view_id);

  if (srv) {
    return srv->name;
  }

  return "";
}

int BKE_scene_multiview_view_id_get(const RenderData *rd, const char *viewname)
{
  SceneRenderView *srv;
  size_t nr;

  if ((!rd) || ((rd->scemode & R_MULTIVIEW) == 0)) {
    return 0;
  }

  if ((!viewname) || (!viewname[0])) {
    return 0;
  }

  for (srv = rd->views.first, nr = 0; srv; srv = srv->next) {
    if (BKE_scene_multiview_is_render_view_active(rd, srv)) {
      if (STREQ(viewname, srv->name)) {
        return nr;
      }

      nr += 1;
    }
  }

  return 0;
}

void BKE_scene_multiview_filepath_get(SceneRenderView *srv, const char *filepath, char *r_filepath)
{
  BLI_strncpy(r_filepath, filepath, FILE_MAX);
  BLI_path_suffix(r_filepath, FILE_MAX, srv->suffix, "");
}

/**
 * When multiview is not used the filepath is as usual (e.g., ``Image.jpg``).
 * When multiview is on, even if only one view is enabled the view is incorporated
 * into the file name (e.g., ``Image_L.jpg``). That allows for the user to re-render
 * individual views.
 */
void BKE_scene_multiview_view_filepath_get(const RenderData *rd,
                                           const char *filepath,
                                           const char *viewname,
                                           char *r_filepath)
{
  SceneRenderView *srv;
  char suffix[FILE_MAX];

  srv = BLI_findstring(&rd->views, viewname, offsetof(SceneRenderView, name));
  if (srv) {
    BLI_strncpy(suffix, srv->suffix, sizeof(suffix));
  }
  else {
    BLI_strncpy(suffix, viewname, sizeof(suffix));
  }

  BLI_strncpy(r_filepath, filepath, FILE_MAX);
  BLI_path_suffix(r_filepath, FILE_MAX, suffix, "");
}

const char *BKE_scene_multiview_view_suffix_get(const RenderData *rd, const char *viewname)
{
  SceneRenderView *srv;

  if ((viewname == NULL) || (viewname[0] == '\0')) {
    return viewname;
  }

  srv = BLI_findstring(&rd->views, viewname, offsetof(SceneRenderView, name));
  if (srv) {
    return srv->suffix;
  }

  return viewname;
}

const char *BKE_scene_multiview_view_id_suffix_get(const RenderData *rd, const int view_id)
{
  if ((rd->scemode & R_MULTIVIEW) == 0) {
    return "";
  }

  const char *viewname = BKE_scene_multiview_render_view_name_get(rd, view_id);
  return BKE_scene_multiview_view_suffix_get(rd, viewname);
}

void BKE_scene_multiview_view_prefix_get(Scene *scene,
                                         const char *name,
                                         char *r_prefix,
                                         const char **r_ext)
{
  SceneRenderView *srv;
  size_t index_act;
  const char *suf_act;
  const char delims[] = {'.', '\0'};

  r_prefix[0] = '\0';

  /* begin of extension */
  index_act = BLI_str_rpartition(name, delims, r_ext, &suf_act);
  if (*r_ext == NULL) {
    return;
  }
  BLI_assert(index_act > 0);
  UNUSED_VARS_NDEBUG(index_act);

  for (srv = scene->r.views.first; srv; srv = srv->next) {
    if (BKE_scene_multiview_is_render_view_active(&scene->r, srv)) {
      const size_t len = strlen(srv->suffix);
      const size_t ext_len = strlen(*r_ext);
      if (ext_len >= len && STREQLEN(*r_ext - len, srv->suffix, len)) {
        BLI_strncpy(r_prefix, name, strlen(name) - ext_len - len + 1);
        break;
      }
    }
  }
}

void BKE_scene_multiview_videos_dimensions_get(const RenderData *rd,
                                               const size_t width,
                                               const size_t height,
                                               size_t *r_width,
                                               size_t *r_height)
{
  if ((rd->scemode & R_MULTIVIEW) && rd->im_format.views_format == R_IMF_VIEWS_STEREO_3D) {
    IMB_stereo3d_write_dimensions(rd->im_format.stereo3d_format.display_mode,
                                  (rd->im_format.stereo3d_format.flag & S3D_SQUEEZED_FRAME) != 0,
                                  width,
                                  height,
                                  r_width,
                                  r_height);
  }
  else {
    *r_width = width;
    *r_height = height;
  }
}

int BKE_scene_multiview_num_videos_get(const RenderData *rd)
{
  if (BKE_imtype_is_movie(rd->im_format.imtype) == false) {
    return 0;
  }

  if ((rd->scemode & R_MULTIVIEW) == 0) {
    return 1;
  }

  if (rd->im_format.views_format == R_IMF_VIEWS_STEREO_3D) {
    return 1;
  }

  /* R_IMF_VIEWS_INDIVIDUAL */
  return BKE_scene_multiview_num_views_get(rd);
}

/* Manipulation of depsgraph storage. */

/* This is a key which identifies depsgraph. */
typedef struct DepsgraphKey {
  const ViewLayer *view_layer;
  /* TODO(sergey): Need to include window somehow (same layer might be in a
   * different states in different windows).
   */
} DepsgraphKey;

static unsigned int depsgraph_key_hash(const void *key_v)
{
  const DepsgraphKey *key = key_v;
  unsigned int hash = BLI_ghashutil_ptrhash(key->view_layer);
  /* TODO(sergey): Include hash from other fields in the key. */
  return hash;
}

static bool depsgraph_key_compare(const void *key_a_v, const void *key_b_v)
{
  const DepsgraphKey *key_a = key_a_v;
  const DepsgraphKey *key_b = key_b_v;
  /* TODO(sergey): Compare rest of  */
  return !(key_a->view_layer == key_b->view_layer);
}

static void depsgraph_key_free(void *key_v)
{
  DepsgraphKey *key = key_v;
  MEM_freeN(key);
}

static void depsgraph_key_value_free(void *value)
{
  Depsgraph *depsgraph = value;
  DEG_graph_free(depsgraph);
}

void BKE_scene_allocate_depsgraph_hash(Scene *scene)
{
  scene->depsgraph_hash = BLI_ghash_new(
      depsgraph_key_hash, depsgraph_key_compare, "Scene Depsgraph Hash");
}

void BKE_scene_ensure_depsgraph_hash(Scene *scene)
{
  if (scene->depsgraph_hash == NULL) {
    BKE_scene_allocate_depsgraph_hash(scene);
  }
}

void BKE_scene_free_depsgraph_hash(Scene *scene)
{
  if (scene->depsgraph_hash == NULL) {
    return;
  }
  BLI_ghash_free(scene->depsgraph_hash, depsgraph_key_free, depsgraph_key_value_free);
  scene->depsgraph_hash = NULL;
}

void BKE_scene_free_view_layer_depsgraph(Scene *scene, ViewLayer *view_layer)
{
  if (scene->depsgraph_hash != NULL) {
    DepsgraphKey key = {view_layer};
    BLI_ghash_remove(scene->depsgraph_hash, &key, depsgraph_key_free, depsgraph_key_value_free);
  }
}

/* Query depsgraph for a specific contexts. */

static Depsgraph **scene_get_depsgraph_p(Scene *scene,
                                         ViewLayer *view_layer,
                                         const bool allocate_ghash_entry)
{
  /* bmain may be NULL here! */
  BLI_assert(scene != NULL);
  BLI_assert(view_layer != NULL);
  BLI_assert(BKE_scene_has_view_layer(scene, view_layer));

  /* Make sure hash itself exists. */
  if (allocate_ghash_entry) {
    BKE_scene_ensure_depsgraph_hash(scene);
  }
  if (scene->depsgraph_hash == NULL) {
    return NULL;
  }

  DepsgraphKey key;
  key.view_layer = view_layer;

  Depsgraph **depsgraph_ptr;
  if (!allocate_ghash_entry) {
    depsgraph_ptr = (Depsgraph **)BLI_ghash_lookup_p(scene->depsgraph_hash, &key);
    return depsgraph_ptr;
  }

  DepsgraphKey **key_ptr;
  if (BLI_ghash_ensure_p_ex(
          scene->depsgraph_hash, &key, (void ***)&key_ptr, (void ***)&depsgraph_ptr)) {
    return depsgraph_ptr;
  }

  /* Depsgraph was not found in the ghash, but the key still needs allocating. */
  *key_ptr = MEM_mallocN(sizeof(DepsgraphKey), __func__);
  **key_ptr = key;

  *depsgraph_ptr = NULL;
  return depsgraph_ptr;
}

static Depsgraph **scene_ensure_depsgraph_p(Main *bmain, Scene *scene, ViewLayer *view_layer)
{
  BLI_assert(bmain != NULL);

  Depsgraph **depsgraph_ptr = scene_get_depsgraph_p(scene, view_layer, true);
  if (depsgraph_ptr == NULL) {
    /* The scene has no depsgraph hash. */
    return NULL;
  }
  if (*depsgraph_ptr != NULL) {
    /* The depsgraph was found, no need to allocate. */
    return depsgraph_ptr;
  }

  /* Allocate a new depsgraph. scene_get_depsgraph_p() already ensured that the pointer is stored
   * in the scene's depsgraph hash. */
  *depsgraph_ptr = DEG_graph_new(bmain, scene, view_layer, DAG_EVAL_VIEWPORT);

  /* TODO(sergey): Would be cool to avoid string format print,
   * but is a bit tricky because we can't know in advance whether
   * we will ever enable debug messages for this depsgraph.
   */
  char name[1024];
  BLI_snprintf(name, sizeof(name), "%s :: %s", scene->id.name, view_layer->name);
  DEG_debug_name_set(*depsgraph_ptr, name);

  /* These viewport depsgraphs communicate changes to the editors. */
  DEG_enable_editors_update(*depsgraph_ptr);

  return depsgraph_ptr;
}

Depsgraph *BKE_scene_get_depsgraph(const Scene *scene, const ViewLayer *view_layer)
{
  BLI_assert(BKE_scene_has_view_layer(scene, view_layer));

  if (scene->depsgraph_hash == NULL) {
    return NULL;
  }

  DepsgraphKey key;
  key.view_layer = view_layer;
  return BLI_ghash_lookup(scene->depsgraph_hash, &key);
}

Depsgraph *BKE_scene_ensure_depsgraph(Main *bmain, Scene *scene, ViewLayer *view_layer)
{
  Depsgraph **depsgraph_ptr = scene_ensure_depsgraph_p(bmain, scene, view_layer);
  return (depsgraph_ptr != NULL) ? *depsgraph_ptr : NULL;
}

static char *scene_undo_depsgraph_gen_key(Scene *scene, ViewLayer *view_layer, char *key_full)
{
  if (key_full == NULL) {
    key_full = MEM_callocN(MAX_ID_NAME + FILE_MAX + MAX_NAME, __func__);
  }

  size_t key_full_offset = BLI_strncpy_rlen(key_full, scene->id.name, MAX_ID_NAME);
  if (scene->id.lib != NULL) {
    key_full_offset += BLI_strncpy_rlen(
        key_full + key_full_offset, scene->id.lib->filepath, FILE_MAX);
  }
  key_full_offset += BLI_strncpy_rlen(key_full + key_full_offset, view_layer->name, MAX_NAME);
  BLI_assert(key_full_offset < MAX_ID_NAME + FILE_MAX + MAX_NAME);

  return key_full;
}

GHash *BKE_scene_undo_depsgraphs_extract(Main *bmain)
{
  GHash *depsgraph_extract = BLI_ghash_new(
      BLI_ghashutil_strhash_p, BLI_ghashutil_strcmp, __func__);

  for (Scene *scene = bmain->scenes.first; scene != NULL; scene = scene->id.next) {
    if (scene->depsgraph_hash == NULL) {
      /* In some cases, e.g. when undo has to perform multiple steps at once, no depsgraph will
       * be built so this pointer may be NULL. */
      continue;
    }
    for (ViewLayer *view_layer = scene->view_layers.first; view_layer != NULL;
         view_layer = view_layer->next) {
      DepsgraphKey key;
      key.view_layer = view_layer;
      Depsgraph **depsgraph = (Depsgraph **)BLI_ghash_lookup_p(scene->depsgraph_hash, &key);

      if (depsgraph != NULL && *depsgraph != NULL) {
        char *key_full = scene_undo_depsgraph_gen_key(scene, view_layer, NULL);

        /* We steal the depsgraph from the scene. */
        BLI_ghash_insert(depsgraph_extract, key_full, *depsgraph);
        *depsgraph = NULL;
      }
    }
  }

  return depsgraph_extract;
}

void BKE_scene_undo_depsgraphs_restore(Main *bmain, GHash *depsgraph_extract)
{
  for (Scene *scene = bmain->scenes.first; scene != NULL; scene = scene->id.next) {
    for (ViewLayer *view_layer = scene->view_layers.first; view_layer != NULL;
         view_layer = view_layer->next) {
      char key_full[MAX_ID_NAME + FILE_MAX + MAX_NAME] = {0};
      scene_undo_depsgraph_gen_key(scene, view_layer, key_full);

      Depsgraph **depsgraph_extract_ptr = (Depsgraph **)BLI_ghash_lookup_p(depsgraph_extract,
                                                                           key_full);
      if (depsgraph_extract_ptr == NULL) {
        continue;
      }
      BLI_assert(*depsgraph_extract_ptr != NULL);

      Depsgraph **depsgraph_scene_ptr = scene_get_depsgraph_p(scene, view_layer, true);
      BLI_assert(depsgraph_scene_ptr != NULL);
      BLI_assert(*depsgraph_scene_ptr == NULL);

      /* We steal the depsgraph back from our 'extract' storage to the scene. */
      Depsgraph *depsgraph = *depsgraph_extract_ptr;

      DEG_graph_replace_owners(depsgraph, bmain, scene, view_layer);

      DEG_graph_tag_relations_update(depsgraph);

      *depsgraph_scene_ptr = depsgraph;
      *depsgraph_extract_ptr = NULL;
    }
  }

  BLI_ghash_free(depsgraph_extract, MEM_freeN, depsgraph_key_value_free);
}

/* -------------------------------------------------------------------- */
/** \name Scene Orientation
 * \{ */

void BKE_scene_transform_orientation_remove(Scene *scene, TransformOrientation *orientation)
{
  const int orientation_index = BKE_scene_transform_orientation_get_index(scene, orientation);

  for (int i = 0; i < ARRAY_SIZE(scene->orientation_slots); i++) {
    TransformOrientationSlot *orient_slot = &scene->orientation_slots[i];
    if (orient_slot->index_custom == orientation_index) {
      /* could also use orientation_index-- */
      orient_slot->type = V3D_ORIENT_GLOBAL;
      orient_slot->index_custom = -1;
    }
    else if (orient_slot->index_custom > orientation_index) {
      BLI_assert(orient_slot->type == V3D_ORIENT_CUSTOM);
      orient_slot->index_custom--;
    }
  }

  BLI_freelinkN(&scene->transform_spaces, orientation);
}

TransformOrientation *BKE_scene_transform_orientation_find(const Scene *scene, const int index)
{
  return BLI_findlink(&scene->transform_spaces, index);
}

/**
 * \return the index that \a orientation has within \a scene's transform-orientation list
 * or -1 if not found.
 */
int BKE_scene_transform_orientation_get_index(const Scene *scene,
                                              const TransformOrientation *orientation)
{
  return BLI_findindex(&scene->transform_spaces, orientation);
}

/** \} */

/* -------------------------------------------------------------------- */
/** \name Scene Cursor Rotation
 *
 * Matches #BKE_object_rot_to_mat3 and #BKE_object_mat3_to_rot.
 * \{ */

void BKE_scene_cursor_rot_to_mat3(const View3DCursor *cursor, float mat[3][3])
{
  if (cursor->rotation_mode > 0) {
    eulO_to_mat3(mat, cursor->rotation_euler, cursor->rotation_mode);
  }
  else if (cursor->rotation_mode == ROT_MODE_AXISANGLE) {
    axis_angle_to_mat3(mat, cursor->rotation_axis, cursor->rotation_angle);
  }
  else {
    float tquat[4];
    normalize_qt_qt(tquat, cursor->rotation_quaternion);
    quat_to_mat3(mat, tquat);
  }
}

void BKE_scene_cursor_rot_to_quat(const View3DCursor *cursor, float quat[4])
{
  if (cursor->rotation_mode > 0) {
    eulO_to_quat(quat, cursor->rotation_euler, cursor->rotation_mode);
  }
  else if (cursor->rotation_mode == ROT_MODE_AXISANGLE) {
    axis_angle_to_quat(quat, cursor->rotation_axis, cursor->rotation_angle);
  }
  else {
    normalize_qt_qt(quat, cursor->rotation_quaternion);
  }
}

void BKE_scene_cursor_mat3_to_rot(View3DCursor *cursor, const float mat[3][3], bool use_compat)
{
  BLI_ASSERT_UNIT_M3(mat);

  switch (cursor->rotation_mode) {
    case ROT_MODE_QUAT: {
      float quat[4];
      mat3_normalized_to_quat(quat, mat);
      if (use_compat) {
        float quat_orig[4];
        copy_v4_v4(quat_orig, cursor->rotation_quaternion);
        quat_to_compatible_quat(cursor->rotation_quaternion, quat, quat_orig);
      }
      else {
        copy_v4_v4(cursor->rotation_quaternion, quat);
      }
      break;
    }
    case ROT_MODE_AXISANGLE: {
      mat3_to_axis_angle(cursor->rotation_axis, &cursor->rotation_angle, mat);
      break;
    }
    default: {
      if (use_compat) {
        mat3_to_compatible_eulO(
            cursor->rotation_euler, cursor->rotation_euler, cursor->rotation_mode, mat);
      }
      else {
        mat3_to_eulO(cursor->rotation_euler, cursor->rotation_mode, mat);
      }
      break;
    }
  }
}

void BKE_scene_cursor_quat_to_rot(View3DCursor *cursor, const float quat[4], bool use_compat)
{
  BLI_ASSERT_UNIT_QUAT(quat);

  switch (cursor->rotation_mode) {
    case ROT_MODE_QUAT: {
      if (use_compat) {
        float quat_orig[4];
        copy_v4_v4(quat_orig, cursor->rotation_quaternion);
        quat_to_compatible_quat(cursor->rotation_quaternion, quat, quat_orig);
      }
      else {
        copy_qt_qt(cursor->rotation_quaternion, quat);
      }
      break;
    }
    case ROT_MODE_AXISANGLE: {
      quat_to_axis_angle(cursor->rotation_axis, &cursor->rotation_angle, quat);
      break;
    }
    default: {
      if (use_compat) {
        quat_to_compatible_eulO(
            cursor->rotation_euler, cursor->rotation_euler, cursor->rotation_mode, quat);
      }
      else {
        quat_to_eulO(cursor->rotation_euler, cursor->rotation_mode, quat);
      }
      break;
    }
  }
}

void BKE_scene_cursor_to_mat4(const View3DCursor *cursor, float mat[4][4])
{
  float mat3[3][3];
  BKE_scene_cursor_rot_to_mat3(cursor, mat3);
  copy_m4_m3(mat, mat3);
  copy_v3_v3(mat[3], cursor->location);
}

void BKE_scene_cursor_from_mat4(View3DCursor *cursor, const float mat[4][4], bool use_compat)
{
  float mat3[3][3];
  copy_m3_m4(mat3, mat);
  BKE_scene_cursor_mat3_to_rot(cursor, mat3, use_compat);
  copy_v3_v3(cursor->location, mat[3]);
}

/** \} */

/* Dependency graph evaluation. */

static void scene_sequencer_disable_sound_strips(Scene *scene)
{
  if (scene->sound_scene == NULL) {
    return;
  }
  Sequence *seq;
  SEQ_ALL_BEGIN (scene->ed, seq) {
    if (seq->scene_sound != NULL) {
      BKE_sound_remove_scene_sound(scene, seq->scene_sound);
      seq->scene_sound = NULL;
    }
  }
  SEQ_ALL_END;
}

void BKE_scene_eval_sequencer_sequences(Depsgraph *depsgraph, Scene *scene)
{
  DEG_debug_print_eval(depsgraph, __func__, scene->id.name, scene);
  if (scene->ed == NULL) {
    return;
  }
  BKE_sound_ensure_scene(scene);
  Sequence *seq;
  SEQ_ALL_BEGIN (scene->ed, seq) {
    if (seq->scene_sound == NULL) {
      if (seq->sound != NULL) {
        if (seq->scene_sound == NULL) {
          seq->scene_sound = BKE_sound_add_scene_sound_defaults(scene, seq);
        }
      }
      else if (seq->type == SEQ_TYPE_SCENE) {
        if (seq->scene != NULL) {
          BKE_sound_ensure_scene(seq->scene);
          seq->scene_sound = BKE_sound_scene_add_scene_sound_defaults(scene, seq);
        }
      }
    }
    if (seq->scene_sound != NULL) {
      /* Make sure changing volume via sequence's properties panel works correct.
       *
       * Ideally, the entire BKE_scene_update_sound() will happen from a dependency graph, so
       * then it is no longer needed to do such manual forced updates. */
      if (seq->type == SEQ_TYPE_SCENE && seq->scene != NULL) {
        BKE_sound_set_scene_volume(seq->scene, seq->scene->audio.volume);
        if ((seq->flag & SEQ_SCENE_STRIPS) == 0) {
          scene_sequencer_disable_sound_strips(seq->scene);
        }
      }
      if (seq->sound != NULL) {
        if (scene->id.recalc & ID_RECALC_AUDIO || seq->sound->id.recalc & ID_RECALC_AUDIO) {
          BKE_sound_update_scene_sound(seq->scene_sound, seq->sound);
        }
      }
      BKE_sound_set_scene_sound_volume(
          seq->scene_sound, seq->volume, (seq->flag & SEQ_AUDIO_VOLUME_ANIMATED) != 0);
      BKE_sound_set_scene_sound_pitch(
          seq->scene_sound, seq->pitch, (seq->flag & SEQ_AUDIO_PITCH_ANIMATED) != 0);
      BKE_sound_set_scene_sound_pan(
          seq->scene_sound, seq->pan, (seq->flag & SEQ_AUDIO_PAN_ANIMATED) != 0);
    }
  }
  SEQ_ALL_END;
  SEQ_edit_update_muting(scene->ed);
  SEQ_sound_update_bounds_all(scene);
}
