##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneGlossyMaterialDiffuse(OctaneBaseSocket):
    bl_idname="OctaneGlossyMaterialDiffuse"
    bl_label="Diffuse"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneRGBColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=30)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(0.700000, 0.700000, 0.700000), update=None, description="Diffuse reflection channel", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGlossyMaterialSpecular(OctaneBaseSocket):
    bl_idname="OctaneGlossyMaterialSpecular"
    bl_label="Specular"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=222)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Specular reflection channel which behaves like a coating on top of the diffuse layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGlossyMaterialBrdf(OctaneBaseSocket):
    bl_idname="OctaneGlossyMaterialBrdf"
    bl_label="BRDF Model"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=357)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Octane", "Octane", "", 0),
        ("Beckmann", "Beckmann", "", 1),
        ("GGX", "GGX", "", 2),
        ("GGX (energy preserving)", "GGX (energy preserving)", "", 6),
        ("STD", "STD", "", 7),
        ("Ward", "Ward", "", 3),
    ]
    default_value: EnumProperty(default="Octane", update=None, description="BRDF Model", items=items)
    octane_hide_value=False
    octane_min_version=3080000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGlossyMaterialRoughness(OctaneBaseSocket):
    bl_idname="OctaneGlossyMaterialRoughness"
    bl_label="Roughness"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=204)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.063200, update=None, description="Roughness of the specular reflection channel", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGlossyMaterialAnisotropy(OctaneBaseSocket):
    bl_idname="OctaneGlossyMaterialAnisotropy"
    bl_label="Anisotropy"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=358)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="The anisotropy of the specular material, -1 is horizontal and 1 is vertical, 0 is isotropy", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=3080000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGlossyMaterialRotation(OctaneBaseSocket):
    bl_idname="OctaneGlossyMaterialRotation"
    bl_label="Rotation"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=203)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="Rotation of the anisotropic specular reflection channel", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=3080000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGlossyMaterialSpread(OctaneBaseSocket):
    bl_idname="OctaneGlossyMaterialSpread"
    bl_label="Spread"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=501)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.500000, update=None, description="The spread of the tail of the specular BSDF model (STD only) of the specular layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=11000007
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGlossyMaterialFilmwidth(OctaneBaseSocket):
    bl_idname="OctaneGlossyMaterialFilmwidth"
    bl_label="Film width"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=49)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="Thickness of the film coating", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGlossyMaterialFilmindex(OctaneBaseSocket):
    bl_idname="OctaneGlossyMaterialFilmindex"
    bl_label="Film IOR"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=48)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.450000, update=None, description="Index of refraction of the film coating", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGlossyMaterialSheen(OctaneBaseSocket):
    bl_idname="OctaneGlossyMaterialSheen"
    bl_label="Sheen"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneRGBColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=377)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=None, description="The sheen color of the material", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=3080008
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGlossyMaterialSheenRoughness(OctaneBaseSocket):
    bl_idname="OctaneGlossyMaterialSheenRoughness"
    bl_label="Sheen Roughness"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=387)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.200000, update=None, description="Roughness of the sheen channel", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=3080013
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGlossyMaterialIndex(OctaneBaseSocket):
    bl_idname="OctaneGlossyMaterialIndex"
    bl_label="Index of refraction"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=80)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.300000, update=None, description="Index of refraction controlling the Fresnel effect of the specular reflection", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGlossyMaterialOpacity(OctaneBaseSocket):
    bl_idname="OctaneGlossyMaterialOpacity"
    bl_label="Opacity"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=125)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Opacity channel controlling the transparency of the material via greyscale texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGlossyMaterialBump(OctaneBaseSocket):
    bl_idname="OctaneGlossyMaterialBump"
    bl_label="Bump"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=18)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGlossyMaterialNormal(OctaneBaseSocket):
    bl_idname="OctaneGlossyMaterialNormal"
    bl_label="Normal"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=119)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGlossyMaterialDisplacement(OctaneBaseSocket):
    bl_idname="OctaneGlossyMaterialDisplacement"
    bl_label="Displacement"
    color=consts.OctanePinColor.Displacement
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=34)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_DISPLACEMENT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=2000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGlossyMaterialSmooth(OctaneBaseSocket):
    bl_idname="OctaneGlossyMaterialSmooth"
    bl_label="Smooth"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=218)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="If disabled normal interpolation will be disabled and triangle meshes will appear \"facetted\"")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGlossyMaterialSmoothShadowTerminator(OctaneBaseSocket):
    bl_idname="OctaneGlossyMaterialSmoothShadowTerminator"
    bl_label="Smooth shadow terminator"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=731)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="If enabled self-intersecting shadow terminator for low polygon is smoothed according to the polygon's curvature")
    octane_hide_value=False
    octane_min_version=11000008
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGlossyMaterialRoundEdges(OctaneBaseSocket):
    bl_idname="OctaneGlossyMaterialRoundEdges"
    bl_label="Round edges"
    color=consts.OctanePinColor.RoundEdges
    octane_default_node_type="OctaneRoundEdges"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=467)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ROUND_EDGES)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=5100001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGlossyMaterialPriority(OctaneBaseSocket):
    bl_idname="OctaneGlossyMaterialPriority"
    bl_label="Priority"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=564)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=0, update=None, description="The material priority for this surface material", min=-100, max=100, soft_min=-100, soft_max=100, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=10020900
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGlossyMaterialCustomAov(OctaneBaseSocket):
    bl_idname="OctaneGlossyMaterialCustomAov"
    bl_label="Custom AOV"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=632)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("None", "None", "", 4096),
        ("Custom AOV 1", "Custom AOV 1", "", 0),
        ("Custom AOV 2", "Custom AOV 2", "", 1),
        ("Custom AOV 3", "Custom AOV 3", "", 2),
        ("Custom AOV 4", "Custom AOV 4", "", 3),
        ("Custom AOV 5", "Custom AOV 5", "", 4),
        ("Custom AOV 6", "Custom AOV 6", "", 5),
        ("Custom AOV 7", "Custom AOV 7", "", 6),
        ("Custom AOV 8", "Custom AOV 8", "", 7),
        ("Custom AOV 9", "Custom AOV 9", "", 8),
        ("Custom AOV 10", "Custom AOV 10", "", 9),
    ]
    default_value: EnumProperty(default="None", update=None, description="If a custom AOV is selected, it will write a mask to it where the material is visible", items=items)
    octane_hide_value=False
    octane_min_version=11000002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGlossyMaterialCustomAovChannel(OctaneBaseSocket):
    bl_idname="OctaneGlossyMaterialCustomAovChannel"
    bl_label="Custom AOV channel"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=633)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("All", "All", "", 0),
        ("Red", "Red", "", 1),
        ("Green", "Green", "", 2),
        ("Blue", "Blue", "", 3),
    ]
    default_value: EnumProperty(default="All", update=None, description="If a custom AOV is selected, the selected channel(s) will receive the mask", items=items)
    octane_hide_value=False
    octane_min_version=11000002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGlossyMaterialLayer(OctaneBaseSocket):
    bl_idname="OctaneGlossyMaterialLayer"
    bl_label="Material layer"
    color=consts.OctanePinColor.MaterialLayer
    octane_default_node_type="OctaneMaterialLayerGroup"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=474)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_MATERIAL_LAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=5100002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGlossyMaterialEdgesRounding(OctaneBaseSocket):
    bl_idname="OctaneGlossyMaterialEdgesRounding"
    bl_label="Rounded edges radius"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=39)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="(deprecated) Radius of rounded edges that are rendered as shading effect", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=100.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=2000000
    octane_end_version=5100001
    octane_deprecated=True

