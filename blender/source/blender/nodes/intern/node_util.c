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

#include <ctype.h>
#include <limits.h>
#include <string.h>

#include "DNA_node_types.h"

#include "BLI_listbase.h"
#include "BLI_string.h"
#include "BLI_utildefines.h"

#include "BLT_translation.h"

#include "BKE_colortools.h"
#include "BKE_node.h"

#include "RNA_access.h"
#include "RNA_enum_types.h"

#include "MEM_guardedalloc.h"

#include "node_util.h"

/* -------------------------------------------------------------------- */
/** \name Storage Data
 * \{ */

void node_free_curves(bNode *node)
{
  BKE_curvemapping_free(node->storage);
}

void node_free_standard_storage(bNode *node)
{
  if (node->storage) {
    MEM_freeN(node->storage);
  }
}

void node_copy_curves(bNodeTree *UNUSED(dest_ntree), bNode *dest_node, const bNode *src_node)
{
  dest_node->storage = BKE_curvemapping_copy(src_node->storage);
}

void node_copy_standard_storage(bNodeTree *UNUSED(dest_ntree),
                                bNode *dest_node,
                                const bNode *src_node)
{
  dest_node->storage = MEM_dupallocN(src_node->storage);
}

void *node_initexec_curves(bNodeExecContext *UNUSED(context),
                           bNode *node,
                           bNodeInstanceKey UNUSED(key))
{
  BKE_curvemapping_init(node->storage);
  return NULL; /* unused return */
}

/** \} */

/* -------------------------------------------------------------------- */
/** \name Updates
 * \{ */

void node_sock_label(bNodeSocket *sock, const char *name)
{
  BLI_strncpy(sock->label, name, MAX_NAME);
}

void node_sock_label_clear(bNodeSocket *sock)
{
  if (sock->label[0] != '\0') {
    sock->label[0] = '\0';
  }
}

void node_math_update(bNodeTree *UNUSED(ntree), bNode *node)
{
  bNodeSocket *sock1 = BLI_findlink(&node->inputs, 0);
  bNodeSocket *sock2 = BLI_findlink(&node->inputs, 1);
  bNodeSocket *sock3 = BLI_findlink(&node->inputs, 2);
  nodeSetSocketAvailability(sock2,
                            !ELEM(node->custom1,
                                  NODE_MATH_SQRT,
                                  NODE_MATH_SIGN,
                                  NODE_MATH_CEIL,
                                  NODE_MATH_SINE,
                                  NODE_MATH_ROUND,
                                  NODE_MATH_FLOOR,
                                  NODE_MATH_COSINE,
                                  NODE_MATH_ARCSINE,
                                  NODE_MATH_TANGENT,
                                  NODE_MATH_ABSOLUTE,
                                  NODE_MATH_RADIANS,
                                  NODE_MATH_DEGREES,
                                  NODE_MATH_FRACTION,
                                  NODE_MATH_ARCCOSINE,
                                  NODE_MATH_ARCTANGENT) &&
                                !ELEM(node->custom1,
                                      NODE_MATH_INV_SQRT,
                                      NODE_MATH_TRUNC,
                                      NODE_MATH_EXPONENT,
                                      NODE_MATH_COSH,
                                      NODE_MATH_SINH,
                                      NODE_MATH_TANH));
  nodeSetSocketAvailability(sock3,
                            ELEM(node->custom1,
                                 NODE_MATH_COMPARE,
                                 NODE_MATH_MULTIPLY_ADD,
                                 NODE_MATH_WRAP,
                                 NODE_MATH_SMOOTH_MIN,
                                 NODE_MATH_SMOOTH_MAX));

  node_sock_label_clear(sock1);
  node_sock_label_clear(sock2);
  node_sock_label_clear(sock3);

  switch (node->custom1) {
    case NODE_MATH_WRAP:
      node_sock_label(sock2, "Max");
      node_sock_label(sock3, "Min");
      break;
    case NODE_MATH_MULTIPLY_ADD:
      node_sock_label(sock2, "Multiplier");
      node_sock_label(sock3, "Addend");
      break;
    case NODE_MATH_LESS_THAN:
    case NODE_MATH_GREATER_THAN:
      node_sock_label(sock2, "Threshold");
      break;
    case NODE_MATH_PINGPONG:
      node_sock_label(sock2, "Scale");
      break;
    case NODE_MATH_SNAP:
      node_sock_label(sock2, "Increment");
      break;
    case NODE_MATH_POWER:
      node_sock_label(sock1, "Base");
      node_sock_label(sock2, "Exponent");
      break;
    case NODE_MATH_LOGARITHM:
      node_sock_label(sock2, "Base");
      break;
    case NODE_MATH_DEGREES:
      node_sock_label(sock1, "Radians");
      break;
    case NODE_MATH_RADIANS:
      node_sock_label(sock1, "Degrees");
      break;
    case NODE_MATH_COMPARE:
      node_sock_label(sock3, "Epsilon");
      break;
    case NODE_MATH_SMOOTH_MAX:
    case NODE_MATH_SMOOTH_MIN:
      node_sock_label(sock3, "Distance");
      break;
  }
}

