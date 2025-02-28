##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneLayeredMaterialMaterial1(OctaneBaseSocket):
    bl_idname="OctaneLayeredMaterialMaterial1"
    bl_label="Base Material"
    color=consts.OctanePinColor.Material
    octane_default_node_type="OctaneDiffuseMaterial"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=100)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_MATERIAL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLayeredMaterialCustomAov(OctaneBaseSocket):
    bl_idname="OctaneLayeredMaterialCustomAov"
    bl_label="Custom AOV"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=632)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("None", "None", "", 4096),
        ("Custom AOV 1", "Custom AOV 1", "", 0),
        ("Custom AOV 2", "Custom AOV 2", "", 1),
        ("Custom AOV 3", "Custom AOV 3", "", 2),
        ("Custom AOV 4", "Custom AOV 4", "", 3),
        ("Custom AOV 5", "Custom AOV 5", "", 4),
        ("Custom AOV 6", "Custom AOV 6", "", 5),
        ("Custom AOV 7", "Custom AOV 7", "", 6),
        ("Custom AOV 8", "Custom AOV 8", "", 7),
        ("Custom AOV 9", "Custom AOV 9", "", 8),
        ("Custom AOV 10", "Custom AOV 10", "", 9),
    ]
    default_value: EnumProperty(default="None", update=None, description="If a custom AOV is selected, it will write a mask to it where the material is visible", items=items)
    octane_hide_value=False
    octane_min_version=11000002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLayeredMaterialCustomAovChannel(OctaneBaseSocket):
    bl_idname="OctaneLayeredMaterialCustomAovChannel"
    bl_label="Custom AOV channel"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=633)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("All", "All", "", 0),
        ("Red", "Red", "", 1),
        ("Green", "Green", "", 2),
        ("Blue", "Blue", "", 3),
    ]
    default_value: EnumProperty(default="All", update=None, description="If a custom AOV is selected, the selected channel(s) will receive the mask", items=items)
    octane_hide_value=False
    octane_min_version=11000002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLayeredMaterial(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneLayeredMaterial"
    bl_label="Layered material"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=143)
    octane_socket_list: StringProperty(name="Socket List", default="Base Material;Custom AOV;Custom AOV channel;")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_pin_count;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="2;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=3)

    a_pin_count: IntProperty(name="Pin count", default=0, update=None, description="The number of material layers. New material layer pins will be added to the end of the pin list")

    def init(self, context):
        self.inputs.new("OctaneLayeredMaterialMaterial1", OctaneLayeredMaterialMaterial1.bl_label).init()
        self.inputs.new("OctaneLayeredMaterialCustomAov", OctaneLayeredMaterialCustomAov.bl_label).init()
        self.inputs.new("OctaneLayeredMaterialCustomAovChannel", OctaneLayeredMaterialCustomAovChannel.bl_label).init()
        self.outputs.new("OctaneMaterialOutSocket", "Material out").init()


_classes=[
    OctaneLayeredMaterialMaterial1,
    OctaneLayeredMaterialCustomAov,
    OctaneLayeredMaterialCustomAovChannel,
    OctaneLayeredMaterial,
]

def register():
    from bpy.utils import register_class
    for _class in _classes:
        register_class(_class)

def unregister():
    from bpy.utils import unregister_class
    for _class in reversed(_classes):
        unregister_class(_class)

##### END OCTANE GENERATED CODE BLOCK #####

from ...utils import utility


class OctaneLayeredMaterialLayerMovableInput(OctaneMovableInput):
    bl_idname="OctaneLayeredMaterialLayerMovableInput"
    bl_label="Layer"
    octane_movable_input_count_attribute_name="a_pin_count"
    octane_input_pattern=r"Layer \d+"
    octane_input_format_pattern="Layer {}"
    color=consts.OctanePinColor.MaterialLayer
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_MATERIAL_LAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneLayeredMaterial_Override(OctaneLayeredMaterial):
    MAX_AOV_OUTPUT_COUNT = 8
    DEFAULT_AOV_OUTPUT_COUNT = 1

    def init(self, context):
        super().init(context)
        self.init_movable_inputs(context, OctaneLayeredMaterialLayerMovableInput, self.DEFAULT_AOV_OUTPUT_COUNT)

    def draw_buttons(self, context, layout):
        self.draw_movable_inputs(context, layout, OctaneLayeredMaterialLayerMovableInput, self.MAX_AOV_OUTPUT_COUNT)


_added_classes = [OctaneLayeredMaterialLayerMovableInput, ]
_classes = _added_classes + _classes
utility.override_class(_classes, OctaneLayeredMaterial, OctaneLayeredMaterial_Override)   