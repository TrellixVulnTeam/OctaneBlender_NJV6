##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneRenderAOVGroupEnabled(OctaneBaseSocket):
    bl_idname="OctaneRenderAOVGroupEnabled"
    bl_label="Enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=42)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Enables/disables all AOVs of this group")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderAOVGroupRenderPassesRaw(OctaneBaseSocket):
    bl_idname="OctaneRenderAOVGroupRenderPassesRaw"
    bl_label="Raw"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=277)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="Make the beauty pass raw render passes by dividing out the color of the BxDF of the surface hit by the camera ray")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderAOVGroupRenderPassCryptomatteCount(OctaneBaseSocket):
    bl_idname="OctaneRenderAOVGroupRenderPassCryptomatteCount"
    bl_label="Cryptomatte bins"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=456)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=6, update=None, description="Amount of cryptomatte bins to render", min=2, max=10, soft_min=2, soft_max=10, step=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderAOVGroupRenderPassCryptomatteSeedFactor(OctaneBaseSocket):
    bl_idname="OctaneRenderAOVGroupRenderPassCryptomatteSeedFactor"
    bl_label="Cryptomatte seed factor"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=472)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=10, update=None, description="Amount of samples to use for seeding cryptomatte. This gets multiplied with the amount of bins.\nLow values result in pitting artefacts at feathered edges, while large values the values can result in artefacts in places with coverage for lots of different IDs", min=4, max=25, soft_min=4, soft_max=25, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderAOVGroupRenderPassInfoMaxSamples(OctaneBaseSocket):
    bl_idname="OctaneRenderAOVGroupRenderPassInfoMaxSamples"
    bl_label="Max info samples"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=161)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=128, update=None, description="The maximum number of samples for the info passes", min=1, max=1024, soft_min=1, soft_max=1024, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderAOVGroupSamplingMode(OctaneBaseSocket):
    bl_idname="OctaneRenderAOVGroupSamplingMode"
    bl_label="Info sampling mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=329)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Distributed rays", "Distributed rays", "", 0),
        ("Non-distributed with pixel filtering", "Non-distributed with pixel filtering", "", 1),
        ("Non-distributed without pixel filtering", "Non-distributed without pixel filtering", "", 2),
    ]
    default_value: EnumProperty(default="Distributed rays", update=None, description="Enables motion blur and depth of field, and sets pixel filtering modes.\n\n'Distributed rays': Enables motion blur and DOF, and also enables pixel filtering.\n'Non-distributed with pixel filtering': Disables motion blur and DOF, but leaves pixel filtering enabled.\n'Non-distributed without pixel filtering': Disables motion blur and DOF, and disables pixel filtering for all render passes except for render layer mask and ambient occlusion", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderAOVGroupOpacityThreshold(OctaneBaseSocket):
    bl_idname="OctaneRenderAOVGroupOpacityThreshold"
    bl_label="Info opacity threshold"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=630)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Geometry with an opacity higher or equal to this value is treated as totally opaque", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderAOVGroupGroupOptions(OctaneGroupTitleSocket):
    bl_idname="OctaneRenderAOVGroupGroupOptions"
    bl_label="[OctaneGroupTitle]Options"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Raw;Cryptomatte bins;Cryptomatte seed factor;Max info samples;Info sampling mode;Info opacity threshold;")

class OctaneRenderAOVGroup(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneRenderAOVGroup"
    bl_label="Render AOV group"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=179)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;Raw;Cryptomatte bins;Cryptomatte seed factor;Max info samples;Info sampling mode;Info opacity threshold;")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_aov_count;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="2;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=7)

    a_aov_count: IntProperty(name="Aov count", default=0, update=None, description="The number of render AOV inputs. Changing this value and evaluating the node will update the number of render AOV inputs")

    def init(self, context):
        self.inputs.new("OctaneRenderAOVGroupEnabled", OctaneRenderAOVGroupEnabled.bl_label).init()
        self.inputs.new("OctaneRenderAOVGroupGroupOptions", OctaneRenderAOVGroupGroupOptions.bl_label).init()
        self.inputs.new("OctaneRenderAOVGroupRenderPassesRaw", OctaneRenderAOVGroupRenderPassesRaw.bl_label).init()
        self.inputs.new("OctaneRenderAOVGroupRenderPassCryptomatteCount", OctaneRenderAOVGroupRenderPassCryptomatteCount.bl_label).init()
        self.inputs.new("OctaneRenderAOVGroupRenderPassCryptomatteSeedFactor", OctaneRenderAOVGroupRenderPassCryptomatteSeedFactor.bl_label).init()
        self.inputs.new("OctaneRenderAOVGroupRenderPassInfoMaxSamples", OctaneRenderAOVGroupRenderPassInfoMaxSamples.bl_label).init()
        self.inputs.new("OctaneRenderAOVGroupSamplingMode", OctaneRenderAOVGroupSamplingMode.bl_label).init()
        self.inputs.new("OctaneRenderAOVGroupOpacityThreshold", OctaneRenderAOVGroupOpacityThreshold.bl_label).init()
        self.outputs.new("OctaneRenderAOVsOutSocket", "Render AOVs out").init()


_classes=[
    OctaneRenderAOVGroupEnabled,
    OctaneRenderAOVGroupRenderPassesRaw,
    OctaneRenderAOVGroupRenderPassCryptomatteCount,
    OctaneRenderAOVGroupRenderPassCryptomatteSeedFactor,
    OctaneRenderAOVGroupRenderPassInfoMaxSamples,
    OctaneRenderAOVGroupSamplingMode,
    OctaneRenderAOVGroupOpacityThreshold,
    OctaneRenderAOVGroupGroupOptions,
    OctaneRenderAOVGroup,
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


class OctaneRenderAOVGroupAOVInput(OctaneMovableInput):
    bl_idname="OctaneRenderAOVGroupAOVInput"
    bl_label="AOV"
    octane_movable_input_count_attribute_name="a_aov_count"
    octane_input_pattern=r"AOV \d+"
    octane_input_format_pattern="AOV {}"
    color=consts.OctanePinColor.RenderAOVs
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_RENDER_PASSES)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneRenderAOVGroupGroupAOVs(OctaneGroupTitleMovableInputs):
    bl_idname="OctaneRenderAOVGroupGroupAOVs"
    bl_label="[OctaneGroupTitle]AOVs"
    octane_group_sockets: StringProperty(name="Group Sockets", default="")


class OctaneRenderAOVGroup_Override(OctaneRenderAOVGroup):
    MAX_AOV_INPUT_COUNT = 16
    DEFAULT_AOV_INPUT_COUNT = 4    

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneRenderAOVGroupGroupAOVs", OctaneRenderAOVGroupGroupAOVs.bl_label).init(cls=OctaneRenderAOVGroupAOVInput, max_num=self.MAX_AOV_INPUT_COUNT)        
        self.init_movable_inputs(context, OctaneRenderAOVGroupAOVInput, self.DEFAULT_AOV_INPUT_COUNT)

    def draw_buttons(self, context, layout):
        self.draw_movable_inputs(context, layout, OctaneRenderAOVGroupAOVInput, self.MAX_AOV_INPUT_COUNT)


_added_classes = [OctaneRenderAOVGroupAOVInput, OctaneRenderAOVGroupGroupAOVs]
_classes = _added_classes + _classes
utility.override_class(_classes, OctaneRenderAOVGroup, OctaneRenderAOVGroup_Override)    