/** \} */

/* -------------------------------------------------------------------- */
/** \name Labels
 * \{ */

void node_blend_label(bNodeTree *UNUSED(ntree), bNode *node, char *label, int maxlen)
{
  const char *name;
  bool enum_label = RNA_enum_name(rna_enum_ramp_blend_items, node->custom1, &name);
  if (!enum_label) {
    name = "Unknown";
  }
  BLI_strncpy(label, IFACE_(name), maxlen);
}

void node_image_label(bNodeTree *UNUSED(ntree), bNode *node, char *label, int maxlen)
{
  /* If there is no loaded image, return an empty string,
   * and let nodeLabel() fill in the proper type translation. */
  BLI_strncpy(label, (node->id) ? node->id->name + 2 : "", maxlen);
}

void node_math_label(bNodeTree *UNUSED(ntree), bNode *node, char *label, int maxlen)
{
  const char *name;
  bool enum_label = RNA_enum_name(rna_enum_node_math_items, node->custom1, &name);
  if (!enum_label) {
    name = "Unknown";
  }
  BLI_strncpy(label, IFACE_(name), maxlen);
}

void node_vector_math_label(bNodeTree *UNUSED(ntree), bNode *node, char *label, int maxlen)
{
  const char *name;
  bool enum_label = RNA_enum_name(rna_enum_node_vec_math_items, node->custom1, &name);
  if (!enum_label) {
    name = "Unknown";
  }
  BLI_strncpy(label, IFACE_(name), maxlen);
}

void node_filter_label(bNodeTree *UNUSED(ntree), bNode *node, char *label, int maxlen)
{
  const char *name;
  bool enum_label = RNA_enum_name(rna_enum_node_filter_items, node->custom1, &name);
  if (!enum_label) {
    name = "Unknown";
  }
  BLI_strncpy(label, IFACE_(name), maxlen);
}

/** \} */

/* -------------------------------------------------------------------- */
/** \name Link Insertion
 * \{ */

static bool node_link_socket_match(const bNodeSocket *a, const bNodeSocket *b)
{
  /* Check if sockets are of the same type. */
  if (a->typeinfo != b->typeinfo) {
    return false;
  }

  /* Test if alphabetic prefix matches, allowing for imperfect matches, such as numeric suffixes
   * like Color1/Color2. */
  int prefix_len = 0;
  const char *ca = a->name, *cb = b->name;
  for (; *ca != '\0' && *cb != '\0'; ca++, cb++) {
    /* End of common prefix? */
    if (*ca != *cb) {
      /* Prefix delimited by non-alphabetic char. */
      if (isalpha(*ca) || isalpha(*cb)) {
        return false;
      }
      break;
    }
    prefix_len++;
  }
  return prefix_len > 0;
}

static int node_count_links(const bNodeTree *ntree, const bNodeSocket *socket)
{
  int count = 0;
  LISTBASE_FOREACH (bNodeLink *, link, &ntree->links) {
    if (ELEM(socket, link->fromsock, link->tosock)) {
      count++;
    }
  }
  return count;
}

