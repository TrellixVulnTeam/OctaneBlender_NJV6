##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneVertexDisplacementMixer(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneVertexDisplacementMixer"
    bl_label="Vertex displacement mixer"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=151)
    octane_socket_list: StringProperty(name="Socket List", default="")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_displacement_count;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="2;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=0)

    a_displacement_count: IntProperty(name="Displacement count", default=0, update=None, description="The number of vertex displacements to mix")

    def init(self, context):
        self.outputs.new("OctaneDisplacementOutSocket", "Displacement out").init()


_classes=[
    OctaneVertexDisplacementMixer,
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
from ..base_socket import OctanePatternInput


class OctaneVertexDisplacementMixerBlendWeightMovableInput(OctanePatternInput):
    bl_idname="OctaneVertexDisplacementMixerBlendWeightMovableInput"
    bl_label="Blend weight"
    octane_input_pattern=r"Blend weight \d+"
    octane_input_format_pattern="Blend weight {}"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False


class OctaneVertexDisplacementMixerDisplacementMovableInput(OctaneMovableInput):
    bl_idname="OctaneVertexDisplacementMixerDisplacementMovableInput"
    bl_label="Displacement"
    octane_movable_input_count_attribute_name="a_displacement_count"
    octane_input_pattern=r"Displacement \d+"
    octane_input_format_pattern="Displacement {}"
    octane_sub_movable_inputs=[OctaneVertexDisplacementMixerBlendWeightMovableInput, ]
    color=consts.OctanePinColor.Displacement
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_DISPLACEMENT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneVertexDisplacementMixer_Override(OctaneVertexDisplacementMixer):
    MAX_DISPLACEMENT_COUNT = 16
    DEFAULT_DISPLACEMENT_COUNT = 2

    def init(self, context):
        super().init(context)
        self.init_movable_inputs(context, OctaneVertexDisplacementMixerDisplacementMovableInput, self.DEFAULT_DISPLACEMENT_COUNT)

    def draw_buttons(self, context, layout):
        self.draw_movable_inputs(context, layout, OctaneVertexDisplacementMixerDisplacementMovableInput, self.MAX_DISPLACEMENT_COUNT)


_added_classes = [OctaneVertexDisplacementMixerBlendWeightMovableInput, OctaneVertexDisplacementMixerDisplacementMovableInput, ]
_classes = _added_classes + _classes
utility.override_class(_classes, OctaneVertexDisplacementMixer, OctaneVertexDisplacementMixer_Override)   