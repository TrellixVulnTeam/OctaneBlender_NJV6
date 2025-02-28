##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctanePlanetaryEnvironmentSundir(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentSundir"
    bl_label="Sun direction"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneSunDirection"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=231)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(1.000000, 0.800000, 0.000000), update=None, description="Vector which defines the direction from which the sun is shining", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="DIRECTION", size=3)
    octane_hide_value=False
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentTurbidity(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentTurbidity"
    bl_label="Sky turbidity"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=246)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=2.400000, update=None, description="Sky turbidity, i.e. the amount of sun light that is scattered. A high value will reduce the contrast between objects in the shadow and in sun light", min=2.000000, max=15.000000, soft_min=2.000000, soft_max=15.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentPower(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentPower"
    bl_label="Power"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=138)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Scale factor that is applied to the sun and sky", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentSunIntensity(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentSunIntensity"
    bl_label="Sun intensity"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=514)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Scale factor that is applied to the sun only. Use this to adjust the relative power of the sun compared to the sky.\n\nNote: values other than 1.0 can produce unrealistic results because in the real world the sky is lit by the sun. Adjusting the balance between the yellowish sun and the bluish sky can also produce a hue shift in the scene", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=8000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentNorthoffset(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentNorthoffset"
    bl_label="North offset"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=120)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="Additional rotation offset on longitude", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentSunSize(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentSunSize"
    bl_label="Sun size"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=233)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Size of the sun given as a factor of the actual sun diameter (which is ~0.5 degree)", min=0.100000, max=30.000000, soft_min=0.100000, soft_max=30.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentPlanetaryAltitude(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentPlanetaryAltitude"
    bl_label="Altitude"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=401)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="The camera altitude", min=0.100000, max=340282346638528859811704183484516925440.000000, soft_min=0.100000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentPlanetaryStarField(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentPlanetaryStarField"
    bl_label="Star field"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=407)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentImportanceSampling(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentImportanceSampling"
    bl_label="Importance sampling"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=79)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="Use importance sampling for image textures")
    octane_hide_value=False
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentMedium(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentMedium"
    bl_label="Medium"
    color=consts.OctanePinColor.Medium
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=110)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_MEDIUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentMediumRadius(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentMediumRadius"
    bl_label="Medium radius"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=269)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Radius of the environment medium. The environment medium acts as a sphere around the camera position with the specified radius", min=0.000100, max=10000000000.000000, soft_min=0.000100, soft_max=10000000000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentLightPassMask(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentLightPassMask"
    bl_label="Medium light pass mask"
    color=consts.OctanePinColor.BitMask
    octane_default_node_type="OctaneBitValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=433)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BIT_MASK)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=11000002
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentLatitude(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentLatitude"
    bl_label="Latitude"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=91)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="Latitude coordinate where we are currently positioned", min=-90.000000, max=90.000000, soft_min=-90.000000, soft_max=90.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=4010000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentLongitude(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentLongitude"
    bl_label="Longitude"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=99)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="Longitude coordinate where we are currently positioned", min=-180.000000, max=180.000000, soft_min=-180.000000, soft_max=180.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=4010000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentPlanetaryDiffuse(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentPlanetaryDiffuse"
    bl_label="Ground albedo"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneRGBColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=402)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(0.031928, 0.130434, 0.557292), update=None, description="Surface texture map on the planet", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentPlanetarySpecular(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentPlanetarySpecular"
    bl_label="Ground reflection"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=403)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentPlanetaryGlossiness(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentPlanetaryGlossiness"
    bl_label="Ground glossiness"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=406)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentPlanetaryEmission(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentPlanetaryEmission"
    bl_label="Ground emission"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneRGBColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=412)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=None, description="Surface texture map on the planet at night time", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=4000007
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentPlanetaryNormal(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentPlanetaryNormal"
    bl_label="Ground normal map"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=404)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentPlanetaryElevation(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentPlanetaryElevation"
    bl_label="Ground elevation"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=408)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentVisibleEnvironmentBackplate(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentVisibleEnvironmentBackplate"
    bl_label="Backplate"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=317)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="When used as a visible environment, this environment will behave as a backplate image")
    octane_hide_value=False
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentVisibleEnvironmentReflections(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentVisibleEnvironmentReflections"
    bl_label="Reflections"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=318)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="When used as a visible environment, this environment will be visible in reflections (specular and glossy materials)")
    octane_hide_value=False
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentVisibleEnvironmentRefractions(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentVisibleEnvironmentRefractions"
    bl_label="Refractions"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=319)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="When used as a visible environment, this environment will be visible in refractions")
    octane_hide_value=False
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentPlanetaryAxis(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentPlanetaryAxis"
    bl_label="Planetary axis"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=400)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 1.000000), update=None, description="(deprecated) The rotational axis of the planet running through the North and South pole", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="NONE", size=3)
    octane_hide_value=False
    octane_min_version=4000003
    octane_end_version=4010000
    octane_deprecated=True

class OctanePlanetaryEnvironmentPlanetaryAngle(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentPlanetaryAngle"
    bl_label="Planetary angle"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=399)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="(deprecated) The rotation around the planetary axis", min=-3.141593, max=3.141593, soft_min=-3.141593, soft_max=3.141593, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=4000003
    octane_end_version=4010000
    octane_deprecated=True