static bNodeSocket *node_find_linkable_socket(bNodeTree *ntree,
                                              bNode *node,
                                              bNodeSocket *to_socket)
{
  bNodeSocket *first = to_socket->in_out == SOCK_IN ? node->inputs.first : node->outputs.first;

  /* Wrap around the list end. */
  bNodeSocket *socket_iter = to_socket->next ? to_socket->next : first;
  while (socket_iter != to_socket) {
    if (!nodeSocketIsHidden(socket_iter) && node_link_socket_match(socket_iter, to_socket)) {
      const int link_count = node_count_links(ntree, socket_iter);
      /* Add one to account for the new link being added. */
      if (link_count + 1 <= nodeSocketLinkLimit(socket_iter)) {
        return socket_iter; /* Found a valid free socket we can swap to. */
      }
    }
    socket_iter = socket_iter->next ? socket_iter->next : first; /* Wrap around the list end. */
  }

  return NULL;
}

/**
 * The idea behind this is: When a user connects an input to a socket that is
 * already linked (and if its not an Multi Input Socket), we try to find a replacement socket for
 * the link that we try to overwrite and connect that previous link to the new socket.
 */
void node_insert_link_default(bNodeTree *ntree, bNode *node, bNodeLink *link)
{
  bNodeSocket *socket = link->tosock;

  if (node != link->tonode) {
    return;
  }

  /* If we're not at the link limit of the target socket, we can skip
   * trying to move existing links to another socket. */
  const int to_link_limit = nodeSocketLinkLimit(socket);
  if (socket->total_inputs + 1 < to_link_limit) {
    return;
  }

  LISTBASE_FOREACH_MUTABLE (bNodeLink *, to_link, &ntree->links) {
    if (socket == to_link->tosock) {
      bNodeSocket *new_socket = node_find_linkable_socket(ntree, node, socket);
      if (new_socket && new_socket != socket) {
        /* Attempt to redirect the existing link to the new socket. */
        to_link->tosock = new_socket;
        return;
      }

      if (new_socket == NULL) {
        /* No possible replacement, remove the existing link. */
        nodeRemLink(ntree, to_link);
        return;
      }
    }
  }
}

/** \} */

/* -------------------------------------------------------------------- */
/** \name Internal Links (mute and disconnect)
 * \{ */

/**
 * Common datatype priorities, works for compositor, shader and texture nodes alike
 * defines priority of datatype connection based on output type (to):
 * `<  0`: never connect these types.
 * `>= 0`: priority of connection (higher values chosen first).
 */
static int node_datatype_priority(eNodeSocketDatatype from, eNodeSocketDatatype to)
{
  switch (to) {
    case SOCK_RGBA:
      switch (from) {
        case SOCK_RGBA:
          return 4;
        case SOCK_FLOAT:
          return 3;
        case SOCK_INT:
          return 2;
        case SOCK_BOOLEAN:
          return 1;
        default:
          return -1;
      }
    case SOCK_VECTOR:
      switch (from) {
        case SOCK_VECTOR:
          return 4;
        case SOCK_FLOAT:
          return 3;
        case SOCK_INT:
          return 2;
        case SOCK_BOOLEAN:
          return 1;
        default:
          return -1;
      }
    case SOCK_FLOAT:
      switch (from) {
        case SOCK_FLOAT:
          return 5;
        case SOCK_INT:
          return 4;
        case SOCK_BOOLEAN:
          return 3;
        case SOCK_RGBA:
          return 2;
        case SOCK_VECTOR:
          return 1;
        default:
          return -1;
      }
    case SOCK_INT:
      switch (from) {
        case SOCK_INT:
          return 5;
        case SOCK_FLOAT:
          return 4;
        case SOCK_BOOLEAN:
          return 3;
        case SOCK_RGBA:
          return 2;
        case SOCK_VECTOR:
          return 1;
        default:
          return -1;
      }
    case SOCK_BOOLEAN:
      switch (from) {
        case SOCK_BOOLEAN:
          return 5;
        case SOCK_INT:
          return 4;
        case SOCK_FLOAT:
          return 3;
        case SOCK_RGBA:
          return 2;
        case SOCK_VECTOR:
          return 1;
        default:
          return -1;
      }
    case SOCK_SHADER:
      switch (from) {
        case SOCK_SHADER:
          return 1;
        default:
          return -1;
      }
    case SOCK_STRING:
      switch (from) {
        case SOCK_STRING:
          return 1;
        default:
          return -1;
      }
    case SOCK_OBJECT: {
      switch (from) {
        case SOCK_OBJECT:
          return 1;
        default:
          return -1;
      }
    }
    case SOCK_GEOMETRY: {
      switch (from) {
        case SOCK_GEOMETRY:
          return 1;
        default:
          return -1;
      }
    }
    case SOCK_COLLECTION: {
      switch (from) {
        case SOCK_COLLECTION:
          return 1;
        default:
          return -1;
      }
    }
    default:
      return -1;
  }
}

