##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneMoireMosaicShape(OctaneBaseSocket):
    bl_idname="OctaneMoireMosaicShape"
    bl_label="Shape"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=608)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Rectangle", "Rectangle", "", 0),
        ("Circle", "Circle", "", 1),
        ("Ring", "Ring", "", 2),
        ("Frame", "Frame", "", 3),
    ]
    default_value: EnumProperty(default="Ring", update=None, description="The type of the generated shapes", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMoireMosaicSize(OctaneBaseSocket):
    bl_idname="OctaneMoireMosaicSize"
    bl_label="Size"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=216)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.750000, update=None, description="The width/height or radius of the generated shapes", min=0.000000, max=4.000000, soft_min=0.000000, soft_max=4.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMoireMosaicRadius(OctaneBaseSocket):
    bl_idname="OctaneMoireMosaicRadius"
    bl_label="Corner radius"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=142)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.100000, update=None, description="The corner radius (frame shape)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMoireMosaicBlur(OctaneBaseSocket):
    bl_idname="OctaneMoireMosaicBlur"
    bl_label="Blur"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=715)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.100000, update=None, description="The blurriness of the lines (circle and ring shapes)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMoireMosaicShift(OctaneBaseSocket):
    bl_idname="OctaneMoireMosaicShift"
    bl_label="Shift"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=214)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.750000, update=None, description="A horizontal shift applied to alternating rows (rectangle and circle shapes)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMoireMosaicSpacing(OctaneBaseSocket):
    bl_idname="OctaneMoireMosaicSpacing"
    bl_label="Ring spacing"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=717)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT2)
    default_value: FloatVectorProperty(default=(4.000000, 4.000000), update=None, description="The horizontal and vertical spacing between rings (ring and frame shapes)", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMoireMosaicIterationCount(OctaneBaseSocket):
    bl_idname="OctaneMoireMosaicIterationCount"
    bl_label="Iteration count"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=718)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=4, update=None, description="The number of iterations used by the shape generator (ring and frame shapes)", min=1, max=4, soft_min=1, soft_max=4, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMoireMosaicTime(OctaneBaseSocket):
    bl_idname="OctaneMoireMosaicTime"
    bl_label="Time"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=241)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.250000, update=None, description="The time in the generation sequence (ring and frame shapes)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMoireMosaicTransform(OctaneBaseSocket):
    bl_idname="OctaneMoireMosaicTransform"
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

class OctaneMoireMosaicProjection(OctaneBaseSocket):
    bl_idname="OctaneMoireMosaicProjection"
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

class OctaneMoireMosaic(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneMoireMosaic"
    bl_label="Moire mosaic"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=264)
    octane_socket_list: StringProperty(name="Socket List", default="Shape;Size;Corner radius;Blur;Shift;Ring spacing;Iteration count;Time;UV transform;Projection;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=10)

    def init(self, context):
        self.inputs.new("OctaneMoireMosaicShape", OctaneMoireMosaicShape.bl_label).init()
        self.inputs.new("OctaneMoireMosaicSize", OctaneMoireMosaicSize.bl_label).init()
        self.inputs.new("OctaneMoireMosaicRadius", OctaneMoireMosaicRadius.bl_label).init()
        self.inputs.new("OctaneMoireMosaicBlur", OctaneMoireMosaicBlur.bl_label).init()
        self.inputs.new("OctaneMoireMosaicShift", OctaneMoireMosaicShift.bl_label).init()
        self.inputs.new("OctaneMoireMosaicSpacing", OctaneMoireMosaicSpacing.bl_label).init()
        self.inputs.new("OctaneMoireMosaicIterationCount", OctaneMoireMosaicIterationCount.bl_label).init()
        self.inputs.new("OctaneMoireMosaicTime", OctaneMoireMosaicTime.bl_label).init()
        self.inputs.new("OctaneMoireMosaicTransform", OctaneMoireMosaicTransform.bl_label).init()
        self.inputs.new("OctaneMoireMosaicProjection", OctaneMoireMosaicProjection.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_classes=[
    OctaneMoireMosaicShape,
    OctaneMoireMosaicSize,
    OctaneMoireMosaicRadius,
    OctaneMoireMosaicBlur,
    OctaneMoireMosaicShift,
    OctaneMoireMosaicSpacing,
    OctaneMoireMosaicIterationCount,
    OctaneMoireMosaicTime,
    OctaneMoireMosaicTransform,
    OctaneMoireMosaicProjection,
    OctaneMoireMosaic,
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
