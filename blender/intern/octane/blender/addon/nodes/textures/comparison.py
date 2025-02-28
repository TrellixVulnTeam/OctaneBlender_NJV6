##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneComparisonTexture1(OctaneBaseSocket):
    bl_idname="OctaneComparisonTexture1"
    bl_label="Input A"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=238)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneComparisonTexture2(OctaneBaseSocket):
    bl_idname="OctaneComparisonTexture2"
    bl_label="Input B"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=239)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.500000, update=None, description="Input texture that is used a the right operand", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneComparisonOperationType(OctaneBaseSocket):
    bl_idname="OctaneComparisonOperationType"
    bl_label="Operation"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=613)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Less than (A < B)", "Less than (A < B)", "", 0),
        ("Greater than (A > B)", "Greater than (A > B)", "", 1),
        ("Equal (A == B)", "Equal (A == B)", "", 2),
        ("Not equal (A != B)", "Not equal (A != B)", "", 3),
        ("Less or equal (A <= B)", "Less or equal (A <= B)", "", 4),
        ("Greater or equal (A >= B)", "Greater or equal (A >= B)", "", 5),
    ]
    default_value: EnumProperty(default="Less than (A < B)", update=None, description="The comparison operation, e.g. A < B", items=items)
    octane_hide_value=False
    octane_min_version=11000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneComparisonTexture3(OctaneBaseSocket):
    bl_idname="OctaneComparisonTexture3"
    bl_label="If true"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneRGBColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=337)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=None, description="Output texture that is picked if A op B is TRUE", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneComparisonTexture4(OctaneBaseSocket):
    bl_idname="OctaneComparisonTexture4"
    bl_label="If false"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneRGBColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=338)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=None, description="Output texture that is picked if A op B is FALSE", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneComparison(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneComparison"
    bl_label="Comparison"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=107)
    octane_socket_list: StringProperty(name="Socket List", default="Input A;Input B;Operation;If true;If false;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=5)

    def init(self, context):
        self.inputs.new("OctaneComparisonTexture1", OctaneComparisonTexture1.bl_label).init()
        self.inputs.new("OctaneComparisonTexture2", OctaneComparisonTexture2.bl_label).init()
        self.inputs.new("OctaneComparisonOperationType", OctaneComparisonOperationType.bl_label).init()
        self.inputs.new("OctaneComparisonTexture3", OctaneComparisonTexture3.bl_label).init()
        self.inputs.new("OctaneComparisonTexture4", OctaneComparisonTexture4.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_classes=[
    OctaneComparisonTexture1,
    OctaneComparisonTexture2,
    OctaneComparisonOperationType,
    OctaneComparisonTexture3,
    OctaneComparisonTexture4,
    OctaneComparison,
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