/* select a suitable input socket for an output */
static bNodeSocket *select_internal_link_input(bNode *node, bNodeSocket *output)
{
  bNodeSocket *selected = NULL, *input;
  int i;
  int sel_priority = -1;
  bool sel_is_linked = false;

  for (input = node->inputs.first, i = 0; input; input = input->next, i++) {
    int priority = node_datatype_priority(input->type, output->type);
    bool is_linked = (input->link != NULL);
    bool preferred;

    if (nodeSocketIsHidden(input) || /* ignore hidden sockets */
        input->flag &
            SOCK_NO_INTERNAL_LINK || /* ignore if input is not allowed for internal connections */
        priority < 0 ||              /* ignore incompatible types */
        priority < sel_priority)     /* ignore if we already found a higher priority input */
    {
      continue;
    }

    /* determine if this input is preferred over the currently selected */
    preferred = (priority > sel_priority) ||   /* prefer higher datatype priority */
                (is_linked && !sel_is_linked); /* prefer linked over unlinked */

    if (preferred) {
      selected = input;
      sel_is_linked = is_linked;
      sel_priority = priority;
    }
  }

  return selected;
}

void node_update_internal_links_default(bNodeTree *ntree, bNode *node)
{
  bNodeLink *link;
  bNodeSocket *output, *input;

  /* sanity check */
  if (!ntree) {
    return;
  }

  /* use link pointer as a tag for handled sockets (for outputs is unused anyway) */
  for (output = node->outputs.first; output; output = output->next) {
    output->link = NULL;
  }

  for (link = ntree->links.first; link; link = link->next) {
    if (nodeLinkIsHidden(link)) {
      continue;
    }

    output = link->fromsock;
    if (link->fromnode != node || output->link) {
      continue;
    }
    if (nodeSocketIsHidden(output) || output->flag & SOCK_NO_INTERNAL_LINK) {
      continue;
    }
    output->link = link; /* not really used, just for tagging handled sockets */

    /* look for suitable input */
    input = select_internal_link_input(node, output);

    if (input) {
      bNodeLink *ilink = MEM_callocN(sizeof(bNodeLink), "internal node link");
      ilink->fromnode = node;
      ilink->fromsock = input;
      ilink->tonode = node;
      ilink->tosock = output;
      /* internal link is always valid */
      ilink->flag |= NODE_LINK_VALID;
      BLI_addtail(&node->internal_links, ilink);
    }
  }

  /* clean up */
  for (output = node->outputs.first; output; output = output->next) {
    output->link = NULL;
  }
}

/** \} */

/* -------------------------------------------------------------------- */
/** \name Default value RNA access
 * \{ */

float node_socket_get_float(bNodeTree *ntree, bNode *UNUSED(node), bNodeSocket *sock)
{
  PointerRNA ptr;
  RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock, &ptr);
  return RNA_float_get(&ptr, "default_value");
}

