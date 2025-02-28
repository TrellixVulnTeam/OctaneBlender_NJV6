##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneDistortedMeshUVRotation(OctaneBaseSocket):
    bl_idname="OctaneDistortedMeshUVRotation"
    bl_label="Rotation"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=203)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="Amount of rotation applied to the UV, normalized to the rotation range.\nA value of 0 rotates the UV by the minimum value in the range, a value of 1 rotates the UV by the maximum value in the range", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDistortedMeshUVRotationRange(OctaneBaseSocket):
    bl_idname="OctaneDistortedMeshUVRotationRange"
    bl_label="Rotation range"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=641)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT2)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), update=None, description="Range of rotation, in degrees", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDistortedMeshUVScale(OctaneBaseSocket):
    bl_idname="OctaneDistortedMeshUVScale"
    bl_label="Scale"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=209)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="Amount of scaling applied to the UV, normalized to the scale range.\nA value of 0 scales the UV by the minimum value in the range, a value of 1 scales the UV by the maximum value in the range", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDistortedMeshUVScaleRange(OctaneBaseSocket):
    bl_idname="OctaneDistortedMeshUVScaleRange"
    bl_label="Scale range"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=642)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT2)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000), update=None, description="Range of scaling", min=0.001000, max=1000.000000, soft_min=0.001000, soft_max=1000.000000, step=1, subtype="NONE", size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDistortedMeshUVTranslation(OctaneBaseSocket):
    bl_idname="OctaneDistortedMeshUVTranslation"
    bl_label="Translation"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=244)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="Amount of translation applied to the UV, normalized to the translation range.\nA value of 0 translates the UV by the minimum value in the range, a value of 1 translates the UV by the maximum value in the range", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDistortedMeshUVTranslationRange(OctaneBaseSocket):
    bl_idname="OctaneDistortedMeshUVTranslationRange"
    bl_label="Translation range"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=643)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT2)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), update=None, description="Range of translation", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDistortedMeshUV(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneDistortedMeshUV"
    bl_label="Distorted mesh UV Projection"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=322)
    octane_socket_list: StringProperty(name="Socket List", default="Rotation;Rotation range;Scale;Scale range;Translation;Translation range;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=6)

    def init(self, context):
        self.inputs.new("OctaneDistortedMeshUVRotation", OctaneDistortedMeshUVRotation.bl_label).init()
        self.inputs.new("OctaneDistortedMeshUVRotationRange", OctaneDistortedMeshUVRotationRange.bl_label).init()
        self.inputs.new("OctaneDistortedMeshUVScale", OctaneDistortedMeshUVScale.bl_label).init()
        self.inputs.new("OctaneDistortedMeshUVScaleRange", OctaneDistortedMeshUVScaleRange.bl_label).init()
        self.inputs.new("OctaneDistortedMeshUVTranslation", OctaneDistortedMeshUVTranslation.bl_label).init()
        self.inputs.new("OctaneDistortedMeshUVTranslationRange", OctaneDistortedMeshUVTranslationRange.bl_label).init()
        self.outputs.new("OctaneProjectionOutSocket", "Projection out").init()


_classes=[
    OctaneDistortedMeshUVRotation,
    OctaneDistortedMeshUVRotationRange,
    OctaneDistortedMeshUVScale,
    OctaneDistortedMeshUVScaleRange,
    OctaneDistortedMeshUVTranslation,
    OctaneDistortedMeshUVTranslationRange,
    OctaneDistortedMeshUV,
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
