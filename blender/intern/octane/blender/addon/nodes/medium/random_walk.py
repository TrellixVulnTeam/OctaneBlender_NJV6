##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneRandomWalkScale(OctaneBaseSocket):
    bl_idname="OctaneRandomWalkScale"
    bl_label="Density"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=209)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=100.000000, update=None, description="Absorption and scattering scale", min=0.000100, max=10000.000000, soft_min=0.000100, soft_max=10000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRandomWalkRayMarchStepLength(OctaneBaseSocket):
    bl_idname="OctaneRandomWalkRayMarchStepLength"
    bl_label="Volume step length"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=274)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=4.000000, update=None, description="Step length that is used for marching through volumes", min=0.000010, max=1000.000000, soft_min=0.000010, soft_max=1000000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=5100002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRandomWalkShadowRayMarchStepLength(OctaneBaseSocket):
    bl_idname="OctaneRandomWalkShadowRayMarchStepLength"
    bl_label="Vol. shadow ray step length"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=496)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=4.000000, update=None, description="Step length that is used by the shadow ray for marching through volumes", min=0.000010, max=1000.000000, soft_min=0.000010, soft_max=1000000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=7000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRandomWalkUseRayStepLengthForShadowRays(OctaneBaseSocket):
    bl_idname="OctaneRandomWalkUseRayStepLengthForShadowRays"
    bl_label="Use Vol. step length for Vol. shadow ray step length"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=515)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="Uses Volume step length as Volume shadow ray step length as well")
    octane_hide_value=False
    octane_min_version=8000005
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRandomWalkDisplacement(OctaneBaseSocket):
    bl_idname="OctaneRandomWalkDisplacement"
    bl_label="Sample position displacement"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=34)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=7000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRandomWalkAlbedo(OctaneBaseSocket):
    bl_idname="OctaneRandomWalkAlbedo"
    bl_label="Albedo"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneRGBColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=409)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(0.500000, 0.500000, 0.500000), update=None, description="Scattering albedo. The coefficients are determined from this using the mean free  path", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRandomWalkRadius(OctaneBaseSocket):
    bl_idname="OctaneRandomWalkRadius"
    bl_label="Radius"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneRGBColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=142)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=None, description="Determines the depth that the light scatters in the medium", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRandomWalkBias(OctaneBaseSocket):
    bl_idname="OctaneRandomWalkBias"
    bl_label="Bias"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=489)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.500000, update=None, description="Bias of the subsurface scattering. Higher values use biased sampling, which usually gives better results for lower depth settings, and more speed for objects with low curvature", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRandomWalkLockStepLength(OctaneBaseSocket):
    bl_idname="OctaneRandomWalkLockStepLength"
    bl_label="Lock step length pins"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=500)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="Locks volume step length and shadow step length pins. So if the value of one is changed then the other one is also changed automatically")
    octane_hide_value=False
    octane_min_version=7000000
    octane_end_version=8000005
    octane_deprecated=True

class OctaneRandomWalk(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneRandomWalk"
    bl_label="Random walk"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=146)
    octane_socket_list: StringProperty(name="Socket List", default="Density;Volume step length;Vol. shadow ray step length;Use Vol. step length for Vol. shadow ray step length;Sample position displacement;Albedo;Radius;Bias;Lock step length pins;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=9)

    def init(self, context):
        self.inputs.new("OctaneRandomWalkScale", OctaneRandomWalkScale.bl_label).init()
        self.inputs.new("OctaneRandomWalkRayMarchStepLength", OctaneRandomWalkRayMarchStepLength.bl_label).init()
        self.inputs.new("OctaneRandomWalkShadowRayMarchStepLength", OctaneRandomWalkShadowRayMarchStepLength.bl_label).init()
        self.inputs.new("OctaneRandomWalkUseRayStepLengthForShadowRays", OctaneRandomWalkUseRayStepLengthForShadowRays.bl_label).init()
        self.inputs.new("OctaneRandomWalkDisplacement", OctaneRandomWalkDisplacement.bl_label).init()
        self.inputs.new("OctaneRandomWalkAlbedo", OctaneRandomWalkAlbedo.bl_label).init()
        self.inputs.new("OctaneRandomWalkRadius", OctaneRandomWalkRadius.bl_label).init()
        self.inputs.new("OctaneRandomWalkBias", OctaneRandomWalkBias.bl_label).init()
        self.inputs.new("OctaneRandomWalkLockStepLength", OctaneRandomWalkLockStepLength.bl_label).init()
        self.outputs.new("OctaneMediumOutSocket", "Medium out").init()


_classes=[
    OctaneRandomWalkScale,
    OctaneRandomWalkRayMarchStepLength,
    OctaneRandomWalkShadowRayMarchStepLength,
    OctaneRandomWalkUseRayStepLengthForShadowRays,
    OctaneRandomWalkDisplacement,
    OctaneRandomWalkAlbedo,
    OctaneRandomWalkRadius,
    OctaneRandomWalkBias,
    OctaneRandomWalkLockStepLength,
    OctaneRandomWalk,
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
