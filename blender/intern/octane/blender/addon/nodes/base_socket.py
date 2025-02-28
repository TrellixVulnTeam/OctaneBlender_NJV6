import bpy
import re
import math
from bpy.props import IntProperty, BoolProperty, StringProperty, EnumProperty, PointerProperty
from bpy.utils import register_class, unregister_class
from bpy.app.translations import contexts as i18n_contexts
from bl_operators.node import NodeAddOperator
from ..utils import consts, utility
from ..utils.consts import SocketType, PinType


class OctaneBaseSocket(bpy.types.NodeSocket):
    """Base class for Octane sockets"""
    DYNAMIC_PIN_ID_OFFSET=10000

    bl_label=""
    bl_idname=""
    bl_socket_idname=""
    color=consts.OctanePinColor.Default    
    octane_default_node_type=""
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=0
    octane_deprecated=False
    octane_pin_id: IntProperty(name="Octane Pin ID", default=consts.P_UNKNOWN)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=PinType.PT_UNKNOWN)
    octane_socket_type: IntProperty(name="Socket Type", default=SocketType.ST_UNKNOWN)
    octane_input_enum_items: EnumProperty(items=utility.node_input_enum_items_callback, update=utility.node_input_enum_update_callback, default=consts.LINK_UTILITY_DEFAULT_INDEX)

    def init(self, **kwargs):
        # Fix the "default_value" display issue under "template_node_view"
        if self.octane_hide_value:
            self.hide_value = self.octane_hide_value
        if self.octane_deprecated:
            self.enabled = False

    def draw_prop(self, context, layout, text):
        if (hasattr(self, "default_value")):
            if self.is_linked:
                layout.label(text=text)
            else:
                if self.octane_socket_type in (SocketType.ST_INT2, SocketType.ST_INT3, SocketType.ST_FLOAT2, SocketType.ST_FLOAT3):
                    # layout in column to enable multiple selections for vector properties
                    layout.column(heading=text).prop(self, "default_value", text="")
                else:
                    layout.prop(self, "default_value", text=text)
        else:
            layout.label(text=text)
            if self.octane_socket_type != SocketType.ST_OUTPUT:
                op = layout.operator("octane.add_default_node", icon="ADD", text="")
                op.node_type = self.octane_default_node_type
                op.input_socket_name = self.name
                op.output_socket_pin_type = self.octane_pin_type

    def draw(self, context, layout, node, text):
        self.draw_prop(context, layout, text)

    def draw_color(self, context, node):
        return self.color

    def is_octane_dynamic_pin(self):
        return self.octane_pin_id - self.DYNAMIC_PIN_ID_OFFSET >= 0

    def get_octane_dynamic_pin_index(self):
        pin_index = self.octane_pin_id - self.DYNAMIC_PIN_ID_OFFSET
        if pin_index < 0:
            return consts.P_INVALID
        return pin_index

    def update_node_tree(self, context):
        if self.node.id_data:
            self.node.id_data.update()


class OctaneGroupTitleSocket(OctaneBaseSocket):    
    bl_label="Octane Group Title"  
    bl_idname="OctaneGroupTitleSocket"
    bl_socket_idname="OctaneGroupTitleSocket"
    color=consts.OctanePinColor.GroupTitle
    display_shape="CIRCLE_DOT"
    octane_hide_value=True
    octane_socket_type: IntProperty(name="Socket Type", default=SocketType.ST_GROUP_TITLE)

    octane_group_sockets: StringProperty(name="Group Sockets", default="")
    show_group_sockets: BoolProperty(name="Show/hide", default=True, description="Show/hide group sockets", update=utility.group_title_socket_show_group_sockets_update_callback)

    def draw_prop(self, context, layout, text):
        layout.alignment = "LEFT"
        # reformat self.bl_label, removing Octane tag "[OctaneGroupTitle]"
        label = self.bl_label.replace("[OctaneGroupTitle]", "")    
        layout.prop(self, "show_group_sockets", icon="TRIA_RIGHT" if self.show_group_sockets else "TRIA_DOWN", text=label, emboss=False)

    def draw(self, context, layout, node, text):
        self.draw_prop(context, layout, text)

    def draw_color(self, context, node):
        return self.color


