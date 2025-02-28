##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneDiffuseLayerDiffuse(OctaneBaseSocket):
    bl_idname="OctaneDiffuseLayerDiffuse"
    bl_label="Diffuse"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneRGBColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=30)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(0.700000, 0.700000, 0.700000), update=None, description="The diffuse color of the material", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDiffuseLayerTransmission(OctaneBaseSocket):
    bl_idname="OctaneDiffuseLayerTransmission"
    bl_label="Transmission"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=245)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDiffuseLayerBrdf(OctaneBaseSocket):
    bl_idname="OctaneDiffuseLayerBrdf"
    bl_label="BRDF Model"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=357)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Octane", "Octane", "", 0),
        ("Lambertian", "Lambertian", "", 1),
    ]
    default_value: EnumProperty(default="Octane", update=None, description="BRDF Model", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDiffuseLayerRoughness(OctaneBaseSocket):
    bl_idname="OctaneDiffuseLayerRoughness"
    bl_label="Roughness"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=204)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="Roughness of the diffuse layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDiffuseLayerBump(OctaneBaseSocket):
    bl_idname="OctaneDiffuseLayerBump"
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

class OctaneDiffuseLayerNormal(OctaneBaseSocket):
    bl_idname="OctaneDiffuseLayerNormal"
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

class OctaneDiffuseLayerOpacity(OctaneBaseSocket):
    bl_idname="OctaneDiffuseLayerOpacity"
    bl_label="Layer opacity"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=125)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Opacity channel controlling the transparency of the layer via greyscale texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDiffuseLayerGroupRoughness(OctaneGroupTitleSocket):
    bl_idname="OctaneDiffuseLayerGroupRoughness"
    bl_label="[OctaneGroupTitle]Roughness"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Roughness;")

class OctaneDiffuseLayerGroupGeometryProperties(OctaneGroupTitleSocket):
    bl_idname="OctaneDiffuseLayerGroupGeometryProperties"
    bl_label="[OctaneGroupTitle]Geometry Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Bump;Normal;")

class OctaneDiffuseLayerGroupLayerProperties(OctaneGroupTitleSocket):
    bl_idname="OctaneDiffuseLayerGroupLayerProperties"
    bl_label="[OctaneGroupTitle]Layer Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Layer opacity;")

class OctaneDiffuseLayer(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneDiffuseLayer"
    bl_label="Diffuse layer"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=140)
    octane_socket_list: StringProperty(name="Socket List", default="Diffuse;Transmission;BRDF Model;Roughness;Bump;Normal;Layer opacity;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=7)

    def init(self, context):
        self.inputs.new("OctaneDiffuseLayerDiffuse", OctaneDiffuseLayerDiffuse.bl_label).init()
        self.inputs.new("OctaneDiffuseLayerTransmission", OctaneDiffuseLayerTransmission.bl_label).init()
        self.inputs.new("OctaneDiffuseLayerBrdf", OctaneDiffuseLayerBrdf.bl_label).init()
        self.inputs.new("OctaneDiffuseLayerGroupRoughness", OctaneDiffuseLayerGroupRoughness.bl_label).init()
        self.inputs.new("OctaneDiffuseLayerRoughness", OctaneDiffuseLayerRoughness.bl_label).init()
        self.inputs.new("OctaneDiffuseLayerGroupGeometryProperties", OctaneDiffuseLayerGroupGeometryProperties.bl_label).init()
        self.inputs.new("OctaneDiffuseLayerBump", OctaneDiffuseLayerBump.bl_label).init()
        self.inputs.new("OctaneDiffuseLayerNormal", OctaneDiffuseLayerNormal.bl_label).init()
        self.inputs.new("OctaneDiffuseLayerGroupLayerProperties", OctaneDiffuseLayerGroupLayerProperties.bl_label).init()
        self.inputs.new("OctaneDiffuseLayerOpacity", OctaneDiffuseLayerOpacity.bl_label).init()
        self.outputs.new("OctaneMaterialLayerOutSocket", "Material layer out").init()


_classes=[
    OctaneDiffuseLayerDiffuse,
    OctaneDiffuseLayerTransmission,
    OctaneDiffuseLayerBrdf,
    OctaneDiffuseLayerRoughness,
    OctaneDiffuseLayerBump,
    OctaneDiffuseLayerNormal,
    OctaneDiffuseLayerOpacity,
    OctaneDiffuseLayerGroupRoughness,
    OctaneDiffuseLayerGroupGeometryProperties,
    OctaneDiffuseLayerGroupLayerProperties,
    OctaneDiffuseLayer,
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
