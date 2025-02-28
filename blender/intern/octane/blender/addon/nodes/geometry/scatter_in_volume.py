##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneScatterInVolumeInput1(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeInput1"
    bl_label="Scattered object 1"
    color=consts.OctanePinColor.Geometry
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=527)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_GEOMETRY)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeInput2(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeInput2"
    bl_label="Scattered object 2"
    color=consts.OctanePinColor.Geometry
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=528)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_GEOMETRY)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeInput3(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeInput3"
    bl_label="Scattered object 3"
    color=consts.OctanePinColor.Geometry
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=573)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_GEOMETRY)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeInput4(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeInput4"
    bl_label="Scattered object 4"
    color=consts.OctanePinColor.Geometry
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=574)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_GEOMETRY)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeInputSelectionMethod(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeInputSelectionMethod"
    bl_label="Object selection method"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=575)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Sequential", "Sequential", "", 0),
        ("Random", "Random", "", 1),
        ("Selection map", "Selection map", "", 2),
    ]
    default_value: EnumProperty(default="Sequential", update=None, description="The method used to select between source objects for each instance", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeInputSelectionSeed(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeInputSelectionSeed"
    bl_label="Object selection seed"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=576)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=0, update=None, description="Seed used to randomize the selection of source objects", min=0, max=2147483647, soft_min=0, soft_max=2147483647, step=1, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeInputSelectionMap(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeInputSelectionMap"
    bl_label="Object selection map"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=577)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeDimensions(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeDimensions"
    bl_label="Dimension"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=31)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT3)
    default_value: IntVectorProperty(default=(3, 3, 3), update=None, description="Number of instances along each dimension", min=1, max=1000, soft_min=1, soft_max=1000, step=1, subtype="NONE", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeOffset(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeOffset"
    bl_label="Offsets"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=122)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=None, description="Offset between instances along each dimension", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeShape(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeShape"
    bl_label="Shape"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=608)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Box", "Box", "", 0),
        ("Sphere", "Sphere", "", 1),
        ("Cylinder", "Cylinder", "", 2),
        ("Cone", "Cone", "", 3),
    ]
    default_value: EnumProperty(default="Box", update=None, description="", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeInstanceCullingMap(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeInstanceCullingMap"
    bl_label="Culling map"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=583)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeInstanceCullingValueMin(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeInstanceCullingValueMin"
    bl_label="Culling min"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=584)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="All instances in areas of the map that have a value below this threshold are removed", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeInstanceCullingValueMax(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeInstanceCullingValueMax"
    bl_label="Culling max"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=585)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="All instances in areas of the map that have a value above this threshold are removed", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeInstanceOrientationPriority(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeInstanceOrientationPriority"
    bl_label="Orientation priority"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=589)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Up", "Up", "", 0),
        ("Front", "Front", "", 1),
    ]
    default_value: EnumProperty(default="Up", update=None, description="If the up and front vector are not orthogonal, selects which one has priority", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeInstanceUpMode(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeInstanceUpMode"
    bl_label="Up direction mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=590)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Direction", "Direction", "", 0),
        ("Point", "Point", "", 1),
    ]
    default_value: EnumProperty(default="Direction", update=None, description="Selects between the use of a reference direction or a reference point", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeInstanceUpDirection(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeInstanceUpDirection"
    bl_label="Reference up direction"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=591)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(0.000000, 1.000000, 0.000000), update=None, description="When up mode is set to Direction, the reference up vector will point in this direction", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="DIRECTION", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeInstanceUpPoint(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeInstanceUpPoint"
    bl_label="Reference up point"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=592)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=None, description="When up mode is set to Point, the reference up vector will point towards this location", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeInstanceFrontMode(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeInstanceFrontMode"
    bl_label="Front direction mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=593)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Direction", "Direction", "", 0),
        ("Point", "Point", "", 1),
    ]
    default_value: EnumProperty(default="Direction", update=None, description="Selects between the use of a reference direction or a reference point", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeInstanceFrontDirection(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeInstanceFrontDirection"
    bl_label="Reference front direction"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=594)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 1.000000), update=None, description="When front mode is set to Direction, the reference front vector will point in this direction", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="DIRECTION", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeInstanceFrontPoint(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeInstanceFrontPoint"
    bl_label="Reference front point"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=595)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=None, description="When front mode is set to Point, the reference front vector will point towards this location", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeInstanceRotationMode(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeInstanceRotationMode"
    bl_label="Rotation mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=596)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Fixed", "Fixed", "", 0),
        ("Randomized with independent axes", "Randomized with independent axes", "", 1),
        ("Randomized with coupled axes", "Randomized with coupled axes", "", 2),
        ("Map", "Map", "", 3),
    ]
    default_value: EnumProperty(default="Fixed", update=None, description="", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeInstanceRotationMin(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeInstanceRotationMin"
    bl_label="Rotation min"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=597)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=None, description="Minimum rotation of the instance", min=-360.000000, max=360.000000, soft_min=-360.000000, soft_max=360.000000, step=1, subtype="NONE", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeInstanceRotationMax(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeInstanceRotationMax"
    bl_label="Rotation max"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=598)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=None, description="Maximum rotation of the instance", min=-360.000000, max=360.000000, soft_min=-360.000000, soft_max=360.000000, step=1, subtype="NONE", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeInstanceRotationStep(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeInstanceRotationStep"
    bl_label="Rotation step"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=609)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="When the rotation mode is random or map and this value is different from zero the values will be aliased to the nearest step", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeInstanceRotationMap(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeInstanceRotationMap"
    bl_label="Rotation map"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=599)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeInstanceScaleMode(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeInstanceScaleMode"
    bl_label="Scale mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=600)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Fixed", "Fixed", "", 0),
        ("Randomized with independent axes", "Randomized with independent axes", "", 1),
        ("Randomized with coupled axes", "Randomized with coupled axes", "", 2),
        ("Map", "Map", "", 3),
    ]
    default_value: EnumProperty(default="Fixed", update=None, description="", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeInstanceScaleMin(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeInstanceScaleMin"
    bl_label="Scale min"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=601)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=None, description="Minimum scale of the instance", min=0.001000, max=1000.000000, soft_min=0.001000, soft_max=1000.000000, step=1, subtype="NONE", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeInstanceScaleMax(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeInstanceScaleMax"
    bl_label="Scale max"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=602)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=None, description="Maximum scale of the instance", min=0.001000, max=1000.000000, soft_min=0.001000, soft_max=1000.000000, step=1, subtype="NONE", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeInstanceScaleStep(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeInstanceScaleStep"
    bl_label="Scale step"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=610)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="When the scale mode is random or map and this value is different from zero the values will be aliased to the nearest step", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeInstanceScaleMap(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeInstanceScaleMap"
    bl_label="Scale map"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=603)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeInstanceTranslationMode(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeInstanceTranslationMode"
    bl_label="Translation mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=604)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Fixed", "Fixed", "", 0),
        ("Randomized with independent axes", "Randomized with independent axes", "", 1),
        ("Randomized with coupled axes", "Randomized with coupled axes", "", 2),
        ("Map", "Map", "", 3),
    ]
    default_value: EnumProperty(default="Fixed", update=None, description="", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeInstanceTranslationMin(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeInstanceTranslationMin"
    bl_label="Translation min"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=605)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=None, description="Minimum translation of the instance", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeInstanceTranslationMax(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeInstanceTranslationMax"
    bl_label="Translation max"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=606)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=None, description="Maximum translation of the instance", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeInstanceTranslationStep(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeInstanceTranslationStep"
    bl_label="Translation step"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=611)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="When the translation mode is random or map and this value is different from zero the values will be aliased to the nearest step", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeInstanceTranslationMap(OctaneBaseSocket):
    bl_idname="OctaneScatterInVolumeInstanceTranslationMap"
    bl_label="Translation map"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=607)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterInVolumeGroupObjects(OctaneGroupTitleSocket):
    bl_idname="OctaneScatterInVolumeGroupObjects"
    bl_label="[OctaneGroupTitle]Objects"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Scattered object 1;Scattered object 2;Scattered object 3;Scattered object 4;Object selection method;Object selection seed;Object selection map;")