class OctanePatternInput(OctaneBaseSocket):
    bl_label="Octane Pattern Input"  
    bl_idname="OctanePatternInput"
    octane_input_pattern=""
    octane_input_format_pattern="{}"

    def init(self, **kwargs):
        super().init(**kwargs)
        index = kwargs["index"] if "index" in kwargs else None
        offset = kwargs["offset"] if "offset" in kwargs else 0
        group_size = kwargs["group_size"] if "group_size" in kwargs else 1
        if index is not None:
            self.set_pattern_input_name(index, offset, group_size)

    @classmethod
    def generate_pattern_input_name(cls, idx):
        return cls.octane_input_format_pattern.format(idx)

    def set_pattern_input_name(self, idx, offset=0, group_size=1):        
        self.octane_pin_id = self.DYNAMIC_PIN_ID_OFFSET + 1 + (idx - 1) * group_size + offset        
        self.name = self.generate_pattern_input_name(idx)


class OctaneMovableInput(OctanePatternInput):
    bl_idname="OctaneMovableInput"
    octane_movable_input_count_attribute_name=""
    octane_sub_movable_inputs=[]
    octane_show_action_ops=True
    octane_hide_value=True
    octane_reversed_input_sockets=False    

    def draw_prop(self, context, layout, text):
        row = layout.row()
        split = row.split(factor=0.25)
        c = split.column()
        c.label(text=text)
        split = split.split(factor=0.4)
        c = split.column()
        op = c.operator("octane.add_default_node", icon="ADD", text="")
        op.node_type = self.octane_default_node_type
        op.input_socket_name = self.name
        op.output_socket_pin_type = self.octane_pin_type
        if not self.octane_show_action_ops:
            return
        split = split.split()
        c1 = split.column()
        c2 = split.column()
        c3 = split.column()

        group_input_num = len(self.octane_sub_movable_inputs) + 1
        octane_movable_pin_count = getattr(self.node, self.octane_movable_input_count_attribute_name, 0)
        octane_movable_pin_count *= group_input_num        
        op = c1.operator("octane.remove_movable_input", icon="PANEL_CLOSE", text="")
        op.movable_input_count_attribute_name = self.octane_movable_input_count_attribute_name
        op.input_socket_name = self.name
        op.input_name_pattern = self.octane_input_pattern
        op.input_socket_bl_idname = self.bl_idname
        op.group_input_num = group_input_num
        op.reversed_input_sockets = self.octane_reversed_input_sockets
        c2.enabled = self.get_octane_dynamic_pin_index() != (octane_movable_pin_count if self.octane_reversed_input_sockets else 1)
        op = c2.operator("octane.move_up_movable_input", icon="SORT_DESC", text="")
        op.movable_input_count_attribute_name = self.octane_movable_input_count_attribute_name
        op.input_socket_name = self.name
        op.group_input_num = group_input_num
        c3.enabled = self.get_octane_dynamic_pin_index() != (1 if self.octane_reversed_input_sockets else octane_movable_pin_count - group_input_num + 1)
        op = c3.operator("octane.move_down_movable_input", icon="SORT_ASC", text="")
        op.movable_input_count_attribute_name = self.octane_movable_input_count_attribute_name
        op.input_socket_name = self.name
        op.group_input_num = group_input_num


class OctaneGroupTitleMovableInputs(OctaneGroupTitleSocket):
    bl_idname="OctaneGroupTitleMovableInputs"
    bl_label="[OctaneGroupTitle]OctaneGroupTitleMovableInputs"

    def init(self, **kwargs):
        super().init(**kwargs)
        _class = kwargs["cls"] if "cls" in kwargs else None
        max_num = kwargs["max_num"] if "max_num" in kwargs else None
        _classes = [_class, ]        
        if _class is not None and max_num is not None:
            _classes.extend(getattr(_class, "octane_sub_movable_inputs", []))
            sockets_list = []
            for socket_cls in _classes:            
                for idx in range(1, max_num + 1):
                    name = socket_cls.generate_pattern_input_name(idx)
                    sockets_list.append(name)
            self.octane_group_sockets = ";".join(sockets_list) + ";"                 