void node_socket_set_float(bNodeTree *ntree, bNode *UNUSED(node), bNodeSocket *sock, float value)
{
  PointerRNA ptr;
  RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock, &ptr);
  RNA_float_set(&ptr, "default_value", value);
}

void node_socket_get_color(bNodeTree *ntree, bNode *UNUSED(node), bNodeSocket *sock, float *value)
{
  PointerRNA ptr;
  RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock, &ptr);
  RNA_float_get_array(&ptr, "default_value", value);
}

void node_socket_set_color(bNodeTree *ntree,
                           bNode *UNUSED(node),
                           bNodeSocket *sock,
                           const float *value)
{
  PointerRNA ptr;
  RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock, &ptr);
  RNA_float_set_array(&ptr, "default_value", value);
}

void node_socket_get_vector(bNodeTree *ntree, bNode *UNUSED(node), bNodeSocket *sock, float *value)
{
  PointerRNA ptr;
  RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock, &ptr);
  RNA_float_get_array(&ptr, "default_value", value);
}

void node_socket_set_vector(bNodeTree *ntree,
                            bNode *UNUSED(node),
                            bNodeSocket *sock,
                            const float *value)
{
  PointerRNA ptr;
  RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock, &ptr);
  RNA_float_set_array(&ptr, "default_value", value);
}

/** \} */

void node_octane_projection_conversion_verify(bNodeTree *ntree, bNode *node, struct ID *id)
{
  bNodeSocket *sock;
  for (sock = node->inputs.first; sock; sock = sock->next) {
    if (STREQ(sock->name, "Coordinate Space")) {
      PointerRNA ptr;
      RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock, &ptr);
      int mode = RNA_int_get(&ptr, "default_value");
      if (mode >= 0 && mode < 255 && node->custom1 == 0) {
        switch (RNA_int_get(&ptr, "default_value")) {
          case 0:
            node->custom1 = OCT_POSITION_GLOBAL;
            break;
          case 1:
            node->custom1 = OCT_POSITION_OBJECT;
            break;
          case 2:
            node->custom1 = OCT_POSITION_NORMAL;
            break;
          default:
            node->custom1 = OCT_POSITION_OBJECT;
        }
        RNA_int_set(&ptr, "default_value", 255);
      }
    }
  }
  if (node->custom1 == 0) {
    node->custom1 = OCT_POSITION_OBJECT;
  }
}

void node_octane_projection_conversion_update(bNodeTree *ntree, bNode *node)
{
  node_octane_projection_conversion_verify(ntree, node, (ID *)ntree);
}

void node_octane_image_texture_conversion_verify(bNodeTree *ntree, bNode *node, struct ID *id)
{
  bNodeSocket *sock;
  for (sock = node->inputs.first; sock; sock = sock->next) {
    if (STREQ(sock->name, "Border mode")) {
      PointerRNA ptr;
      RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock, &ptr);
      int mode = RNA_int_get(&ptr, "default_value");
      if (mode >= 0 && mode < 255) {
        switch (mode) {
          case 0:
            node->custom2 = OCT_BORDER_MODE_WRAP;
            break;
          case 1:
            node->custom2 = OCT_BORDER_MODE_BLACK;
            break;
          case 2:
            node->custom2 = OCT_BORDER_MODE_WHITE;
            break;
          case 3:
            node->custom2 = OCT_BORDER_MODE_CLAMP;
            break;
          case 4:
            node->custom2 = OCT_BORDER_MODE_MIRROR;
            break;
          default:
            node->custom2 = OCT_BORDER_MODE_WRAP;
        }
        RNA_int_set(&ptr, "default_value", 255);
      }
    }
  }
  if (node->custom1 == 0) {
    node->custom1 = OCT_HDR_BIT_DEPTH_16;
  }
  if (node->oct_custom1 == 0) {
    node->oct_custom1 = IES_MAX_1;
  }
}

void node_octane_image_texture_conversion_update(bNodeTree *ntree, bNode *node)
{
  node_octane_image_texture_conversion_verify(ntree, node, (ID *)ntree);
}