class OctaneScatterInVolumeGroupGrid(OctaneGroupTitleSocket):
    bl_idname="OctaneScatterInVolumeGroupGrid"
    bl_label="[OctaneGroupTitle]Grid"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Dimension;Offsets;")

class OctaneScatterInVolumeGroupShape(OctaneGroupTitleSocket):
    bl_idname="OctaneScatterInVolumeGroupShape"
    bl_label="[OctaneGroupTitle]Shape"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Shape;Culling map;Culling min;Culling max;")

class OctaneScatterInVolumeGroupInstanceOrientation(OctaneGroupTitleSocket):
    bl_idname="OctaneScatterInVolumeGroupInstanceOrientation"
    bl_label="[OctaneGroupTitle]Instance orientation"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Orientation priority;Up direction mode;Reference up direction;Reference up point;Front direction mode;Reference front direction;Reference front point;")

class OctaneScatterInVolumeGroupInstanceTransform(OctaneGroupTitleSocket):
    bl_idname="OctaneScatterInVolumeGroupInstanceTransform"
    bl_label="[OctaneGroupTitle]Instance transform"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Rotation mode;Rotation min;Rotation max;Rotation step;Rotation map;Scale mode;Scale min;Scale max;Scale step;Scale map;Translation mode;Translation min;Translation max;Translation step;Translation map;")