class OCTANE_OT_add_default_node_helper(bpy.types.Operator):
    """Add a node to the active tree"""
    bl_idname = "octane.add_default_node_helper"
    bl_label = "Add"

    offset_x = -50
    offset_y = -20
    socket_step_y = -20

    # The destination node
    destination_node = None
    # The destination socket name
    destination_socket_name = ""
    # The output socket pin type
    output_socket_pin_type = 0  
    # The type of the node to add
    node_type: StringProperty()
      
    @staticmethod
    def store_mouse_cursor(context, event):
        space = context.space_data
        tree = getattr(space, "edit_tree", None)

        if tree is None:
            return

        # convert mouse position to the View2D for later node placement
        if context.region.type == 'WINDOW':
            # convert mouse position to the View2D for later node placement
            space.cursor_location_from_region(
                event.mouse_region_x, event.mouse_region_y)
        else:
            space.cursor_location = tree.view_center

    @classmethod
    def poll(cls, context):
        return True

    @classmethod
    def update_destinations(cls, destination_node, destination_socket_name, output_socket_pin_type):
        cls.destination_node = destination_node
        cls.destination_socket_name = destination_socket_name
        cls.output_socket_pin_type = output_socket_pin_type

    @classmethod
    def _execute(cls, context, node_type):
        node = cls.destination_node
        cursor_location = None
        if node is None:
            space = context.space_data
            node_tree = space.edit_tree
            cursor_location = space.cursor_location
        else:
            node_tree = getattr(node, "id_data", None)
        if node_tree is None:
            return
        for n in node_tree.nodes:
            n.select = False            
        if len(node_type):
            output_socket_name = ""
            if node_type.find(":") != -1:
                node_type, output_socket_name = node_type.split(":")
            # Create node
            new_node = node_tree.nodes.new(node_type)
            if node is None:
                if cursor_location is not None:
                    new_node.location = cursor_location
                return
            # Location
            offset_x = -new_node.width + cls.offset_x
            offset_y = cls.offset_y
            step_y = cls.socket_step_y
            if len(node.inputs) > 0:
                step_y = -node.dimensions[1] / len(node.inputs)
            for _input in node.inputs:
                if _input.name == cls.destination_socket_name:
                    break
                offset_y += step_y
            else:
                offset_y = cls.offset_y
            new_node.location = (node.location.x + offset_x, node.location.y + offset_y) 
            # Link
            output_socket = None
            if output_socket_name in new_node.outputs:
                output_socket = new_node.outputs[output_socket_name]
            if output_socket is None:
                for output in new_node.outputs:
                    if getattr(output, "octane_pin_type", consts.PinType.PT_UNKNOWN) == cls.output_socket_pin_type:
                        output_socket = output
                        break
            if output_socket:
                input_socket = node.inputs[cls.destination_socket_name]
                node_tree.links.new(output_socket, input_socket)
            # Clear the stored destination node
            cls.destination_node = None

    def execute(self, context):
        self._execute(context, self.node_type)
        return {"FINISHED"}

    def invoke(self, context, event):
        self.store_mouse_cursor(context, event)
        result = self.execute(context)
        return result        


class OCTANE_OT_add_default_node(bpy.types.Operator):
    """Add an Octane default node(if there is one). \nOR Open a menu with all suitable nodes(if no default node available). \nUse 'Shift + Click' to always open the menu"""
    
    bl_idname = "octane.add_default_node"
    bl_label = "Add"
    bl_description = "Add an Octane default node(if there is one). \nOR Open a menu with all suitable nodes(if no default node available). \nUse 'Shift + Click' to always open the menu"

    offset_x = -50
    offset_y = -100

    node_type: StringProperty()
    input_socket_name: StringProperty()
    output_socket_pin_type: IntProperty()

    @classmethod
    def poll(cls, context):
        node = getattr(context, "node", None)
        node_tree = getattr(node, "id_data", None)
        return node is not None and node_tree is not None

    def invoke(self, context, event):
        node = context.node
        node_tree = node.id_data
        OCTANE_OT_add_default_node_helper.update_destinations(node, self.input_socket_name, self.output_socket_pin_type)
        if event.shift or len(self.node_type) == 0:
            OCTANE_NODE_MT_node_add.octane_pin_type = self.output_socket_pin_type
            bpy.ops.wm.call_menu(name="OCTANE_NODE_MT_node_add")
        else:
            OCTANE_OT_add_default_node_helper._execute(context, self.node_type)
        return {"FINISHED"}