void node_octane_image_tile_conversion_verify(bNodeTree *ntree, bNode *node, struct ID *id)
{
  if (node->custom1 == 0) {
    node->custom1 = OCT_HDR_BIT_DEPTH_16;
  }
}

void node_octane_image_tile_conversion_update(bNodeTree *ntree, bNode *node)
{
  node_octane_image_tile_conversion_verify(ntree, node, (ID *)ntree);
}

void node_octane_transform_conversion_verify(bNodeTree *ntree, bNode *node, struct ID *id)
{
  bNodeSocket *sock;
  for (sock = node->inputs.first; sock; sock = sock->next) {
    if (STREQ(sock->name, "Rotation order")) {
      PointerRNA ptr;
      RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock, &ptr);
      int mode = RNA_int_get(&ptr, "default_value");
      if (mode >= 0 && mode < 255) {
        switch (mode) {
          case 0:
            node->custom1 = OCT_ROT_XYZ;
            break;
          case 1:
            node->custom1 = OCT_ROT_XZY;
            break;
          case 2:
            node->custom1 = OCT_ROT_YXZ;
            break;
          case 3:
            node->custom1 = OCT_ROT_YZX;
            break;
          case 4:
            node->custom1 = OCT_ROT_ZXY;
            break;
          case 5:
            node->custom1 = OCT_ROT_ZYX;
            break;
          default:
            node->custom1 = OCT_ROT_YXZ;
        }
        RNA_int_set(&ptr, "default_value", 255);
      }
    }
  }
}

void node_octane_transform_conversion_update(bNodeTree *ntree, bNode *node)
{
  node_octane_transform_conversion_verify(ntree, node, (ID *)ntree);
}

void node_octane_noise_tex_conversion_verify(bNodeTree *ntree, bNode *node, struct ID *id)
{
  bNodeSocket *sock;
  for (sock = node->inputs.first; sock; sock = sock->next) {
    if (STREQ(sock->name, "Noise type")) {
      PointerRNA ptr;
      RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock, &ptr);
      int mode = RNA_int_get(&ptr, "default_value");
      if (mode >= 0 && mode < 255) {
        switch (mode) {
          case 0:
            node->custom1 = OCT_NOISE_TYPE_PERLIN;
            break;
          case 1:
            node->custom1 = OCT_NOISE_TYPE_TURBULENCE;
            break;
          case 2:
            node->custom1 = OCT_NOISE_TYPE_CIRCULAR;
            break;
          case 3:
            node->custom1 = OCT_NOISE_TYPE_CHIPS;
            break;
          default:
            node->custom1 = OCT_NOISE_TYPE_PERLIN;
        }
        RNA_int_set(&ptr, "default_value", 255);
      }
    }
  }
}

void node_octane_noise_tex_conversion_update(bNodeTree *ntree, bNode *node)
{
  node_octane_noise_tex_conversion_verify(ntree, node, (ID *)ntree);
}

void node_octane_falloff_tex_conversion_verify(bNodeTree *ntree, bNode *node, struct ID *id)
{
  bNodeSocket *sock;
  for (sock = node->inputs.first; sock; sock = sock->next) {
    if (STREQ(sock->name, "Mode")) {
      PointerRNA ptr;
      RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock, &ptr);
      int mode = RNA_int_get(&ptr, "default_value");
      if (mode >= 0 && mode < 255) {
        switch (mode) {
          case 0:
            node->custom1 = OCT_FALLOFF_NORMAL_VS_EYE_RAY;
            break;
          case 1:
            node->custom1 = OCT_FALLOFF_NORMAL_VS_VECTOR_90DEG;
            break;
          case 2:
            node->custom1 = OCT_FALLOFF_NORMAL_VS_VECTOR_180DEG;
            break;
          default:
            node->custom1 = OCT_FALLOFF_NORMAL_VS_EYE_RAY;
        }
        RNA_int_set(&ptr, "default_value", 255);
      }
    }
  }
}

void node_octane_falloff_tex_conversion_update(bNodeTree *ntree, bNode *node)
{
  node_octane_falloff_tex_conversion_verify(ntree, node, (ID *)ntree);
}

