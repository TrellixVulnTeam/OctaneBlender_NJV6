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
 */

/** \file
 * \ingroup modifiers
 */

#include <string.h>

#include "BLI_string.h"
#include "BLI_utildefines.h"

#include "BLT_translation.h"

#include "DNA_cachefile_types.h"
#include "DNA_defaults.h"
#include "DNA_mesh_types.h"
#include "DNA_meshdata_types.h"
#include "DNA_modifier_types.h"
#include "DNA_object_types.h"
#include "DNA_scene_types.h"
#include "DNA_screen_types.h"

#include "MEM_guardedalloc.h"

#include "BKE_cachefile.h"
#include "BKE_context.h"
#include "BKE_lib_query.h"
#include "BKE_scene.h"
#include "BKE_screen.h"

#include "UI_interface.h"
#include "UI_resources.h"

#include "RNA_access.h"

#include "BLO_read_write.h"

#include "DEG_depsgraph_build.h"
#include "DEG_depsgraph_query.h"

#include "MOD_modifiertypes.h"
#include "MOD_ui_common.h"

#ifdef WITH_ALEMBIC
#  include "ABC_alembic.h"
#  include "BKE_global.h"
#  include "BKE_lib_id.h"
#endif

static void initData(ModifierData *md)
{
  MeshSeqCacheModifierData *mcmd = (MeshSeqCacheModifierData *)md;

  BLI_assert(MEMCMP_STRUCT_AFTER_IS_ZERO(mcmd, modifier));

  MEMCPY_STRUCT_AFTER(mcmd, DNA_struct_default_get(MeshSeqCacheModifierData), modifier);
}

static void copyData(const ModifierData *md, ModifierData *target, const int flag)
{
#if 0
  const MeshSeqCacheModifierData *mcmd = (const MeshSeqCacheModifierData *)md;
#endif
  MeshSeqCacheModifierData *tmcmd = (MeshSeqCacheModifierData *)target;

  BKE_modifier_copydata_generic(md, target, flag);

  tmcmd->reader = NULL;
  tmcmd->reader_object_path[0] = '\0';
}

static void freeData(ModifierData *md)
{
  MeshSeqCacheModifierData *mcmd = (MeshSeqCacheModifierData *)md;

  if (mcmd->reader) {
    mcmd->reader_object_path[0] = '\0';
    BKE_cachefile_reader_free(mcmd->cache_file, &mcmd->reader);
  }

  if (mcmd->vertex_velocities) {
    MEM_freeN(mcmd->vertex_velocities);
  }
}

static bool isDisabled(const struct Scene *UNUSED(scene),
                       ModifierData *md,
                       bool UNUSED(useRenderParams))
{
  MeshSeqCacheModifierData *mcmd = (MeshSeqCacheModifierData *)md;

  /* leave it up to the modifier to check the file is valid on calculation */
  return (mcmd->cache_file == NULL) || (mcmd->object_path[0] == '\0');
}

static Mesh *modifyMesh(ModifierData *md, const ModifierEvalContext *ctx, Mesh *mesh)
{
#ifdef WITH_ALEMBIC
  MeshSeqCacheModifierData *mcmd = (MeshSeqCacheModifierData *)md;

  /* Only used to check whether we are operating on org data or not... */
  Mesh *me = (ctx->object->type == OB_MESH) ? ctx->object->data : NULL;
  Mesh *org_mesh = mesh;

  Scene *scene = DEG_get_evaluated_scene(ctx->depsgraph);
  CacheFile *cache_file = mcmd->cache_file;
  const float frame = DEG_get_ctime(ctx->depsgraph);
  const float time = BKE_cachefile_time_offset(cache_file, frame, FPS);
  const char *err_str = NULL;

  if (!mcmd->reader || !STREQ(mcmd->reader_object_path, mcmd->object_path)) {
    STRNCPY(mcmd->reader_object_path, mcmd->object_path);
    BKE_cachefile_reader_open(cache_file, &mcmd->reader, ctx->object, mcmd->object_path);
    if (!mcmd->reader) {
      BKE_modifier_set_error(
          ctx->object, md, "Could not create Alembic reader for file %s", cache_file->filepath);
      return mesh;
    }
  }

  /* If this invocation is for the ORCO mesh, and the mesh in Alembic hasn't changed topology, we
   * must return the mesh as-is instead of deforming it. */
  if (ctx->flag & MOD_APPLY_ORCO &&
      !ABC_mesh_topology_changed(mcmd->reader, ctx->object, mesh, time, &err_str)) {
    return mesh;
  }

  if (me != NULL) {
    MVert *mvert = mesh->mvert;
    MEdge *medge = mesh->medge;
    MPoly *mpoly = mesh->mpoly;

    /* TODO(sybren+bastien): possibly check relevant custom data layers (UV/color depending on
     * flags) and duplicate those too. */
    if ((me->mvert == mvert) || (me->medge == medge) || (me->mpoly == mpoly)) {
      /* We need to duplicate data here, otherwise we'll modify org mesh, see T51701. */
      mesh = (Mesh *)BKE_id_copy_ex(NULL,
                                    &mesh->id,
                                    NULL,
                                    LIB_ID_CREATE_NO_MAIN | LIB_ID_CREATE_NO_USER_REFCOUNT |
                                        LIB_ID_CREATE_NO_DEG_TAG | LIB_ID_COPY_NO_PREVIEW);
    }
  }

  Mesh *result = ABC_read_mesh(mcmd->reader, ctx->object, mesh, time, &err_str, mcmd->read_flag);
  if (result) {
    result->oct_sphere_randomized_radius_seed = org_mesh->oct_sphere_randomized_radius_seed;
    result->oct_sphere_radius = org_mesh->oct_sphere_radius;
    result->oct_randomized_radius_min = org_mesh->oct_randomized_radius_min;
    result->oct_randomized_radius_max = org_mesh->oct_randomized_radius_max;
    result->oct_enable_octane_sphere_attribute = org_mesh->oct_enable_octane_sphere_attribute;
    result->oct_hide_original_mesh = org_mesh->oct_hide_original_mesh;
    result->oct_use_randomized_radius = org_mesh->oct_use_randomized_radius;
  }

  mcmd->velocity_delta = 1.0f;
  if (mcmd->cache_file->velocity_unit == CACHEFILE_VELOCITY_UNIT_SECOND) {
    mcmd->velocity_delta /= FPS;
  }

  mcmd->last_lookup_time = time;

  if (result != NULL) {
    mcmd->num_vertices = result->totvert;
  }

  if (err_str) {
    BKE_modifier_set_error(ctx->object, md, "%s", err_str);
  }

  if (!ELEM(result, NULL, mesh) && (mesh != org_mesh)) {
    BKE_id_free(NULL, mesh);
    mesh = org_mesh;
  }

  return result ? result : mesh;
#else
  UNUSED_VARS(ctx, md);
  return mesh;
#endif
}

