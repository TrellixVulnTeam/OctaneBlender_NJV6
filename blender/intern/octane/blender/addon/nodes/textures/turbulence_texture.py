##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneTurbulenceTexturePower(OctaneBaseSocket):
    bl_idname="OctaneTurbulenceTexturePower"
    bl_label="Power"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=138)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Power/brightness", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTurbulenceTextureOffset(OctaneBaseSocket):
    bl_idname="OctaneTurbulenceTextureOffset"
    bl_label="Offset"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=122)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="Coordinate offset", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTurbulenceTextureOctaves(OctaneBaseSocket):
    bl_idname="OctaneTurbulenceTextureOctaves"
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

class OctaneTurbulenceTextureOmega(OctaneBaseSocket):
    bl_idname="OctaneTurbulenceTextureOmega"
    bl_label="Omega"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=123)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.500000, update=None, description="Difference per octave interval", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTurbulenceTextureTransform(OctaneBaseSocket):
    bl_idname="OctaneTurbulenceTextureTransform"
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

class OctaneTurbulenceTextureProjection(OctaneBaseSocket):
    bl_idname="OctaneTurbulenceTextureProjection"
    bl_label="Projection"
    color=consts.OctanePinColor.Projection
    octane_default_node_type="OctaneXYZToUVW"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_PROJECTION)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=1210000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTurbulenceTextureTurbulence(OctaneBaseSocket):
    bl_idname="OctaneTurbulenceTextureTurbulence"
    bl_label="Use turbulence"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=247)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="On - turbulence. Off - regular noise")
    octane_hide_value=False
    octane_min_version=2100003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTurbulenceTextureInvert(OctaneBaseSocket):
    bl_idname="OctaneTurbulenceTextureInvert"
    bl_label="Invert"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=83)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="Invert output")
    octane_hide_value=False
    octane_min_version=2100003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTurbulenceTextureGamma(OctaneBaseSocket):
    bl_idname="OctaneTurbulenceTextureGamma"
    bl_label="Gamma"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=57)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Output gamma", min=0.010000, max=100.000000, soft_min=0.010000, soft_max=100.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=2100003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTurbulenceTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneTurbulenceTexture"
    bl_label="Turbulence texture"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=22)
    octane_socket_list: StringProperty(name="Socket List", default="Power;Offset;Octaves;Omega;UVW transform;Projection;Use turbulence;Invert;Gamma;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=9)

    def init(self, context):
        self.inputs.new("OctaneTurbulenceTexturePower", OctaneTurbulenceTexturePower.bl_label).init()
        self.inputs.new("OctaneTurbulenceTextureOffset", OctaneTurbulenceTextureOffset.bl_label).init()
        self.inputs.new("OctaneTurbulenceTextureOctaves", OctaneTurbulenceTextureOctaves.bl_label).init()
        self.inputs.new("OctaneTurbulenceTextureOmega", OctaneTurbulenceTextureOmega.bl_label).init()
        self.inputs.new("OctaneTurbulenceTextureTransform", OctaneTurbulenceTextureTransform.bl_label).init()
        self.inputs.new("OctaneTurbulenceTextureProjection", OctaneTurbulenceTextureProjection.bl_label).init()
        self.inputs.new("OctaneTurbulenceTextureTurbulence", OctaneTurbulenceTextureTurbulence.bl_label).init()
        self.inputs.new("OctaneTurbulenceTextureInvert", OctaneTurbulenceTextureInvert.bl_label).init()
        self.inputs.new("OctaneTurbulenceTextureGamma", OctaneTurbulenceTextureGamma.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_classes=[
    OctaneTurbulenceTexturePower,
    OctaneTurbulenceTextureOffset,
    OctaneTurbulenceTextureOctaves,
    OctaneTurbulenceTextureOmega,
    OctaneTurbulenceTextureTransform,
    OctaneTurbulenceTextureProjection,
    OctaneTurbulenceTextureTurbulence,
    OctaneTurbulenceTextureInvert,
    OctaneTurbulenceTextureGamma,
    OctaneTurbulenceTexture,
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
