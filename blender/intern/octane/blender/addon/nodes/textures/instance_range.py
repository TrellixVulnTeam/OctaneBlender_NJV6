##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneInstanceRangeMax(OctaneBaseSocket):
    bl_idname="OctaneInstanceRangeMax"
    bl_label="Maximum ID"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=106)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=1, update=None, description="Maximum instance ID used to map an instance ID to a grey scale value. This node maps instance ID zero to black color, and maximum instance ID to white color and vice versa when invert is selected", min=1, max=2147483646, soft_min=1, soft_max=2147483646, step=1, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneInstanceRangeInvert(OctaneBaseSocket):
    bl_idname="OctaneInstanceRangeInvert"
    bl_label="Invert"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=83)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="Invert the colors that are mapped to instance IDs, ie. map the instance ID 0 to white color and the maximum ID to black color")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneInstanceRange(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneInstanceRange"
    bl_label="Instance range"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=114)
    octane_socket_list: StringProperty(name="Socket List", default="Maximum ID;Invert;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=2)

    def init(self, context):
        self.inputs.new("OctaneInstanceRangeMax", OctaneInstanceRangeMax.bl_label).init()
        self.inputs.new("OctaneInstanceRangeInvert", OctaneInstanceRangeInvert.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_classes=[
    OctaneInstanceRangeMax,
    OctaneInstanceRangeInvert,
    OctaneInstanceRange,
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