class NODE_OT_octane_add_search(NodeAddOperator, bpy.types.Operator):
    '''Add a node to the active tree'''
    bl_idname = "node.octane_add_search"
    bl_label = "Search and Add Node"
    bl_options = {'REGISTER', 'UNDO'}
    bl_property = "node_item"

    _enum_item_hack = []

    # Create an enum list from node items
    def node_enum_items(self, context):
        import nodeitems_utils
        from . import node_items

        enum_items = NODE_OT_octane_add_search._enum_item_hack
        enum_items.clear()        

        for index, item in enumerate(nodeitems_utils.node_items_iter(context)):
            if isinstance(item, nodeitems_utils.NodeItem):
                if isinstance(item, node_items.OctaneNodeItem):
                    if item.is_pin_type_compatible(self.octane_pin_type):
                        new_item = True
                        for added_item in enum_items:
                            if item.label == added_item[1]:
                                new_item = False
                                break
                        if new_item:
                            enum_items.append(
                                (str(index),
                                 item.label,
                                 "",
                                 index,
                                 ))
                else:
                    # Do not show Blender's menu under quick adding mode(octane_pin_type is assigned)
                    if self.octane_pin_type == consts.PinType.PT_UNKNOWN:
                        enum_items.append(
                            (str(index),
                             item.label,
                             "",
                             index,
                             ))
        return enum_items

    # Look up the item based on index
    def find_node_item(self, context):
        import nodeitems_utils

        node_item = int(self.node_item)
        for index, item in enumerate(nodeitems_utils.node_items_iter(context)):
            if index == node_item:
                return item
        return None

    node_item: EnumProperty(
        name="Node Type",
        description="Node type",
        items=node_enum_items,
    )

    octane_pin_type: IntProperty()

    def execute(self, context):
        item = self.find_node_item(context)

        # no need to keep
        self._enum_item_hack.clear()

        if item:
            # apply settings from the node item
            for setting in item.settings.items():
                ops = self.settings.add()
                ops.name = setting[0]
                ops.value = setting[1]

            OCTANE_OT_add_default_node_helper._execute(context, item.nodetype)

            if self.use_transform:
                bpy.ops.node.translate_attach_remove_on_cancel(
                    'INVOKE_DEFAULT')

            return {'FINISHED'}
        else:
            return {'CANCELLED'}

    def invoke(self, context, event):
        self.store_mouse_cursor(context, event)
        # Delayed execution in the search popup
        context.window_manager.invoke_search_popup(self)
        return {'CANCELLED'}


class OCTANE_NODE_MT_node_add(bpy.types.Menu):
    bl_space_type = 'NODE_EDITOR'
    bl_label = "Add"
    bl_translation_context = i18n_contexts.operator_default    
    octane_pin_type = consts.PinType.PT_UNKNOWN

    def draw(self, context):
        import nodeitems_utils
        from . import node_items

        layout = self.layout
        layout.operator_context = 'INVOKE_DEFAULT'
        if nodeitems_utils.has_node_categories(context):
            props = layout.operator("node.octane_add_search", text="Search...", icon='VIEWZOOM')
            props.octane_pin_type = self.octane_pin_type
            props.use_transform = True

            layout.separator()

            # actual node submenus are defined by draw functions from node categories
            node_items.draw_octane_node_categories_menu(self, context, self.octane_pin_type)


