##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneRoundEdgesRoundEdgesMode(OctaneBaseSocket):
    bl_idname="OctaneRoundEdgesRoundEdgesMode"
    bl_label="Mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=485)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Off", "Off", "", 0),
        ("Fast", "Fast", "", 1),
        ("Accurate", "Accurate", "", 2),
        ("Accurate convex only", "Accurate convex only", "", 3),
        ("Accurate concave only", "Accurate concave only", "", 4),
    ]
    default_value: EnumProperty(default="Fast", update=None, description="Whether rounding is applied to convex and/or concave edges", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRoundEdgesRoundEdgesRadius(OctaneBaseSocket):
    bl_idname="OctaneRoundEdgesRoundEdgesRadius"
    bl_label="Radius"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=473)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="Edge rounding radius", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=100.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRoundEdgesRoundEdgesCurvatureRoundness(OctaneBaseSocket):
    bl_idname="OctaneRoundEdgesRoundEdgesCurvatureRoundness"
    bl_label="Roundness"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=475)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Specifies the roundness of the edge being 1 completely round and 0 a chamfer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRoundEdgesRoundEdgesSampleCount(OctaneBaseSocket):
    bl_idname="OctaneRoundEdgesRoundEdgesSampleCount"
    bl_label="Samples"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=508)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=8, update=None, description="The number of rays to use when sampling the neighboring geometry", min=4, max=16, soft_min=4, soft_max=16, step=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=6000500
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRoundEdgesRoundEdgesConsiderOtherObjects(OctaneBaseSocket):
    bl_idname="OctaneRoundEdgesRoundEdgesConsiderOtherObjects"
    bl_label="Consider other objects"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=476)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="Whether to consider other objects in the scene or just the current object")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRoundEdgesGroupAccurateModeSettings(OctaneGroupTitleSocket):
    bl_idname="OctaneRoundEdgesGroupAccurateModeSettings"
    bl_label="[OctaneGroupTitle]Accurate mode settings"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Roundness;Samples;Consider other objects;")

class OctaneRoundEdges(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneRoundEdges"
    bl_label="Round edges"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=137)
    octane_socket_list: StringProperty(name="Socket List", default="Mode;Radius;Roundness;Samples;Consider other objects;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=5)

    def init(self, context):
        self.inputs.new("OctaneRoundEdgesRoundEdgesMode", OctaneRoundEdgesRoundEdgesMode.bl_label).init()
        self.inputs.new("OctaneRoundEdgesRoundEdgesRadius", OctaneRoundEdgesRoundEdgesRadius.bl_label).init()
        self.inputs.new("OctaneRoundEdgesGroupAccurateModeSettings", OctaneRoundEdgesGroupAccurateModeSettings.bl_label).init()
        self.inputs.new("OctaneRoundEdgesRoundEdgesCurvatureRoundness", OctaneRoundEdgesRoundEdgesCurvatureRoundness.bl_label).init()
        self.inputs.new("OctaneRoundEdgesRoundEdgesSampleCount", OctaneRoundEdgesRoundEdgesSampleCount.bl_label).init()
        self.inputs.new("OctaneRoundEdgesRoundEdgesConsiderOtherObjects", OctaneRoundEdgesRoundEdgesConsiderOtherObjects.bl_label).init()
        self.outputs.new("OctaneRoundEdgesOutSocket", "Round edges out").init()


_classes=[
    OctaneRoundEdgesRoundEdgesMode,
    OctaneRoundEdgesRoundEdgesRadius,
    OctaneRoundEdgesRoundEdgesCurvatureRoundness,
    OctaneRoundEdgesRoundEdgesSampleCount,
    OctaneRoundEdgesRoundEdgesConsiderOtherObjects,
    OctaneRoundEdgesGroupAccurateModeSettings,
    OctaneRoundEdges,
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
