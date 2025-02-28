##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneProceduralEffectsOperationType(OctaneBaseSocket):
    bl_idname="OctaneProceduralEffectsOperationType"
    bl_label="Type"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=613)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Combustible Voronoi", "Combustible Voronoi", "", 0),
        ("Fractal", "Fractal", "", 1),
        ("Kaleidoscope", "Kaleidoscope", "", 2),
        ("Neon stripes", "Neon stripes", "", 3),
        ("Paint colors", "Paint colors", "", 4),
        ("Particles", "Particles", "", 5),
        ("Star scroller", "Star scroller", "", 6),
        ("Wavey colors", "Wavey colors", "", 7),
    ]
    default_value: EnumProperty(default="Combustible Voronoi", update=None, description="The effect to generate", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneProceduralEffectsTime(OctaneBaseSocket):
    bl_idname="OctaneProceduralEffectsTime"
    bl_label="Time"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=241)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="The animation timestamp", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneProceduralEffectsTransform(OctaneBaseSocket):
    bl_idname="OctaneProceduralEffectsTransform"
    bl_label="UV transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type="OctaneTransformValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TRANSFORM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneProceduralEffectsProjection(OctaneBaseSocket):
    bl_idname="OctaneProceduralEffectsProjection"
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

class OctaneProceduralEffects(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneProceduralEffects"
    bl_label="Procedural effects"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=262)
    octane_socket_list: StringProperty(name="Socket List", default="Type;Time;UV transform;Projection;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=4)

    def init(self, context):
        self.inputs.new("OctaneProceduralEffectsOperationType", OctaneProceduralEffectsOperationType.bl_label).init()
        self.inputs.new("OctaneProceduralEffectsTime", OctaneProceduralEffectsTime.bl_label).init()
        self.inputs.new("OctaneProceduralEffectsTransform", OctaneProceduralEffectsTransform.bl_label).init()
        self.inputs.new("OctaneProceduralEffectsProjection", OctaneProceduralEffectsProjection.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_classes=[
    OctaneProceduralEffectsOperationType,
    OctaneProceduralEffectsTime,
    OctaneProceduralEffectsTransform,
    OctaneProceduralEffectsProjection,
    OctaneProceduralEffects,
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