class OctaneScatterInVolume(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneScatterInVolume"
    bl_label="Scatter in volume"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=165)
    octane_socket_list: StringProperty(name="Socket List", default="Scattered object 1;Scattered object 2;Scattered object 3;Scattered object 4;Object selection method;Object selection seed;Object selection map;Dimension;Offsets;Shape;Culling map;Culling min;Culling max;Orientation priority;Up direction mode;Reference up direction;Reference up point;Front direction mode;Reference front direction;Reference front point;Rotation mode;Rotation min;Rotation max;Rotation step;Rotation map;Scale mode;Scale min;Scale max;Scale step;Scale map;Translation mode;Translation min;Translation max;Translation step;Translation map;")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_module_graph_storage;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="10;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=35)

    a_module_graph_storage: StringProperty(name="Module graph storage", default="", update=None, description="Data stored by the wrapped module node graph. Will be updated after every evaluation of the graph")

    def init(self, context):
        self.inputs.new("OctaneScatterInVolumeGroupObjects", OctaneScatterInVolumeGroupObjects.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeInput1", OctaneScatterInVolumeInput1.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeInput2", OctaneScatterInVolumeInput2.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeInput3", OctaneScatterInVolumeInput3.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeInput4", OctaneScatterInVolumeInput4.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeInputSelectionMethod", OctaneScatterInVolumeInputSelectionMethod.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeInputSelectionSeed", OctaneScatterInVolumeInputSelectionSeed.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeInputSelectionMap", OctaneScatterInVolumeInputSelectionMap.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeGroupGrid", OctaneScatterInVolumeGroupGrid.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeDimensions", OctaneScatterInVolumeDimensions.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeOffset", OctaneScatterInVolumeOffset.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeGroupShape", OctaneScatterInVolumeGroupShape.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeShape", OctaneScatterInVolumeShape.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeInstanceCullingMap", OctaneScatterInVolumeInstanceCullingMap.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeInstanceCullingValueMin", OctaneScatterInVolumeInstanceCullingValueMin.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeInstanceCullingValueMax", OctaneScatterInVolumeInstanceCullingValueMax.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeGroupInstanceOrientation", OctaneScatterInVolumeGroupInstanceOrientation.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeInstanceOrientationPriority", OctaneScatterInVolumeInstanceOrientationPriority.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeInstanceUpMode", OctaneScatterInVolumeInstanceUpMode.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeInstanceUpDirection", OctaneScatterInVolumeInstanceUpDirection.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeInstanceUpPoint", OctaneScatterInVolumeInstanceUpPoint.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeInstanceFrontMode", OctaneScatterInVolumeInstanceFrontMode.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeInstanceFrontDirection", OctaneScatterInVolumeInstanceFrontDirection.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeInstanceFrontPoint", OctaneScatterInVolumeInstanceFrontPoint.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeGroupInstanceTransform", OctaneScatterInVolumeGroupInstanceTransform.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeInstanceRotationMode", OctaneScatterInVolumeInstanceRotationMode.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeInstanceRotationMin", OctaneScatterInVolumeInstanceRotationMin.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeInstanceRotationMax", OctaneScatterInVolumeInstanceRotationMax.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeInstanceRotationStep", OctaneScatterInVolumeInstanceRotationStep.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeInstanceRotationMap", OctaneScatterInVolumeInstanceRotationMap.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeInstanceScaleMode", OctaneScatterInVolumeInstanceScaleMode.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeInstanceScaleMin", OctaneScatterInVolumeInstanceScaleMin.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeInstanceScaleMax", OctaneScatterInVolumeInstanceScaleMax.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeInstanceScaleStep", OctaneScatterInVolumeInstanceScaleStep.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeInstanceScaleMap", OctaneScatterInVolumeInstanceScaleMap.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeInstanceTranslationMode", OctaneScatterInVolumeInstanceTranslationMode.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeInstanceTranslationMin", OctaneScatterInVolumeInstanceTranslationMin.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeInstanceTranslationMax", OctaneScatterInVolumeInstanceTranslationMax.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeInstanceTranslationStep", OctaneScatterInVolumeInstanceTranslationStep.bl_label).init()
        self.inputs.new("OctaneScatterInVolumeInstanceTranslationMap", OctaneScatterInVolumeInstanceTranslationMap.bl_label).init()
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out").init()