class OCTANE_OT_modify_movable_input_num(bpy.types.Operator):
    movable_input_count_attribute_name: StringProperty()
    input_name_pattern: StringProperty()
    input_socket_bl_idname: StringProperty()
    group_input_num: IntProperty()
    reversed_input_sockets: BoolProperty(default=False)

    @classmethod
    def poll(cls, context):
        node = getattr(context, "node", None)
        return node is not None

    def update_movable_input_count(self, node):
        node.update_movable_input_count(self.movable_input_count_attribute_name, self.input_socket_bl_idname, self.input_name_pattern)

    def reversed_iter_indices_of_movable_inputs(self, node, target_input):
        target_input_index = 0
        for idx, _input in enumerate(node.inputs):
            if _input == target_input:
                target_input_index = idx
                break
        octane_sub_movable_inputs = getattr(target_input, "octane_sub_movable_inputs", [])
        for index in range(len(octane_sub_movable_inputs), -1, -1):
            yield (target_input_index + index, index)

    def set_input_name(self, node, target_input, index):
        group_size = len(target_input.octane_sub_movable_inputs) + 1
        for idx, offset in self.reversed_iter_indices_of_movable_inputs(node, target_input):            
            node.inputs[idx].set_pattern_input_name(index, offset, group_size) 
                
    def remove_input(self, node, target_input):
        for idx, offset in self.reversed_iter_indices_of_movable_inputs(node, target_input):
            node.inputs.remove(node.inputs[idx])   

    def swap_inputs(self, node, input1, input2):
        # swap_node_socket_position
        if input1.is_octane_dynamic_pin() and input2.is_octane_dynamic_pin():
            input1_index = 0
            input2_index = 0
            for idx, _input in enumerate(node.inputs):
                if _input == input1:
                    input1_index = idx 
                elif _input == input2:
                    input2_index = idx                  
            for offset in range(len(input1.octane_sub_movable_inputs) + 1):
                utility.swap_node_socket_position(node, node.inputs[input1_index + offset], node.inputs[input2_index + offset])
            input1_pin_idx = math.ceil(input1.get_octane_dynamic_pin_index() / self.group_input_num)
            input2_pin_idx = math.ceil(input2.get_octane_dynamic_pin_index() / self.group_input_num)
            self.set_input_name(node, input1, input2_pin_idx)
            self.set_input_name(node, input2, input1_pin_idx)


class OCTANE_OT_quick_add_movable_input(OCTANE_OT_modify_movable_input_num):
    bl_idname = "octane.quick_add_movable_input"
    bl_label = "Add Input"
    bl_description = "Add an movable input"

    def execute(self, context):
        node = context.node
        self.update_movable_input_count(node)
        octane_movable_pin_count = getattr(node, self.movable_input_count_attribute_name, 0)
        current_index = len(node.inputs)
        next_movable_input_index = octane_movable_pin_count + 1
        movable_input = node.inputs.new(self.input_socket_bl_idname, self.bl_label)
        movable_input.init(index=next_movable_input_index, offset=0, group_size=self.group_input_num)
        newly_created_configs = [(self.input_socket_bl_idname, self.input_name_pattern), ]
        for offset_idx, sub_input_class in enumerate(getattr(movable_input, "octane_sub_movable_inputs", [])):            
            sub_input = node.inputs.new(sub_input_class.bl_idname, sub_input_class.bl_label)
            sub_input.init(index=next_movable_input_index, offset=offset_idx + 1, group_size=self.group_input_num)
            newly_created_configs.append((sub_input_class.bl_idname, sub_input_class.octane_input_pattern))
        if self.reversed_input_sockets:
            for bl_idname, pattern in newly_created_configs:
                first_input_ui_index = None
                for input_idx in range(len(node.inputs) - 1, -1, -1):
                    _input = node.inputs[input_idx]
                    if _input.bl_idname == bl_idname and re.match(pattern, _input.name) is not None:
                        if input_idx != current_index:
                            node.inputs.move(input_idx, current_index)
                            current_index = input_idx
        self.update_movable_input_count(node)
        return {"FINISHED"}


class OCTANE_OT_quick_remove_movable_input(OCTANE_OT_modify_movable_input_num):
    bl_idname = "octane.quick_remove_movable_input"
    bl_label = "Remove Input"
    bl_description = "Remove the movable input"

    def execute(self, context):
        node = context.node
        target_input = None
        target_input_index = 0
        for input_idx in (range(len(node.inputs)) if self.reversed_input_sockets else range(len(node.inputs) - 1, -1, -1)):
            _input = node.inputs[input_idx]
            if _input.bl_idname == self.input_socket_bl_idname and re.match(self.input_name_pattern, _input.name) is not None:
                target_input = _input
                target_input_index = input_idx
                break
        if target_input is not None:
            self.remove_input(node, target_input)
        self.update_movable_input_count(node)
        # Fix the viewport update issue
        if node.id_data:
            node.id_data.update_tag()
        return {"FINISHED"}