class OctaneGlossyMaterialGroupRoughness(OctaneGroupTitleSocket):
    bl_idname="OctaneGlossyMaterialGroupRoughness"
    bl_label="[OctaneGroupTitle]Roughness"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Roughness;Anisotropy;Rotation;Spread;")

class OctaneGlossyMaterialGroupThinFilmLayer(OctaneGroupTitleSocket):
    bl_idname="OctaneGlossyMaterialGroupThinFilmLayer"
    bl_label="[OctaneGroupTitle]Thin Film Layer"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Film width;Film IOR;")

class OctaneGlossyMaterialGroupSheenLayer(OctaneGroupTitleSocket):
    bl_idname="OctaneGlossyMaterialGroupSheenLayer"
    bl_label="[OctaneGroupTitle]Sheen Layer"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Sheen;Sheen Roughness;")

class OctaneGlossyMaterialGroupIOR(OctaneGroupTitleSocket):
    bl_idname="OctaneGlossyMaterialGroupIOR"
    bl_label="[OctaneGroupTitle]IOR"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Index of refraction;")

class OctaneGlossyMaterialGroupTransmissionProperties(OctaneGroupTitleSocket):
    bl_idname="OctaneGlossyMaterialGroupTransmissionProperties"
    bl_label="[OctaneGroupTitle]Transmission Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Opacity;")

class OctaneGlossyMaterialGroupGeometryProperties(OctaneGroupTitleSocket):
    bl_idname="OctaneGlossyMaterialGroupGeometryProperties"
    bl_label="[OctaneGroupTitle]Geometry Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Bump;Normal;Displacement;Smooth;Smooth shadow terminator;Round edges;Priority;")

