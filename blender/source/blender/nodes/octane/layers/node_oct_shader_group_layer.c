/*
 * ***** BEGIN GPL LICENSE BLOCK *****
 *
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
 * The Original Code is Copyright (C) 2005 Blender Foundation.
 * All rights reserved.
 *
 * The Original Code is: all of this file.
 *
 * Contributor(s): none yet.
 *
 * ***** END GPL LICENSE BLOCK *****
 */

#include "../../../../source/blender/nodes/shader/node_shader_util.h"

static bNodeSocketTemplate sh_node_in[] = {{SOCK_SHADER,
                                            N_("Layer 1"),
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            1.0f,
                                            PROP_NONE,
                                            SOCK_NO_INTERNAL_LINK},
                                           {SOCK_SHADER,
                                            N_("Layer 2"),
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            1.0f,
                                            PROP_NONE,
                                            SOCK_NO_INTERNAL_LINK},
                                           {SOCK_SHADER,
                                            N_("Layer 3"),
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            1.0f,
                                            PROP_NONE,
                                            SOCK_NO_INTERNAL_LINK},
                                           {SOCK_SHADER,
                                            N_("Layer 4"),
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            1.0f,
                                            PROP_NONE,
                                            SOCK_NO_INTERNAL_LINK},
                                           {SOCK_SHADER,
                                            N_("Layer 5"),
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            1.0f,
                                            PROP_NONE,
                                            SOCK_NO_INTERNAL_LINK},
                                           {SOCK_SHADER,
                                            N_("Layer 6"),
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            1.0f,
                                            PROP_NONE,
                                            SOCK_NO_INTERNAL_LINK},
                                           {SOCK_SHADER,
                                            N_("Layer 7"),
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            1.0f,
                                            PROP_NONE,
                                            SOCK_NO_INTERNAL_LINK},
                                           {SOCK_SHADER,
                                            N_("Layer 8"),
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            0.0f,
                                            1.0f,
                                            PROP_NONE,
                                            SOCK_NO_INTERNAL_LINK},
                                           {-1, ""}};

static bNodeSocketTemplate sh_node_out[] = {
    {SOCK_SHADER, N_("OutMatLayer")},
    {SOCK_SHADER,
     N_("OutMat"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_HIDDEN | SOCK_UNAVAIL | SOCK_AUTO_HIDDEN__DEPRECATED},
    {-1, ""}};

static void node_oct_init_group_layer(bNodeTree *ntree, bNode *node)
{
  node->custom1 = 1;
}

static void node_shader_update_group_layer(bNodeTree *UNUSED(ntree), bNode *node)
{
  bNodeSocket *sock;
  int layer_number = node->custom1;
  for (int i = 1; i <= 8; ++i) {
    bool show = i <= layer_number;
    char sock_name[64];
    sprintf(sock_name, "Layer %d", i);
    for (sock = node->inputs.first; sock; sock = sock->next) {
      if (STREQ(sock->name, sock_name)) {
        if (show) {
          sock->flag &= ~SOCK_UNAVAIL;
        }
        else {
          sock->flag |= SOCK_UNAVAIL;
        }
      }
    }
  }
}

void register_node_type_sh_oct_group_layer(void)
{
  static bNodeType ntype;

  if (ntype.type != SH_NODE_OCT_GROUP_LAYER)
    node_type_base(
        &ntype, SH_NODE_OCT_GROUP_LAYER, "Octane Layer Group", NODE_CLASS_OCT_LAYER, NODE_OPTIONS);
  node_type_socket_templates(&ntype, sh_node_in, sh_node_out);
  node_type_size(&ntype, 160, 160, 500);
  node_type_init(&ntype, node_oct_init_group_layer);
  node_type_storage(&ntype, "", NULL, NULL);
  node_type_update(&ntype, node_shader_update_group_layer);

  nodeRegisterType(&ntype);
} /* register_node_type_sh_oct_group_layer() */
