##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneSunDirectionLatitude(OctaneBaseSocket):
    bl_idname="OctaneSunDirectionLatitude"
    bl_label="Latitude"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=91)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=-37.043659, update=None, description="Latitude of the location", min=-90.000000, max=90.000000, soft_min=-90.000000, soft_max=90.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSunDirectionLongitude(OctaneBaseSocket):
    bl_idname="OctaneSunDirectionLongitude"
    bl_label="Longitude"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=99)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=174.509171, update=None, description="Longitude of the location", min=-180.000000, max=180.000000, soft_min=-180.000000, soft_max=180.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSunDirectionMonth(OctaneBaseSocket):
    bl_idname="OctaneSunDirectionMonth"
    bl_label="Month"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=115)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=3, update=None, description="Month of the time the sun direction should be calculated for", min=1, max=12, soft_min=1, soft_max=12, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSunDirectionDay(OctaneBaseSocket):
    bl_idname="OctaneSunDirectionDay"
    bl_label="Day"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=27)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=1, update=None, description="Day of the month of the time the sun direction should be calculated for", min=1, max=31, soft_min=1, soft_max=31, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSunDirectionHour(OctaneBaseSocket):
    bl_idname="OctaneSunDirectionHour"
    bl_label="Local time"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=75)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=10.000000, update=None, description="The local time as hours since 0:00", min=0.000000, max=24.000000, soft_min=0.000000, soft_max=24.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSunDirectionGmtoffset(OctaneBaseSocket):
    bl_idname="OctaneSunDirectionGmtoffset"
    bl_label="GMT offset"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=67)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=12, update=None, description="The time zone as offset to GMT", min=-12, max=12, soft_min=-12, soft_max=12, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSunDirection(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneSunDirection"
    bl_label="Sun direction"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=30)
    octane_socket_list: StringProperty(name="Socket List", default="Latitude;Longitude;Month;Day;Local time;GMT offset;")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_value;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="8;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=6)

    a_value: FloatVectorProperty(name="Value", default=(0.617750, 0.703410, -0.351568), size=3, update=None, description="The direction calculated from the input pins of the node (normalized)")

    def init(self, context):
        self.inputs.new("OctaneSunDirectionLatitude", OctaneSunDirectionLatitude.bl_label).init()
        self.inputs.new("OctaneSunDirectionLongitude", OctaneSunDirectionLongitude.bl_label).init()
        self.inputs.new("OctaneSunDirectionMonth", OctaneSunDirectionMonth.bl_label).init()
        self.inputs.new("OctaneSunDirectionDay", OctaneSunDirectionDay.bl_label).init()
        self.inputs.new("OctaneSunDirectionHour", OctaneSunDirectionHour.bl_label).init()
        self.inputs.new("OctaneSunDirectionGmtoffset", OctaneSunDirectionGmtoffset.bl_label).init()
        self.outputs.new("OctaneFloatOutSocket", "Float out").init()


_classes=[
    OctaneSunDirectionLatitude,
    OctaneSunDirectionLongitude,
    OctaneSunDirectionMonth,
    OctaneSunDirectionDay,
    OctaneSunDirectionHour,
    OctaneSunDirectionGmtoffset,
    OctaneSunDirection,
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

from ...utils import utility

class OctaneSunDirection_Override(OctaneSunDirection):
    octane_attribute_list: StringProperty(name="Attribute List", default="")

utility.override_class(_classes, OctaneSunDirection, OctaneSunDirection_Override)  