class OCTANE_OT_remove_movable_input(OCTANE_OT_modify_movable_input_num):
    bl_idname = "octane.remove_movable_input"
    bl_label = "Remove Input"
    bl_description = "Remove this movable input"

    input_socket_name: StringProperty()

    def execute(self, context):
        node = context.node
        target_input = None
        if len(self.input_socket_name) and self.input_socket_name in node.inputs:
            target_input = node.inputs[self.input_socket_name]
            last_available_pin_index = None
            for idx in (range(len(node.inputs) - 1, -1, -1) if self.reversed_input_sockets else range(len(node.inputs))):
                _input = node.inputs[idx]
                if _input.bl_idname == target_input.bl_idname and last_available_pin_index is not None:
                    temp_last_available_pin_index = last_available_pin_index
                    if _input.is_octane_dynamic_pin():
                        last_available_pin_index = _input.get_octane_dynamic_pin_index()
                    else:
                        last_available_pin_index = None
                    self.set_input_name(node, _input, math.ceil(temp_last_available_pin_index / self.group_input_num))
                if _input == target_input and target_input.is_octane_dynamic_pin():
                    last_available_pin_index = target_input.get_octane_dynamic_pin_index()
        if target_input is not None:
            self.remove_input(node, target_input)
        self.update_movable_input_count(node)
        return {"FINISHED"}


class OCTANE_OT_move_up_movable_input(OCTANE_OT_modify_movable_input_num):
    """Move Up Input"""
    
    bl_idname = "octane.move_up_movable_input"
    bl_label = "Move Input Up"
    bl_description = "Move this movable input up"

    input_socket_name: StringProperty()

    def execute(self, context):
        node = context.node
        target_input = None
        if len(self.input_socket_name) and self.input_socket_name in node.inputs:
            target_input = node.inputs[self.input_socket_name]
        if target_input is not None:
            last_input = None            
            for _input in node.inputs:
                if _input == target_input:
                    break
                if _input.bl_idname == target_input.bl_idname:
                    last_input = _input
            if last_input is not None:
                self.swap_inputs(node, last_input, target_input)
        return {"FINISHED"}


class OCTANE_OT_move_down_movable_input(OCTANE_OT_modify_movable_input_num):
    """Move Down Input"""
    
    bl_idname = "octane.move_down_movable_input"
    bl_label = "Move Input Down"
    bl_description = "Move this movable input down"

    input_socket_name: StringProperty()

    def execute(self, context):
        node = context.node
        target_input = None
        if len(self.input_socket_name) and self.input_socket_name in node.inputs:
            target_input = node.inputs[self.input_socket_name]
        if target_input is not None:
            last_input = None
            for input_idx in range(len(node.inputs) - 1, 0, -1):
                _input = node.inputs[input_idx]
                if _input == target_input:
                    break
                if _input.bl_idname == target_input.bl_idname:
                    last_input = _input
            if last_input is not None:
                self.swap_inputs(node, target_input, last_input)
        return {"FINISHED"}


