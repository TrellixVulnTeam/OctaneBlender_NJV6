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
 * The Original Code is Copyright (C) 2007 Blender Foundation.
 * All rights reserved.
 */

/** \file
 * \ingroup nodes
 */

#pragma once

#include "DNA_listBase.h"

#include "BLI_utildefines.h"

#include "BKE_node.h"

#include "MEM_guardedalloc.h"

#include "NOD_socket.h"

#include "GPU_material.h" /* For Shader muting GPU code... */

#include "RNA_access.h"

#ifdef __cplusplus
extern "C" {
#endif

struct bNode;
struct bNodeTree;

/* data for initializing node execution */
typedef struct bNodeExecContext {
  struct bNodeInstanceHash *previews;
} bNodeExecContext;

typedef struct bNodeExecData {
  void *data;                   /* custom data storage */
  struct bNodePreview *preview; /* optional preview image */
} bNodeExecData;

/**** Storage Data ****/

extern void node_free_curves(struct bNode *node);
extern void node_free_standard_storage(struct bNode *node);

extern void node_copy_curves(struct bNodeTree *dest_ntree,
                             struct bNode *dest_node,
                             const struct bNode *src_node);
extern void node_copy_standard_storage(struct bNodeTree *dest_ntree,
                                       struct bNode *dest_node,
                                       const struct bNode *src_node);
extern void *node_initexec_curves(struct bNodeExecContext *context,
                                  struct bNode *node,
                                  bNodeInstanceKey key);

/**** Updates ****/
void node_sock_label(struct bNodeSocket *sock, const char *name);
void node_sock_label_clear(struct bNodeSocket *sock);
void node_math_update(struct bNodeTree *ntree, struct bNode *node);

/**** Labels ****/
void node_blend_label(struct bNodeTree *ntree, struct bNode *node, char *label, int maxlen);
void node_image_label(struct bNodeTree *ntree, struct bNode *node, char *label, int maxlen);
void node_math_label(struct bNodeTree *ntree, struct bNode *node, char *label, int maxlen);
void node_vector_math_label(struct bNodeTree *ntree, struct bNode *node, char *label, int maxlen);
void node_filter_label(struct bNodeTree *ntree, struct bNode *node, char *label, int maxlen);

/*** Link Handling */
void node_insert_link_default(struct bNodeTree *ntree, struct bNode *node, struct bNodeLink *link);
void node_update_internal_links_default(struct bNodeTree *ntree, struct bNode *node);

float node_socket_get_float(struct bNodeTree *ntree, struct bNode *node, struct bNodeSocket *sock);
void node_socket_set_float(struct bNodeTree *ntree,
                           struct bNode *node,
                           struct bNodeSocket *sock,
                           float value);
void node_socket_get_color(struct bNodeTree *ntree,
                           struct bNode *node,
                           struct bNodeSocket *sock,
                           float *value);
void node_socket_set_color(struct bNodeTree *ntree,
                           struct bNode *node,
                           struct bNodeSocket *sock,
                           const float *value);
void node_socket_get_vector(struct bNodeTree *ntree,
                            struct bNode *node,
                            struct bNodeSocket *sock,
                            float *value);
void node_socket_set_vector(struct bNodeTree *ntree,
                            struct bNode *node,
                            struct bNodeSocket *sock,
                            const float *value);

void node_octane_projection_conversion_update(bNodeTree *ntree, bNode *node);
void node_octane_projection_conversion_verify(bNodeTree *ntree, bNode *node, struct ID *id);
void node_octane_image_texture_conversion_update(bNodeTree *ntree, bNode *node);
void node_octane_image_texture_conversion_verify(bNodeTree *ntree, bNode *node, struct ID *id);
void node_octane_image_tile_conversion_update(bNodeTree *ntree, bNode *node);
void node_octane_image_tile_conversion_verify(bNodeTree *ntree, bNode *node, struct ID *id);
void node_octane_transform_conversion_update(bNodeTree *ntree, bNode *node);
void node_octane_transform_conversion_verify(bNodeTree *ntree, bNode *node, struct ID *id);
void node_octane_noise_tex_conversion_update(bNodeTree *ntree, bNode *node);
void node_octane_noise_tex_conversion_verify(bNodeTree *ntree, bNode *node, struct ID *id);
void node_octane_falloff_tex_conversion_update(bNodeTree *ntree, bNode *node);
void node_octane_falloff_tex_conversion_verify(bNodeTree *ntree, bNode *node, struct ID *id);
void node_octane_displacement_tex_conversion_update(bNodeTree *ntree, bNode *node);
void node_octane_displacement_tex_conversion_verify(bNodeTree *ntree, bNode *node, struct ID *id);
void node_octane_medium_init(bNodeTree *ntree, bNode *node);
void node_octane_medium_update(bNodeTree *ntree, bNode *node);
void node_octane_avo_settings_init(bNodeTree *ntree, bNode *node);

#ifdef __cplusplus
}
#endif
