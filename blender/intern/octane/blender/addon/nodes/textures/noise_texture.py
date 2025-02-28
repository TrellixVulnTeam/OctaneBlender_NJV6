##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneNoiseTextureNoiseType(OctaneBaseSocket):
    bl_idname="OctaneNoiseTextureNoiseType"
    bl_label="Noise type"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=117)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Perlin", "Perlin", "", 0),
        ("Turbulence", "Turbulence", "", 1),
        ("Circular", "Circular", "", 2),
        ("Chips", "Chips", "", 3),
    ]
    default_value: EnumProperty(default="Perlin", update=None, description="Noise type", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNoiseTextureOctaves(OctaneBaseSocket):
    bl_idname="OctaneNoiseTextureOctaves"
    bl_label="Octaves"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=121)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=5, update=None, description="Number of octaves", min=1, max=16, soft_min=1, soft_max=16, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNoiseTextureOmega(OctaneBaseSocket):
    bl_idname="OctaneNoiseTextureOmega"
    bl_label="Omega"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=123)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.500000, update=None, description="Difference per octave interval", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNoiseTextureTransform(OctaneBaseSocket):
    bl_idname="OctaneNoiseTextureTransform"
    bl_label="UVW transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type="OctaneTransformValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TRANSFORM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNoiseTextureProjection(OctaneBaseSocket):
    bl_idname="OctaneNoiseTextureProjection"
    bl_label="Projection"
    color=consts.OctanePinColor.Projection
    octane_default_node_type="OctaneXYZToUVW"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_PROJECTION)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNoiseTextureInvert(OctaneBaseSocket):
    bl_idname="OctaneNoiseTextureInvert"
    bl_label="Invert"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=83)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="Inert output")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNoiseTextureGamma(OctaneBaseSocket):
    bl_idname="OctaneNoiseTextureGamma"
    bl_label="Gamma"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=57)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Output gamma", min=0.010000, max=100.000000, soft_min=0.010000, soft_max=100.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNoiseTextureContrast(OctaneBaseSocket):
    bl_idname="OctaneNoiseTextureContrast"
    bl_label="Contrast"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=26)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.001000, update=None, description="Output contrast", min=0.001000, max=1000.000000, soft_min=0.001000, soft_max=1000.000000, step=1, precision=3, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNoiseTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneNoiseTexture"
    bl_label="Noise texture"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=87)
    octane_socket_list: StringProperty(name="Socket List", default="Noise type;Octaves;Omega;UVW transform;Projection;Invert;Gamma;Contrast;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=8)

    def init(self, context):
        self.inputs.new("OctaneNoiseTextureNoiseType", OctaneNoiseTextureNoiseType.bl_label).init()
        self.inputs.new("OctaneNoiseTextureOctaves", OctaneNoiseTextureOctaves.bl_label).init()
        self.inputs.new("OctaneNoiseTextureOmega", OctaneNoiseTextureOmega.bl_label).init()
        self.inputs.new("OctaneNoiseTextureTransform", OctaneNoiseTextureTransform.bl_label).init()
        self.inputs.new("OctaneNoiseTextureProjection", OctaneNoiseTextureProjection.bl_label).init()
        self.inputs.new("OctaneNoiseTextureInvert", OctaneNoiseTextureInvert.bl_label).init()
        self.inputs.new("OctaneNoiseTextureGamma", OctaneNoiseTextureGamma.bl_label).init()
        self.inputs.new("OctaneNoiseTextureContrast", OctaneNoiseTextureContrast.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_classes=[
    OctaneNoiseTextureNoiseType,
    OctaneNoiseTextureOctaves,
    OctaneNoiseTextureOmega,
    OctaneNoiseTextureTransform,
    OctaneNoiseTextureProjection,
    OctaneNoiseTextureInvert,
    OctaneNoiseTextureGamma,
    OctaneNoiseTextureContrast,
    OctaneNoiseTexture,
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