class OCTANE_OT_base_node_link_menu(bpy.types.Operator):
    """Open the node link menu"""
    
    bl_idname = "octane.base_node_link_menu"
    bl_label = "Octane Node Link Menu"
    bl_description = "Open the Octane node link menu"    
    configuration_map = {
        ("OUTPUT_MATERIAL", "Surface"): "octane.material_node_link_menu",
        ("OUTPUT_MATERIAL", "Volume"): "octane.volume_node_link_menu",
        ("OUTPUT_WORLD", "Octane Environment"): "octane.environment_node_link_menu",
        ("OUTPUT_WORLD", "Octane VisibleEnvironment"): "octane.visible_environment_node_link_menu",
    }   

    enum_items: EnumProperty(items=utility.node_input_enum_items_callback)
    octane_pin_type: IntProperty(default=consts.PinType.PT_UNKNOWN)

    @staticmethod
    def draw_node_link_menu(context, layout, node_tree, output_type, socket_name):
        operator_name = OCTANE_OT_base_node_link_menu.configuration_map.get((output_type, socket_name), None)
        if operator_name is None:
            return
        output_node = node_tree.get_output_node(consts.ENGINE_NAME)
        label = ""
        if output_node and len(output_node.inputs[socket_name].links):
            label = output_node.inputs[socket_name].links[0].from_node.bl_label
        left, right = utility.get_split_panel_ui_layout(layout)
        left.label(text=socket_name)
        op = right.operator_menu_enum(operator_name, "enum_items", text=label)

    def _execute(self, node_tree, node_bl_idname):       
        output_node_type, socket_name = self.configuration
        output_node = node_tree.get_output_node(consts.ENGINE_NAME)
        if output_node and output_node.type == output_node_type:
            socket = output_node.inputs[socket_name]
            utility.node_input_quick_operator(node_tree, output_node, socket, node_bl_idname)       


class OCTANE_OT_material_node_link_menu(OCTANE_OT_base_node_link_menu):
    bl_idname = "octane.material_node_link_menu"
    configuration = ("OUTPUT_MATERIAL", "Surface")
    octane_pin_type: IntProperty(default=consts.PinType.PT_MATERIAL)

    def execute(self, context):
        mat = context.material
        if not mat or not mat.use_nodes:
            return {"FINISHED"}
        node_tree = mat.node_tree
        self._execute(node_tree, self.enum_items)
        return {"FINISHED"}


class OCTANE_OT_volume_node_link_menu(OCTANE_OT_base_node_link_menu):
    bl_idname = "octane.volume_node_link_menu"
    configuration = ("OUTPUT_MATERIAL", "Volume")  
    octane_pin_type: IntProperty(default=consts.PinType.PT_MEDIUM)
 
    def execute(self, context):
        mat = context.material
        if not mat or not mat.use_nodes:
            return {"FINISHED"}
        node_tree = mat.node_tree
        self._execute(node_tree, self.enum_items)
        return {"FINISHED"}


class OCTANE_OT_environment_node_link_menu(OCTANE_OT_base_node_link_menu):
    bl_idname = "octane.environment_node_link_menu"
    configuration = ("OUTPUT_WORLD", "Octane Environment")  
    octane_pin_type: IntProperty(default=consts.PinType.PT_ENVIRONMENT)
 
    def execute(self, context):
        world = context.world
        if not world or not world.use_nodes:
            return {"FINISHED"}
        node_tree = world.node_tree
        self._execute(node_tree, self.enum_items)
        return {"FINISHED"}


class OCTANE_OT_visible_environment_node_link_menu(OCTANE_OT_base_node_link_menu):
    bl_idname = "octane.visible_environment_node_link_menu"
    configuration = ("OUTPUT_WORLD", "Octane VisibleEnvironment")  
    octane_pin_type: IntProperty(default=consts.PinType.PT_ENVIRONMENT)
 
    def execute(self, context):
        world = context.world
        if not world or not world.use_nodes:
            return {"FINISHED"}
        node_tree = world.node_tree
        self._execute(node_tree, self.enum_items)
        return {"FINISHED"}


_CLASSES = [
    OCTANE_OT_add_default_node_helper,
    OCTANE_OT_add_default_node,
    NODE_OT_octane_add_search,
    OCTANE_NODE_MT_node_add,  
    OCTANE_OT_quick_add_movable_input,
    OCTANE_OT_quick_remove_movable_input,
    OCTANE_OT_remove_movable_input,
    OCTANE_OT_move_up_movable_input,
    OCTANE_OT_move_down_movable_input,
    OCTANE_OT_material_node_link_menu,
    OCTANE_OT_volume_node_link_menu,
    OCTANE_OT_environment_node_link_menu,
    OCTANE_OT_visible_environment_node_link_menu,
    OctaneGroupTitleSocket,
]


def register(): 
    for cls in _CLASSES:
        register_class(cls)


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)