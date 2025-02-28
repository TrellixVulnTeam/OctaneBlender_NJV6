##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneLightAOVEnabled(OctaneBaseSocket):
    bl_idname="OctaneLightAOVEnabled"
    bl_label="Enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=42)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Enables the render AOV")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightAOVSubType(OctaneBaseSocket):
    bl_idname="OctaneLightAOVSubType"
    bl_label="ID"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=703)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Sun", "Sun", "", 0),
        ("Environment", "Environment", "", 1),
        ("Light ID 1", "Light ID 1", "", 2),
        ("Light ID 2", "Light ID 2", "", 3),
        ("Light ID 3", "Light ID 3", "", 4),
        ("Light ID 4", "Light ID 4", "", 5),
        ("Light ID 5", "Light ID 5", "", 6),
        ("Light ID 6", "Light ID 6", "", 7),
        ("Light ID 7", "Light ID 7", "", 8),
        ("Light ID 8", "Light ID 8", "", 9),
    ]
    default_value: EnumProperty(default="Light ID 1", update=OctaneBaseSocket.update_node_tree, description="The ID of the light AOV", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneLightAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneLightAOV"
    bl_label="Light AOV"
    bl_width_default=200
    octane_render_pass_id={0: 22, 1: 21, 2: 23, 3: 24, 4: 25, 5: 26, 6: 27, 7: 28, 8: 29, 9: 30, }
    octane_render_pass_name={0: "Sunlight", 1: "Ambient light", 2: "Light ID 1", 3: "Light ID 2", 4: "Light ID 3", 5: "Light ID 4", 6: "Light ID 5", 7: "Light ID 6", 8: "Light ID 7", 9: "Light ID 8", }
    octane_render_pass_short_name={0: "SLi", 1: "ALi", 2: "Li1", 3: "Li2", 4: "Li3", 5: "Li4", 6: "Li5", 7: "Li6", 8: "Li7", 9: "Li8", }
    octane_render_pass_description={0: "Captures the sunlight in the scene", 1: "Captures the ambient light (sky and environment) in the scene", 2: "Captures the light of the emitters with light pass ID 1", 3: "Captures the light of the emitters with light pass ID 2", 4: "Captures the light of the emitters with light pass ID 3", 5: "Captures the light of the emitters with light pass ID 4", 6: "Captures the light of the emitters with light pass ID 5", 7: "Captures the light of the emitters with light pass ID 6", 8: "Captures the light of the emitters with light pass ID 7", 9: "Captures the light of the emitters with light pass ID 8", }
    octane_render_pass_sub_type_name="ID"
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=205)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;ID;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=2)

    def init(self, context):
        self.inputs.new("OctaneLightAOVEnabled", OctaneLightAOVEnabled.bl_label).init()
        self.inputs.new("OctaneLightAOVSubType", OctaneLightAOVSubType.bl_label).init()
        self.outputs.new("OctaneRenderAOVsOutSocket", "Render AOVs out").init()


_classes=[
    OctaneLightAOVEnabled,
    OctaneLightAOVSubType,
    OctaneLightAOV,
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