void node_octane_displacement_tex_conversion_verify(bNodeTree *ntree, bNode *node, struct ID *id)
{
  bNodeSocket *sock;
  for (sock = node->inputs.first; sock; sock = sock->next) {
    if (STREQ(sock->name, "Level of details")) {
      PointerRNA ptr;
      RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock, &ptr);
      int mode = RNA_int_get(&ptr, "default_value");
      if (mode >= 0 && mode < 255) {
        switch (mode) {
          case 8:
            node->custom1 = OCT_DISPLACEMENT_LEVEL_256;
            break;
          case 9:
            node->custom1 = OCT_DISPLACEMENT_LEVEL_512;
            break;
          case 10:
            node->custom1 = OCT_DISPLACEMENT_LEVEL_1024;
            break;
          case 11:
            node->custom1 = OCT_DISPLACEMENT_LEVEL_2048;
            break;
          case 12:
            node->custom1 = OCT_DISPLACEMENT_LEVEL_4096;
            break;
          case 13:
            node->custom1 = OCT_DISPLACEMENT_LEVEL_8192;
            break;
          default:
            node->custom1 = OCT_DISPLACEMENT_LEVEL_1024;
        }
        RNA_int_set(&ptr, "default_value", 255);
      }
    }
    else if (STREQ(sock->name, "Displacement direction")) {
      PointerRNA ptr;
      RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock, &ptr);
      int mode = RNA_int_get(&ptr, "default_value");
      if (mode >= 0 && mode < 255) {
        switch (mode) {
          case 1:
            node->custom2 = OCT_DISPLACEMENT_VERTEX_NORMAL;
            break;
          case 2:
            node->custom2 = OCT_DISPLACEMENT_GEOMETRIC_NORMAL;
            break;
          case 3:
            node->custom2 = OCT_DISPLACEMENT_SMOOTH_NORMAL;
            break;
          default:
            node->custom2 = OCT_DISPLACEMENT_VERTEX_NORMAL;
        }
        RNA_int_set(&ptr, "default_value", 255);
      }
    }
    else if (STREQ(sock->name, "Filter type")) {
      PointerRNA ptr;
      RNA_pointer_create((ID *)ntree, &RNA_NodeSocket, sock, &ptr);
      int mode = RNA_int_get(&ptr, "default_value");
      if (mode >= 0 && mode < 255) {
        switch (mode) {
          case 0:
            node->oct_custom1 = OCT_FILTER_TYPE_NONE;
            break;
          case 1:
            node->oct_custom1 = OCT_FILTER_TYPE_BOX;
            break;
          case 2:
            node->oct_custom1 = OCT_FILTER_TYPE_GAUSSIAN;
            break;
          default:
            node->oct_custom1 = OCT_FILTER_TYPE_NONE;
        }
        RNA_int_set(&ptr, "default_value", 255);
      }
    }
  }
}

void node_octane_displacement_tex_conversion_update(bNodeTree *ntree, bNode *node)
{
  node_octane_displacement_tex_conversion_verify(ntree, node, (ID *)ntree);
}

void node_octane_medium_init(bNodeTree *ntree, bNode *node)
{
  // Use "Lock mode" as default
  node->oct_custom1 = 1;
} 

void node_octane_medium_update(bNodeTree *ntree, bNode *node)
{
  bNodeSocket *sock;
  bool is_lock_step_length_pins = node->oct_custom1;
  for (sock = node->inputs.first; sock; sock = sock->next) {
    if (STREQ(sock->name, "Vol. shadow ray step length")) {
      if (!is_lock_step_length_pins) {
        sock->flag &= ~SOCK_UNAVAIL;
      }
      else {
        sock->flag |= SOCK_UNAVAIL;
      }
    }
  }
}

void node_octane_avo_settings_init(bNodeTree *ntree, bNode *node)
{
  node->oct_custom_aov = INVALID_CUSTOM_AOV;
  node->oct_custom_aov_channel = CUSTOM_AOV_CHANNEL_ALL;
}