class OctanePlanetaryEnvironmentGroupPlanetarySurface(OctaneGroupTitleSocket):
    bl_idname="OctanePlanetaryEnvironmentGroupPlanetarySurface"
    bl_label="[OctaneGroupTitle]Planetary surface"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Ground albedo;Ground reflection;Ground glossiness;Ground emission;Ground normal map;Ground elevation;")

class OctanePlanetaryEnvironmentGroupVisibleEnvironment(OctaneGroupTitleSocket):
    bl_idname="OctanePlanetaryEnvironmentGroupVisibleEnvironment"
    bl_label="[OctaneGroupTitle]Visible environment"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Backplate;Reflections;Refractions;")

class OctanePlanetaryEnvironment(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctanePlanetaryEnvironment"
    bl_label="Planetary environment"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=129)
    octane_socket_list: StringProperty(name="Socket List", default="Sun direction;Sky turbidity;Power;Sun intensity;North offset;Sun size;Altitude;Star field;Importance sampling;Medium;Medium radius;Medium light pass mask;Latitude;Longitude;Ground albedo;Ground reflection;Ground glossiness;Ground emission;Ground normal map;Ground elevation;Backplate;Reflections;Refractions;Planetary axis;Planetary angle;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=25)

    def init(self, context):
        self.inputs.new("OctanePlanetaryEnvironmentSundir", OctanePlanetaryEnvironmentSundir.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentTurbidity", OctanePlanetaryEnvironmentTurbidity.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentPower", OctanePlanetaryEnvironmentPower.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentSunIntensity", OctanePlanetaryEnvironmentSunIntensity.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentNorthoffset", OctanePlanetaryEnvironmentNorthoffset.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentSunSize", OctanePlanetaryEnvironmentSunSize.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentPlanetaryAltitude", OctanePlanetaryEnvironmentPlanetaryAltitude.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentPlanetaryStarField", OctanePlanetaryEnvironmentPlanetaryStarField.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentImportanceSampling", OctanePlanetaryEnvironmentImportanceSampling.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentMedium", OctanePlanetaryEnvironmentMedium.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentMediumRadius", OctanePlanetaryEnvironmentMediumRadius.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentLightPassMask", OctanePlanetaryEnvironmentLightPassMask.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentLatitude", OctanePlanetaryEnvironmentLatitude.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentLongitude", OctanePlanetaryEnvironmentLongitude.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentGroupPlanetarySurface", OctanePlanetaryEnvironmentGroupPlanetarySurface.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentPlanetaryDiffuse", OctanePlanetaryEnvironmentPlanetaryDiffuse.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentPlanetarySpecular", OctanePlanetaryEnvironmentPlanetarySpecular.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentPlanetaryGlossiness", OctanePlanetaryEnvironmentPlanetaryGlossiness.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentPlanetaryEmission", OctanePlanetaryEnvironmentPlanetaryEmission.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentPlanetaryNormal", OctanePlanetaryEnvironmentPlanetaryNormal.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentPlanetaryElevation", OctanePlanetaryEnvironmentPlanetaryElevation.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentGroupVisibleEnvironment", OctanePlanetaryEnvironmentGroupVisibleEnvironment.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentVisibleEnvironmentBackplate", OctanePlanetaryEnvironmentVisibleEnvironmentBackplate.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentVisibleEnvironmentReflections", OctanePlanetaryEnvironmentVisibleEnvironmentReflections.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentVisibleEnvironmentRefractions", OctanePlanetaryEnvironmentVisibleEnvironmentRefractions.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentPlanetaryAxis", OctanePlanetaryEnvironmentPlanetaryAxis.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentPlanetaryAngle", OctanePlanetaryEnvironmentPlanetaryAngle.bl_label).init()
        self.outputs.new("OctaneEnvironmentOutSocket", "Environment out").init()


_classes=[
    OctanePlanetaryEnvironmentSundir,
    OctanePlanetaryEnvironmentTurbidity,
    OctanePlanetaryEnvironmentPower,
    OctanePlanetaryEnvironmentSunIntensity,
    OctanePlanetaryEnvironmentNorthoffset,
    OctanePlanetaryEnvironmentSunSize,
    OctanePlanetaryEnvironmentPlanetaryAltitude,
    OctanePlanetaryEnvironmentPlanetaryStarField,
    OctanePlanetaryEnvironmentImportanceSampling,
    OctanePlanetaryEnvironmentMedium,
    OctanePlanetaryEnvironmentMediumRadius,
    OctanePlanetaryEnvironmentLightPassMask,
    OctanePlanetaryEnvironmentLatitude,
    OctanePlanetaryEnvironmentLongitude,
    OctanePlanetaryEnvironmentPlanetaryDiffuse,
    OctanePlanetaryEnvironmentPlanetarySpecular,
    OctanePlanetaryEnvironmentPlanetaryGlossiness,
    OctanePlanetaryEnvironmentPlanetaryEmission,
    OctanePlanetaryEnvironmentPlanetaryNormal,
    OctanePlanetaryEnvironmentPlanetaryElevation,
    OctanePlanetaryEnvironmentVisibleEnvironmentBackplate,
    OctanePlanetaryEnvironmentVisibleEnvironmentReflections,
    OctanePlanetaryEnvironmentVisibleEnvironmentRefractions,
    OctanePlanetaryEnvironmentPlanetaryAxis,
    OctanePlanetaryEnvironmentPlanetaryAngle,
    OctanePlanetaryEnvironmentGroupPlanetarySurface,
    OctanePlanetaryEnvironmentGroupVisibleEnvironment,
    OctanePlanetaryEnvironment,
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
