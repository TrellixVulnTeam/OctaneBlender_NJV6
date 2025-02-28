##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctanePolygonSideInvert(OctaneBaseSocket):
    bl_idname="OctanePolygonSideInvert"
    bl_label="Invert"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=83)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="If switched off, the front side is white and the back side is black. If switched on, the front side is black and the back side is white")
    octane_hide_value=False
    octane_min_version=2150000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePolygonSide(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctanePolygonSide"
    bl_label="Polygon side"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=89)
    octane_socket_list: StringProperty(name="Socket List", default="Invert;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=1)

    def init(self, context):
        self.inputs.new("OctanePolygonSideInvert", OctanePolygonSideInvert.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_classes=[
    OctanePolygonSideInvert,
    OctanePolygonSide,
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