_classes=[
    OctaneScatterInVolumeInput1,
    OctaneScatterInVolumeInput2,
    OctaneScatterInVolumeInput3,
    OctaneScatterInVolumeInput4,
    OctaneScatterInVolumeInputSelectionMethod,
    OctaneScatterInVolumeInputSelectionSeed,
    OctaneScatterInVolumeInputSelectionMap,
    OctaneScatterInVolumeDimensions,
    OctaneScatterInVolumeOffset,
    OctaneScatterInVolumeShape,
    OctaneScatterInVolumeInstanceCullingMap,
    OctaneScatterInVolumeInstanceCullingValueMin,
    OctaneScatterInVolumeInstanceCullingValueMax,
    OctaneScatterInVolumeInstanceOrientationPriority,
    OctaneScatterInVolumeInstanceUpMode,
    OctaneScatterInVolumeInstanceUpDirection,
    OctaneScatterInVolumeInstanceUpPoint,
    OctaneScatterInVolumeInstanceFrontMode,
    OctaneScatterInVolumeInstanceFrontDirection,
    OctaneScatterInVolumeInstanceFrontPoint,
    OctaneScatterInVolumeInstanceRotationMode,
    OctaneScatterInVolumeInstanceRotationMin,
    OctaneScatterInVolumeInstanceRotationMax,
    OctaneScatterInVolumeInstanceRotationStep,
    OctaneScatterInVolumeInstanceRotationMap,
    OctaneScatterInVolumeInstanceScaleMode,
    OctaneScatterInVolumeInstanceScaleMin,
    OctaneScatterInVolumeInstanceScaleMax,
    OctaneScatterInVolumeInstanceScaleStep,
    OctaneScatterInVolumeInstanceScaleMap,
    OctaneScatterInVolumeInstanceTranslationMode,
    OctaneScatterInVolumeInstanceTranslationMin,
    OctaneScatterInVolumeInstanceTranslationMax,
    OctaneScatterInVolumeInstanceTranslationStep,
    OctaneScatterInVolumeInstanceTranslationMap,
    OctaneScatterInVolumeGroupObjects,
    OctaneScatterInVolumeGroupGrid,
    OctaneScatterInVolumeGroupShape,
    OctaneScatterInVolumeGroupInstanceOrientation,
    OctaneScatterInVolumeGroupInstanceTransform,
    OctaneScatterInVolume,
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

OctaneScatterInVolumeInput1.octane_default_node_type = "ShaderNodeOctObjectData:OutGeo"
OctaneScatterInVolumeInput2.octane_default_node_type = "ShaderNodeOctObjectData:OutGeo"
OctaneScatterInVolumeInput3.octane_default_node_type = "ShaderNodeOctObjectData:OutGeo"
OctaneScatterInVolumeInput4.octane_default_node_type = "ShaderNodeOctObjectData:OutGeo"