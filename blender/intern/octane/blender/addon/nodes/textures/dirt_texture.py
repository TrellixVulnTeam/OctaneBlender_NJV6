##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneDirtTextureStrength(OctaneBaseSocket):
    bl_idname="OctaneDirtTextureStrength"
    bl_label="Strength"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=230)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Strength", min=0.100000, max=10.000000, soft_min=0.100000, soft_max=10.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirtTextureDetails(OctaneBaseSocket):
    bl_idname="OctaneDirtTextureDetails"
    bl_label="Details"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=28)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="Details", min=0.000000, max=100.000000, soft_min=0.000000, soft_max=100.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirtTextureRadius(OctaneBaseSocket):
    bl_idname="OctaneDirtTextureRadius"
    bl_label="Radius"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=142)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Specifies the maximum area affected by the dirt effect", min=0.000010, max=100000.000000, soft_min=0.000010, soft_max=100000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirtTextureDirtMap(OctaneBaseSocket):
    bl_idname="OctaneDirtTextureDirtMap"
    bl_label="Radius map"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=502)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Determines the proportion of the maximum area affected by the dirt effect", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=8000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirtTextureTolerance(OctaneBaseSocket):
    bl_idname="OctaneDirtTextureTolerance"
    bl_label="Tolerance"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=242)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="Tolerance for small curvature and small angles between polygons", min=0.000000, max=0.300000, soft_min=0.000000, soft_max=0.300000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=2000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirtTextureSpread(OctaneBaseSocket):
    bl_idname="OctaneDirtTextureSpread"
    bl_label="Spread"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=501)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Spread controls the ray direction with respect to the normal of the surface. 0 means the dirt direction is shot straight in the direction of the surface normal, and 1 means the dirt rays are shot in all directions in the upper hemisphere in a cosine lobe", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=8000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirtTextureDistribution(OctaneBaseSocket):
    bl_idname="OctaneDirtTextureDistribution"
    bl_label="Distribution"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=37)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Distribution controls how evenly rays are shot within the sampling cone. When the value is 100, rays gather closer to the lateral surface. If the value is 1 rays are evenly distributed", min=1.000000, max=100.000000, soft_min=1.000000, soft_max=100.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=8000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirtTextureOffset(OctaneBaseSocket):
    bl_idname="OctaneDirtTextureOffset"
    bl_label="Bias"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=122)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 1.000000), update=None, description="The shading normal vector in shading space that we sample with as a custom direction. By default the direction is (0, 0, 1), which is the shading normal in shading coordinates. If any non-zero bias is set, then this bias vector is used as shading normal to sample dirt rays", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="NONE", size=3)
    octane_hide_value=False
    octane_min_version=8000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirtTextureDirtOffsetSpace(OctaneBaseSocket):
    bl_idname="OctaneDirtTextureDirtOffsetSpace"
    bl_label="Bias coordinate space"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=505)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("World space", "World space", "", 1),
        ("Object space", "Object space", "", 3),
        ("Normal space", "Normal space", "", 4),
    ]
    default_value: EnumProperty(default="Normal space", update=None, description="The coordinate space the bias vector is in", items=items)
    octane_hide_value=False
    octane_min_version=8000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirtTextureObjectIncludeMode(OctaneBaseSocket):
    bl_idname="OctaneDirtTextureObjectIncludeMode"
    bl_label="Include object mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=734)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("All", "All", "", 0),
        ("Self", "Self", "", 1),
        ("Others", "Others", "", 2),
    ]
    default_value: EnumProperty(default="All", update=None, description="Includes objects when calculating dirt value:  By default the selected mode is All, which includes all object intersections into calculating dirt. If Self is selected, then only self-intersection is taken into account for dirt. If Others is selected, then only ray-intersection with other objects is used for dirt", items=items)
    octane_hide_value=False
    octane_min_version=11000010
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirtTextureInvertNormal(OctaneBaseSocket):
    bl_idname="OctaneDirtTextureInvertNormal"
    bl_label="Invert normal"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=84)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="Invert normal")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirtTextureDirtGlobal(OctaneBaseSocket):
    bl_idname="OctaneDirtTextureDirtGlobal"
    bl_label="Dirt global"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=503)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("All", "All", "", 0),
        ("Self", "Self", "", 1),
        ("Others", "Others", "", 2),
    ]
    default_value: EnumProperty(default="All", update=None, description="(deprecated)", items=items)
    octane_hide_value=False
    octane_min_version=8000000
    octane_end_version=11000010
    octane_deprecated=True

class OctaneDirtTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneDirtTexture"
    bl_label="Dirt texture"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=63)
    octane_socket_list: StringProperty(name="Socket List", default="Strength;Details;Radius;Radius map;Tolerance;Spread;Distribution;Bias;Bias coordinate space;Include object mode;Invert normal;Dirt global;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=12)

    def init(self, context):
        self.inputs.new("OctaneDirtTextureStrength", OctaneDirtTextureStrength.bl_label).init()
        self.inputs.new("OctaneDirtTextureDetails", OctaneDirtTextureDetails.bl_label).init()
        self.inputs.new("OctaneDirtTextureRadius", OctaneDirtTextureRadius.bl_label).init()
        self.inputs.new("OctaneDirtTextureDirtMap", OctaneDirtTextureDirtMap.bl_label).init()
        self.inputs.new("OctaneDirtTextureTolerance", OctaneDirtTextureTolerance.bl_label).init()
        self.inputs.new("OctaneDirtTextureSpread", OctaneDirtTextureSpread.bl_label).init()
        self.inputs.new("OctaneDirtTextureDistribution", OctaneDirtTextureDistribution.bl_label).init()
        self.inputs.new("OctaneDirtTextureOffset", OctaneDirtTextureOffset.bl_label).init()
        self.inputs.new("OctaneDirtTextureDirtOffsetSpace", OctaneDirtTextureDirtOffsetSpace.bl_label).init()
        self.inputs.new("OctaneDirtTextureObjectIncludeMode", OctaneDirtTextureObjectIncludeMode.bl_label).init()
        self.inputs.new("OctaneDirtTextureInvertNormal", OctaneDirtTextureInvertNormal.bl_label).init()
        self.inputs.new("OctaneDirtTextureDirtGlobal", OctaneDirtTextureDirtGlobal.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_classes=[
    OctaneDirtTextureStrength,
    OctaneDirtTextureDetails,
    OctaneDirtTextureRadius,
    OctaneDirtTextureDirtMap,
    OctaneDirtTextureTolerance,
    OctaneDirtTextureSpread,
    OctaneDirtTextureDistribution,
    OctaneDirtTextureOffset,
    OctaneDirtTextureDirtOffsetSpace,
    OctaneDirtTextureObjectIncludeMode,
    OctaneDirtTextureInvertNormal,
    OctaneDirtTextureDirtGlobal,
    OctaneDirtTexture,
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
