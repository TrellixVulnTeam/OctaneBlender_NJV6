##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneGaussianSpectrumWavelength(OctaneBaseSocket):
    bl_idname="OctaneGaussianSpectrumWavelength"
    bl_label="Wavelength"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=254)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.500000, update=None, description="Mean wavelength (380nm-720nm)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGaussianSpectrumWidth(OctaneBaseSocket):
    bl_idname="OctaneGaussianSpectrumWidth"
    bl_label="Width"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=256)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.100000, update=None, description="Standard deviation (0-800nm)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGaussianSpectrumPower(OctaneBaseSocket):
    bl_idname="OctaneGaussianSpectrumPower"
    bl_label="Power/brightness"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=138)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Power/brightness", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGaussianSpectrum(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneGaussianSpectrum"
    bl_label="Gaussian spectrum"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=32)
    octane_socket_list: StringProperty(name="Socket List", default="Wavelength;Width;Power/brightness;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=3)

    def init(self, context):
        self.inputs.new("OctaneGaussianSpectrumWavelength", OctaneGaussianSpectrumWavelength.bl_label).init()
        self.inputs.new("OctaneGaussianSpectrumWidth", OctaneGaussianSpectrumWidth.bl_label).init()
        self.inputs.new("OctaneGaussianSpectrumPower", OctaneGaussianSpectrumPower.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_classes=[
    OctaneGaussianSpectrumWavelength,
    OctaneGaussianSpectrumWidth,
    OctaneGaussianSpectrumPower,
    OctaneGaussianSpectrum,
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
