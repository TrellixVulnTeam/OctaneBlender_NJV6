##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneRangeInput(OctaneBaseSocket):
    bl_idname="OctaneRangeInput"
    bl_label="Value"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=82)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRangeInterpolationType(OctaneBaseSocket):
    bl_idname="OctaneRangeInterpolationType"
    bl_label="Interpolation"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=661)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Linear", "Linear", "", 0),
        ("Steps", "Steps", "", 1),
        ("Smoothstep", "Smoothstep", "", 2),
        ("Smootherstep", "Smootherstep", "", 3),
    ]
    default_value: EnumProperty(default="Linear", update=None, description="Interpolation", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRangeInputMin(OctaneBaseSocket):
    bl_idname="OctaneRangeInputMin"
    bl_label="Input min"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=662)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="Input min", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRangeInputMax(OctaneBaseSocket):
    bl_idname="OctaneRangeInputMax"
    bl_label="Input max"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=663)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Input max", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRangeOutputMin(OctaneBaseSocket):
    bl_idname="OctaneRangeOutputMin"
    bl_label="Output min"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=664)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="Output min", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRangeOutputMax(OctaneBaseSocket):
    bl_idname="OctaneRangeOutputMax"
    bl_label="Output max"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=665)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Output max", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRangeInterpolationSteps(OctaneBaseSocket):
    bl_idname="OctaneRangeInterpolationSteps"
    bl_label="Steps"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=666)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=8, update=None, description="Number of steps when using stepped interpolation", min=1, max=2147483647, soft_min=1, soft_max=2147483647, step=1, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRangeClamp(OctaneBaseSocket):
    bl_idname="OctaneRangeClamp"
    bl_label="Clamp"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=628)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="Clamp the result to the output range")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRange(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneRange"
    bl_label="Range"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=334)
    octane_socket_list: StringProperty(name="Socket List", default="Value;Interpolation;Input min;Input max;Output min;Output max;Steps;Clamp;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=8)

    def init(self, context):
        self.inputs.new("OctaneRangeInput", OctaneRangeInput.bl_label).init()
        self.inputs.new("OctaneRangeInterpolationType", OctaneRangeInterpolationType.bl_label).init()
        self.inputs.new("OctaneRangeInputMin", OctaneRangeInputMin.bl_label).init()
        self.inputs.new("OctaneRangeInputMax", OctaneRangeInputMax.bl_label).init()
        self.inputs.new("OctaneRangeOutputMin", OctaneRangeOutputMin.bl_label).init()
        self.inputs.new("OctaneRangeOutputMax", OctaneRangeOutputMax.bl_label).init()
        self.inputs.new("OctaneRangeInterpolationSteps", OctaneRangeInterpolationSteps.bl_label).init()
        self.inputs.new("OctaneRangeClamp", OctaneRangeClamp.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_classes=[
    OctaneRangeInput,
    OctaneRangeInterpolationType,
    OctaneRangeInputMin,
    OctaneRangeInputMax,
    OctaneRangeOutputMin,
    OctaneRangeOutputMax,
    OctaneRangeInterpolationSteps,
    OctaneRangeClamp,
    OctaneRange,
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
