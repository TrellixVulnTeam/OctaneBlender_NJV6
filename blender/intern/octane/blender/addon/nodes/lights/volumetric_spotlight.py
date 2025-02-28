##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneVolumetricSpotlightThrowDistance(OctaneBaseSocket):
    bl_idname="OctaneVolumetricSpotlightThrowDistance"
    bl_label="Throw distance"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=516)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumetricSpotlightConeWidth(OctaneBaseSocket):
    bl_idname="OctaneVolumetricSpotlightConeWidth"
    bl_label="Cone width"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=517)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.500000, update=None, description="", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumetricSpotlightMedium(OctaneBaseSocket):
    bl_idname="OctaneVolumetricSpotlightMedium"
    bl_label="Light medium"
    color=consts.OctanePinColor.Medium
    octane_default_node_type="OctaneScattering"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=110)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_MEDIUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumetricSpotlightEmitterMaterial(OctaneBaseSocket):
    bl_idname="OctaneVolumetricSpotlightEmitterMaterial"
    bl_label="Emitter material"
    color=consts.OctanePinColor.Material
    octane_default_node_type="OctaneDiffuseMaterial"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=518)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_MATERIAL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumetricSpotlightBarnDoorsMaterial(OctaneBaseSocket):
    bl_idname="OctaneVolumetricSpotlightBarnDoorsMaterial"
    bl_label="Barn doors material"
    color=consts.OctanePinColor.Material
    octane_default_node_type="OctaneDiffuseMaterial"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=519)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_MATERIAL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumetricSpotlightObjectLayer(OctaneBaseSocket):
    bl_idname="OctaneVolumetricSpotlightObjectLayer"
    bl_label="Object layer"
    color=consts.OctanePinColor.ObjectLayer
    octane_default_node_type="OctaneObjectLayer"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=328)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OBJECTLAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumetricSpotlightTransform(OctaneBaseSocket):
    bl_idname="OctaneVolumetricSpotlightTransform"
    bl_label="Light transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type="OctaneTransformValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TRANSFORM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumetricSpotlightEnableBarnDoors(OctaneBaseSocket):
    bl_idname="OctaneVolumetricSpotlightEnableBarnDoors"
    bl_label="Enable barn doors"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=520)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumetricSpotlightBarnDoorsSize(OctaneBaseSocket):
    bl_idname="OctaneVolumetricSpotlightBarnDoorsSize"
    bl_label="Barn doors size"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=521)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.080000, update=None, description="", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumetricSpotlightBarnDoor1Angle(OctaneBaseSocket):
    bl_idname="OctaneVolumetricSpotlightBarnDoor1Angle"
    bl_label="Barn door 1 angle"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=522)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.750000, update=None, description="", min=-340282346638528859811704183484516925440.000000, max=1.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumetricSpotlightBarnDoor2Angle(OctaneBaseSocket):
    bl_idname="OctaneVolumetricSpotlightBarnDoor2Angle"
    bl_label="Barn door 2 angle"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=523)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.750000, update=None, description="", min=-340282346638528859811704183484516925440.000000, max=1.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumetricSpotlightBarnDoor3Angle(OctaneBaseSocket):
    bl_idname="OctaneVolumetricSpotlightBarnDoor3Angle"
    bl_label="Barn door 3 angle"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=524)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.750000, update=None, description="", min=-340282346638528859811704183484516925440.000000, max=1.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumetricSpotlightBarnDoor4Angle(OctaneBaseSocket):
    bl_idname="OctaneVolumetricSpotlightBarnDoor4Angle"
    bl_label="Barn door 4 angle"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=525)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.750000, update=None, description="", min=-340282346638528859811704183484516925440.000000, max=1.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumetricSpotlightGroupBarnDoors(OctaneGroupTitleSocket):
    bl_idname="OctaneVolumetricSpotlightGroupBarnDoors"
    bl_label="[OctaneGroupTitle]Barn doors"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Enable barn doors;Barn doors size;Barn door 1 angle;Barn door 2 angle;Barn door 3 angle;Barn door 4 angle;")

class OctaneVolumetricSpotlight(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneVolumetricSpotlight"
    bl_label="Volumetric spotlight"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=152)
    octane_socket_list: StringProperty(name="Socket List", default="Throw distance;Cone width;Light medium;Emitter material;Barn doors material;Object layer;Light transform;Enable barn doors;Barn doors size;Barn door 1 angle;Barn door 2 angle;Barn door 3 angle;Barn door 4 angle;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=13)

    def init(self, context):
        self.inputs.new("OctaneVolumetricSpotlightThrowDistance", OctaneVolumetricSpotlightThrowDistance.bl_label).init()
        self.inputs.new("OctaneVolumetricSpotlightConeWidth", OctaneVolumetricSpotlightConeWidth.bl_label).init()
        self.inputs.new("OctaneVolumetricSpotlightMedium", OctaneVolumetricSpotlightMedium.bl_label).init()
        self.inputs.new("OctaneVolumetricSpotlightEmitterMaterial", OctaneVolumetricSpotlightEmitterMaterial.bl_label).init()
        self.inputs.new("OctaneVolumetricSpotlightBarnDoorsMaterial", OctaneVolumetricSpotlightBarnDoorsMaterial.bl_label).init()
        self.inputs.new("OctaneVolumetricSpotlightObjectLayer", OctaneVolumetricSpotlightObjectLayer.bl_label).init()
        self.inputs.new("OctaneVolumetricSpotlightTransform", OctaneVolumetricSpotlightTransform.bl_label).init()
        self.inputs.new("OctaneVolumetricSpotlightGroupBarnDoors", OctaneVolumetricSpotlightGroupBarnDoors.bl_label).init()
        self.inputs.new("OctaneVolumetricSpotlightEnableBarnDoors", OctaneVolumetricSpotlightEnableBarnDoors.bl_label).init()
        self.inputs.new("OctaneVolumetricSpotlightBarnDoorsSize", OctaneVolumetricSpotlightBarnDoorsSize.bl_label).init()
        self.inputs.new("OctaneVolumetricSpotlightBarnDoor1Angle", OctaneVolumetricSpotlightBarnDoor1Angle.bl_label).init()
        self.inputs.new("OctaneVolumetricSpotlightBarnDoor2Angle", OctaneVolumetricSpotlightBarnDoor2Angle.bl_label).init()
        self.inputs.new("OctaneVolumetricSpotlightBarnDoor3Angle", OctaneVolumetricSpotlightBarnDoor3Angle.bl_label).init()
        self.inputs.new("OctaneVolumetricSpotlightBarnDoor4Angle", OctaneVolumetricSpotlightBarnDoor4Angle.bl_label).init()
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out").init()


_classes=[
    OctaneVolumetricSpotlightThrowDistance,
    OctaneVolumetricSpotlightConeWidth,
    OctaneVolumetricSpotlightMedium,
    OctaneVolumetricSpotlightEmitterMaterial,
    OctaneVolumetricSpotlightBarnDoorsMaterial,
    OctaneVolumetricSpotlightObjectLayer,
    OctaneVolumetricSpotlightTransform,
    OctaneVolumetricSpotlightEnableBarnDoors,
    OctaneVolumetricSpotlightBarnDoorsSize,
    OctaneVolumetricSpotlightBarnDoor1Angle,
    OctaneVolumetricSpotlightBarnDoor2Angle,
    OctaneVolumetricSpotlightBarnDoor3Angle,
    OctaneVolumetricSpotlightBarnDoor4Angle,
    OctaneVolumetricSpotlightGroupBarnDoors,
    OctaneVolumetricSpotlight,
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