static bool dependsOnTime(ModifierData *md)
{
#ifdef WITH_ALEMBIC
  MeshSeqCacheModifierData *mcmd = (MeshSeqCacheModifierData *)md;
  return (mcmd->cache_file != NULL);
#else
  UNUSED_VARS(md);
  return false;
#endif
}

static void foreachIDLink(ModifierData *md, Object *ob, IDWalkFunc walk, void *userData)
{
  MeshSeqCacheModifierData *mcmd = (MeshSeqCacheModifierData *)md;

  walk(userData, ob, (ID **)&mcmd->cache_file, IDWALK_CB_USER);
}

static void updateDepsgraph(ModifierData *md, const ModifierUpdateDepsgraphContext *ctx)
{
  MeshSeqCacheModifierData *mcmd = (MeshSeqCacheModifierData *)md;

  if (mcmd->cache_file != NULL) {
    DEG_add_object_cache_relation(
        ctx->node, mcmd->cache_file, DEG_OB_COMP_CACHE, "Mesh Cache File");
  }
}

static void panel_draw(const bContext *C, Panel *panel)
{
  uiLayout *layout = panel->layout;

  PointerRNA ob_ptr;
  PointerRNA *ptr = modifier_panel_get_property_pointers(panel, &ob_ptr);

  PointerRNA cache_file_ptr = RNA_pointer_get(ptr, "cache_file");
  bool has_cache_file = !RNA_pointer_is_null(&cache_file_ptr);

  uiLayoutSetPropSep(layout, true);

  uiTemplateCacheFile(layout, C, ptr, "cache_file");

  if (has_cache_file) {
    uiItemPointerR(layout, ptr, "object_path", &cache_file_ptr, "object_paths", NULL, ICON_NONE);
  }

  if (RNA_enum_get(&ob_ptr, "type") == OB_MESH) {
    uiItemR(layout, ptr, "read_data", UI_ITEM_R_EXPAND, NULL, ICON_NONE);
    uiItemR(layout, ptr, "use_vertex_interpolation", 0, NULL, ICON_NONE);
  }

  uiItemR(layout, ptr, "velocity_scale", 0, NULL, ICON_NONE);

  modifier_panel_end(layout, ptr);
}

static void panelRegister(ARegionType *region_type)
{
  modifier_panel_register(region_type, eModifierType_MeshSequenceCache, panel_draw);
}

static void blendRead(BlendDataReader *UNUSED(reader), ModifierData *md)
{
  MeshSeqCacheModifierData *msmcd = (MeshSeqCacheModifierData *)md;
  msmcd->reader = NULL;
  msmcd->reader_object_path[0] = '\0';
}

ModifierTypeInfo modifierType_MeshSequenceCache = {
    /* name */ "MeshSequenceCache",
    /* structName */ "MeshSeqCacheModifierData",
    /* structSize */ sizeof(MeshSeqCacheModifierData),
    /* srna */ &RNA_MeshSequenceCacheModifier,
    /* type */ eModifierTypeType_Constructive,
    /* flags */ eModifierTypeFlag_AcceptsMesh | eModifierTypeFlag_AcceptsCVs,
    /* icon */ ICON_MOD_MESHDEFORM, /* TODO: Use correct icon. */

    /* copyData */ copyData,

    /* deformVerts */ NULL,
    /* deformMatrices */ NULL,
    /* deformVertsEM */ NULL,
    /* deformMatricesEM */ NULL,
    /* modifyMesh */ modifyMesh,
    /* modifyHair */ NULL,
    /* modifyGeometrySet */ NULL,
    /* modifyVolume */ NULL,

    /* initData */ initData,
    /* requiredDataMask */ NULL,
    /* freeData */ freeData,
    /* isDisabled */ isDisabled,
    /* updateDepsgraph */ updateDepsgraph,
    /* dependsOnTime */ dependsOnTime,
    /* dependsOnNormals */ NULL,
    /* foreachIDLink */ foreachIDLink,
    /* foreachTexLink */ NULL,
    /* freeRuntimeData */ NULL,
    /* panelRegister */ panelRegister,
    /* blendWrite */ NULL,
    /* blendRead */ blendRead,
};
