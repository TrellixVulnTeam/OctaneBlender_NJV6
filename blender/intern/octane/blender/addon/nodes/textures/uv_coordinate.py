##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneUVCoordinateProjection(OctaneBaseSocket):
    bl_idname="OctaneUVCoordinateProjection"
    bl_label="Projection"
    color=consts.OctanePinColor.Projection
    octane_default_node_type="OctaneMeshUVProjection"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_PROJECTION)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUVCoordinateUVMax(OctaneBaseSocket):
    bl_idname="OctaneUVCoordinateUVMax"
    bl_label="UV max"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=250)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="UV coordinate value mapped to maximum intensity", min=0.000010, max=1000.000000, soft_min=0.000010, soft_max=1000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUVCoordinate(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneUVCoordinate"
    bl_label="UV coordinate"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=330)
    octane_socket_list: StringProperty(name="Socket List", default="Projection;UV max;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=2)

    def init(self, context):
        self.inputs.new("OctaneUVCoordinateProjection", OctaneUVCoordinateProjection.bl_label).init()
        self.inputs.new("OctaneUVCoordinateUVMax", OctaneUVCoordinateUVMax.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_classes=[
    OctaneUVCoordinateProjection,
    OctaneUVCoordinateUVMax,
    OctaneUVCoordinate,
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
