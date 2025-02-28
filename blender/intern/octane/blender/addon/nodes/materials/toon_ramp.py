##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneToonRampGradientInterpolationType(OctaneBaseSocket):
    bl_idname="OctaneToonRampGradientInterpolationType"
    bl_label="Interpolation"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=299)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Constant", "Constant", "", 1),
        ("Linear", "Linear", "", 2),
        ("Cubic", "Cubic", "", 3),
    ]
    default_value: EnumProperty(default="Constant", update=None, description="Determines how colors are blended", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonRampMin(OctaneBaseSocket):
    bl_idname="OctaneToonRampMin"
    bl_label="Start value"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=113)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(0.500000, 0.500000, 0.500000), update=None, description="Output value at 0", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonRampMax(OctaneBaseSocket):
    bl_idname="OctaneToonRampMax"
    bl_label="End value"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=106)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=None, description="Output value at 1.0", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonRamp(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneToonRamp"
    bl_label="Toon ramp"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=122)
    octane_socket_list: StringProperty(name="Socket List", default="Interpolation;Start value;End value;")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_num_controlpoints;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="2;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=3)

    a_num_controlpoints: IntProperty(name="Num controlpoints", default=0, update=None, description="The number of control points between start and end")

    def init(self, context):
        self.inputs.new("OctaneToonRampGradientInterpolationType", OctaneToonRampGradientInterpolationType.bl_label).init()
        self.inputs.new("OctaneToonRampMin", OctaneToonRampMin.bl_label).init()
        self.inputs.new("OctaneToonRampMax", OctaneToonRampMax.bl_label).init()
        self.outputs.new("OctaneToonRampOutSocket", "Toon ramp out").init()


_classes=[
    OctaneToonRampGradientInterpolationType,
    OctaneToonRampMin,
    OctaneToonRampMax,
    OctaneToonRamp,
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