class OctaneGlossyMaterial(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneGlossyMaterial"
    bl_label="Glossy material"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=16)
    octane_socket_list: StringProperty(name="Socket List", default="Diffuse;Specular;BRDF Model;Roughness;Anisotropy;Rotation;Spread;Film width;Film IOR;Sheen;Sheen Roughness;Index of refraction;Opacity;Bump;Normal;Displacement;Smooth;Smooth shadow terminator;Round edges;Priority;Custom AOV;Custom AOV channel;Material layer;Rounded edges radius;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=24)

    def init(self, context):
        self.inputs.new("OctaneGlossyMaterialDiffuse", OctaneGlossyMaterialDiffuse.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialSpecular", OctaneGlossyMaterialSpecular.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialBrdf", OctaneGlossyMaterialBrdf.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialGroupRoughness", OctaneGlossyMaterialGroupRoughness.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialRoughness", OctaneGlossyMaterialRoughness.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialAnisotropy", OctaneGlossyMaterialAnisotropy.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialRotation", OctaneGlossyMaterialRotation.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialSpread", OctaneGlossyMaterialSpread.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialGroupThinFilmLayer", OctaneGlossyMaterialGroupThinFilmLayer.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialFilmwidth", OctaneGlossyMaterialFilmwidth.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialFilmindex", OctaneGlossyMaterialFilmindex.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialGroupSheenLayer", OctaneGlossyMaterialGroupSheenLayer.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialSheen", OctaneGlossyMaterialSheen.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialSheenRoughness", OctaneGlossyMaterialSheenRoughness.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialGroupIOR", OctaneGlossyMaterialGroupIOR.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialIndex", OctaneGlossyMaterialIndex.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialGroupTransmissionProperties", OctaneGlossyMaterialGroupTransmissionProperties.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialOpacity", OctaneGlossyMaterialOpacity.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialGroupGeometryProperties", OctaneGlossyMaterialGroupGeometryProperties.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialBump", OctaneGlossyMaterialBump.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialNormal", OctaneGlossyMaterialNormal.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialDisplacement", OctaneGlossyMaterialDisplacement.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialSmooth", OctaneGlossyMaterialSmooth.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialSmoothShadowTerminator", OctaneGlossyMaterialSmoothShadowTerminator.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialRoundEdges", OctaneGlossyMaterialRoundEdges.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialPriority", OctaneGlossyMaterialPriority.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialCustomAov", OctaneGlossyMaterialCustomAov.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialCustomAovChannel", OctaneGlossyMaterialCustomAovChannel.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialLayer", OctaneGlossyMaterialLayer.bl_label).init()
        self.inputs.new("OctaneGlossyMaterialEdgesRounding", OctaneGlossyMaterialEdgesRounding.bl_label).init()
        self.outputs.new("OctaneMaterialOutSocket", "Material out").init()


_classes=[
    OctaneGlossyMaterialDiffuse,
    OctaneGlossyMaterialSpecular,
    OctaneGlossyMaterialBrdf,
    OctaneGlossyMaterialRoughness,
    OctaneGlossyMaterialAnisotropy,
    OctaneGlossyMaterialRotation,
    OctaneGlossyMaterialSpread,
    OctaneGlossyMaterialFilmwidth,
    OctaneGlossyMaterialFilmindex,
    OctaneGlossyMaterialSheen,
    OctaneGlossyMaterialSheenRoughness,
    OctaneGlossyMaterialIndex,
    OctaneGlossyMaterialOpacity,
    OctaneGlossyMaterialBump,
    OctaneGlossyMaterialNormal,
    OctaneGlossyMaterialDisplacement,
    OctaneGlossyMaterialSmooth,
    OctaneGlossyMaterialSmoothShadowTerminator,
    OctaneGlossyMaterialRoundEdges,
    OctaneGlossyMaterialPriority,
    OctaneGlossyMaterialCustomAov,
    OctaneGlossyMaterialCustomAovChannel,
    OctaneGlossyMaterialLayer,
    OctaneGlossyMaterialEdgesRounding,
    OctaneGlossyMaterialGroupRoughness,
    OctaneGlossyMaterialGroupThinFilmLayer,
    OctaneGlossyMaterialGroupSheenLayer,
    OctaneGlossyMaterialGroupIOR,
    OctaneGlossyMaterialGroupTransmissionProperties,
    OctaneGlossyMaterialGroupGeometryProperties,
    OctaneGlossyMaterial,
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
