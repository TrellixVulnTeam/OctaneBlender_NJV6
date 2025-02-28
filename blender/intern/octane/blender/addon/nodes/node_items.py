import bpy
from bpy.props import IntProperty, StringProperty
import nodeitems_utils
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from ..utils import consts


def check_pin_type_compatible(octane_pin_type1, octane_pin_type2):
    if octane_pin_type1 == consts.PinType.PT_UNKNOWN:
        return True
    elif octane_pin_type2 == consts.PinType.PT_UNKNOWN:
        return True
    elif octane_pin_type1 == octane_pin_type2:
        return True
    else:
        return False

def render_aov_poll(context):
        return context.scene.render.engine == consts.ENGINE_NAME and \
            (not hasattr(context.space_data, "tree_type") or context.space_data.tree_type == consts.OctaneNodeTreeIDName.RENDER_AOV)

def composite_poll(context):
        return context.scene.render.engine == consts.ENGINE_NAME and \
            (not hasattr(context.space_data, "tree_type") or context.space_data.tree_type == consts.OctaneNodeTreeIDName.COMPOSITE)

def shader_poll(context):
        return context.scene.render.engine == consts.ENGINE_NAME and \
            (not hasattr(context.space_data, "tree_type") or context.space_data.tree_type == consts.OctaneNodeTreeIDName.BLENDER_SHADER)

class OctaneNodeItem(NodeItem):
    def __init__(self, nodetype, label=None, settings=None, poll=None, octane_pin_type=consts.PinType.PT_UNKNOWN):
        super().__init__(nodetype, label, settings, poll)
        self.octane_pin_type = octane_pin_type

    def is_pin_type_compatible(self, octane_pin_type):
        return check_pin_type_compatible(self.octane_pin_type, octane_pin_type)

    @staticmethod
    def draw(self, layout, _context):
        if _context.region.type == "HEADER":
            return NodeItem.draw(self, layout, _context)
        else:  
            op = layout.operator("octane.add_default_node_helper", text=self.label, text_ctxt=self.translation_context)
            op.node_type = self.nodetype


class OctaneNodeItemSeperator(object):
    def __init__(self, label, icon="TEXTURE"):
        self.label = label
        self.icon = icon

    @classmethod
    def poll(cls, context):
        return True

    @staticmethod
    def draw(self, layout, context):
        layout.label(text=self.label, icon=self.icon)


class OctaneNodeCategory(NodeCategory):
    NODE_TREE_ID_LIST = []

    def __init__(self, identifier, name, description="", items=None, octane_pin_type=consts.PinType.PT_UNKNOWN):
        super().__init__(identifier, name, description, items)
        self.octane_pin_type = octane_pin_type

    def is_pin_type_compatible(self, octane_pin_type):
        return check_pin_type_compatible(self.octane_pin_type, octane_pin_type)

    @classmethod
    def poll(cls, context):
        if context.scene.render.engine != consts.ENGINE_NAME:
            return False
        if not hasattr(context.space_data, "tree_type") or len(cls.NODE_TREE_ID_LIST) == 0:
            return True
        return context.space_data.tree_type in cls.NODE_TREE_ID_LIST



class OctaneGeneralNodeCategory(OctaneNodeCategory):
    pass


class OctaneOutputNodeCategory(OctaneNodeCategory):
    NODE_TREE_ID_LIST = [consts.OctaneNodeTreeIDName.COMPOSITE, consts.OctaneNodeTreeIDName.RENDER_AOV, ]


class OctaneTextureNodeCategory(OctaneNodeCategory):
    NODE_TREE_ID_LIST = [consts.OctaneNodeTreeIDName.BLENDER_SHADER, consts.OctaneNodeTreeIDName.BLENDER_TEXTURE, consts.OctaneNodeTreeIDName.RENDER_AOV, ]


class OctaneShaderNodeCategory(OctaneNodeCategory):
    NODE_TREE_ID_LIST = [consts.OctaneNodeTreeIDName.BLENDER_SHADER, ]


class OctaneCompositeNodeCategory(OctaneNodeCategory):
    NODE_TREE_ID_LIST = [consts.OctaneNodeTreeIDName.COMPOSITE, ]


class OctaneRenderAovNodeCategory(OctaneNodeCategory):
    NODE_TREE_ID_LIST = [consts.OctaneNodeTreeIDName.RENDER_AOV, ]


def register_octane_node_categories(identifier, cat_list):
    _node_categories = nodeitems_utils._node_categories
    if identifier in _node_categories:
        raise KeyError("Node categories list '%s' already registered" % identifier)
        return

    # works as draw function for menus
    def draw_node_item(self, context):
        octane_pin_type = getattr(self, "octane_pin_type", consts.PinType.PT_UNKNOWN)
        layout = self.layout
        col = layout.column()
        for item in self.category.items(context):
            if hasattr(item, "octane_pin_type"):
                if not item.is_pin_type_compatible(octane_pin_type):
                    continue
            if isinstance(item, NodeCategory):
                layout.menu("NODE_MT_category_%s" % item.identifier)
            else:
                item.draw(item, col, context)

    def draw_add_menu(self, context, octane_pin_type=consts.PinType.PT_UNKNOWN):
        layout = self.layout      
        for cat in cat_list:
            if cat.poll(context):
                if isinstance(cat, OctaneNodeCategory):
                    if cat.is_pin_type_compatible(octane_pin_type):
                        layout.menu("NODE_MT_category_%s" % cat.identifier)
                else:
                    layout.menu("NODE_MT_category_%s" % cat.identifier)


    def register_octane_node_category(menu_types, cat):
        menu_type = type("NODE_MT_category_" + cat.identifier, (bpy.types.Menu,), {
            "bl_space_type": 'NODE_EDITOR',
            "bl_label": cat.name,
            "category": cat,
            "poll": cat.poll,
            "draw": draw_node_item,
        })
        menu_types.append(menu_type)
        bpy.utils.register_class(menu_type)


    def register_submenu(menu_types, sub_cat_list, cat, octane_pin_type):
        if isinstance(cat, OctaneNodeItem):
            if getattr(cat, "octane_pin_type", consts.PinType.PT_UNKNOWN) == consts.PinType.PT_UNKNOWN:
                cat.octane_pin_type = octane_pin_type
            return
        sub_cat_list.append(cat)
        register_octane_node_category(menu_types, cat)
        for item in cat.items(None):
            register_submenu(menu_types, sub_cat_list, item, cat.octane_pin_type)

    menu_types = []
    sub_cat_list = []
    for cat in cat_list:
        register_submenu(menu_types, sub_cat_list, cat, cat.octane_pin_type)

    # stores: (categories list, menu draw function, submenu types)
    final_cat_list = []
    for cat in (cat_list + sub_cat_list):
        if cat not in final_cat_list:
            final_cat_list.append(cat)
    _node_categories[identifier] = (final_cat_list, draw_add_menu, menu_types)


def unregister_node_cat_types(cats):
    for mt in cats[2]:
        bpy.utils.unregister_class(mt)


def unregister_octane_node_categories(identifier=None):
    _node_categories = nodeitems_utils._node_categories
    # unregister existing UI classes
    if identifier:
        cat_types = _node_categories.get(identifier, None)
        if cat_types:
            unregister_node_cat_types(cat_types)
        del _node_categories[identifier]

    else:
        for cat_types in _node_categories.values():
            unregister_node_cat_types(cat_types)
        _node_categories.clear()


def draw_octane_node_categories_menu(self, context, octane_pin_type=consts.PinType.PT_UNKNOWN):
    _node_categories = nodeitems_utils._node_categories
    for cats in _node_categories.values():
        is_octane_node_category = False
        for cat in cats[0]:
            if isinstance(cat, OctaneNodeCategory):
                is_octane_node_category = True
                break        
        if is_octane_node_category:
            for menu in cats[2]:
                menu.octane_pin_type = octane_pin_type
            cats[1](self, context, octane_pin_type)        
        else:
            # Do not show Blender's menu under quick adding mode(octane_pin_type is assigned)
            if octane_pin_type == consts.PinType.PT_UNKNOWN:
                cats[1](self, context)


### Octane Nodes 

_octane_node_items = {
    "OCTANE_OUTPUT": [
        OctaneOutputNodeCategory("OCTANE_OUTPUT", "Octane Output", 
            octane_pin_type=consts.PinType.PT_BLENDER_OUTPUT,
            items=[
                OctaneNodeItem("OctaneAOVOutputGroupOutputNode", poll=composite_poll),
                OctaneNodeItem("OctaneRenderAOVsOutputNode", poll=render_aov_poll),   
            ]
        ),
    ],  
    # "OCTANE_INPUT": [
    #     OctaneOutputNodeCategory("OCTANE_INPUT", "Utility", 
    #         octane_pin_type=consts.PinType.PT_BLENDER_UTILITY,
    #         items=[
    #             OctaneNodeItem("ShaderNodeCameraData"),
    #             OctaneNodeItem("ShaderNodeOctObjectData"),   
    #         ]
    #     ),
    # ],  
    "OCTANE_VALUE": [
        OctaneGeneralNodeCategory("OCTANE_VALUE", "Octane Values", 
            octane_pin_type=consts.PinType.PT_BLENDER_VALUES,
            items=[
                OctaneNodeItem("OctaneBoolValue", octane_pin_type=consts.PinType.PT_BOOL),
                OctaneNodeItem("OctaneIntValue", octane_pin_type=consts.PinType.PT_INT),
                OctaneNodeItem("OctaneFloatValue", octane_pin_type=consts.PinType.PT_FLOAT),    
                OctaneNodeItem("OctaneStringValue", octane_pin_type=consts.PinType.PT_STRING),
                OctaneNodeItem("OctaneSunDirection"),    
            ]
        ),
    ],
    "OCTANE_DISPLACEMENT": [
        OctaneGeneralNodeCategory("OCTANE_DISPLACEMENT", "Octane Displacement", 
            octane_pin_type=consts.PinType.PT_DISPLACEMENT,
            items=[  
                OctaneNodeItem("OctaneTextureDisplacement"),
                OctaneNodeItem("OctaneVertexDisplacement"),
                OctaneNodeItem("OctaneVertexDisplacementMixer"),                
            ]
        ),
    ],    
    "OCTANE_PROJECTION": [
        OctaneGeneralNodeCategory("OCTANE_PROJECTION", "Octane Projection", 
            octane_pin_type=consts.PinType.PT_PROJECTION,
            items=[
                OctaneNodeItem("OctaneBox"),
                OctaneNodeItem("OctaneColorToUVW"),
                OctaneNodeItem("OctaneCylindrical"),
                OctaneNodeItem("OctaneDistortedMeshUV"),
                OctaneNodeItem("OctaneMatCap"),
                OctaneNodeItem("OctaneMeshUVProjection"),
                OctaneNodeItem("OctaneOSLDelayedUV"),
                # OctaneNodeItem("OctaneOSLProjection"),
                OctaneNodeItem("ShaderNodeOctOSLProjection", poll=shader_poll),
                OctaneNodeItem("OctanePerspective"),
                OctaneNodeItem("OctaneSamplePosToUV"),
                OctaneNodeItem("OctaneSpherical"),
                OctaneNodeItem("OctaneTriplanar"),
                OctaneNodeItem("OctaneXYZToUVW"),   
            ]
        ),
    ],
    "OCTANE_TRANSFORM": [
        OctaneGeneralNodeCategory("OCTANE_TRANSFORM", "Octane Transform", 
            octane_pin_type=consts.PinType.PT_TRANSFORM,
            items=[
                OctaneNodeItem("Octane2DTransformation"),
                OctaneNodeItem("Octane3DTransformation"),
                OctaneNodeItem("OctaneRotation"),
                OctaneNodeItem("OctaneScale"),
                OctaneNodeItem("OctaneTransformValue"),     
            ]
        ),
    ],
    "OCTANE_COMPOSITE": [
        OctaneCompositeNodeCategory("OCTANE_COMPOSITE", "Octane Compositor", 
            octane_pin_type=consts.PinType.PT_OUTPUT_AOV,
            items=[
                OctaneNodeItem("OctaneAOVOutputGroup", octane_pin_type=consts.PinType.PT_OUTPUT_AOV_GROUP),
                OctaneNodeItem("OctaneColorAOVOutput"),
                OctaneNodeItem("OctaneCompositeAOVOutput"),
                OctaneNodeItem("OctaneCompositeAOVOutputLayer", octane_pin_type=consts.PinType.PT_COMPOSITE_AOV_LAYER),
                OctaneNodeItem("ShaderNodeOctImageAovOutput"),
                OctaneNodeItem("OctaneRenderAOVOutput"),
                OctaneCompositeNodeCategory("OCTANE_COMPOSITE_OPERATORS", "Operators", 
                    octane_pin_type=consts.PinType.PT_OUTPUT_AOV,
                    items=[
                        OctaneNodeItem("OctaneClampAOVOutput"),
                        OctaneNodeItem("OctaneColorCorrectionAOVOutput"),
                        OctaneNodeItem("OctaneMapRangeAOVOutput"),
                    ]
                ), 
                OctaneCompositeNodeCategory("OCTANE_COMPOSITOR_UTILITY", "Utility", 
                    octane_pin_type=consts.PinType.PT_OUTPUT_AOV,
                    items=[
                        OctaneNodeItem("OctaneLightMixerAOVOutput"),
                    ]
                ), 
            ]        
        ),
    ],
    "OCTANE_RENDER_AOV": [
        OctaneRenderAovNodeCategory("OCTANE_RENDER_AOV", "Octane Render AOV", 
            octane_pin_type=consts.PinType.PT_RENDER_PASSES,
            items=[
                OctaneNodeItem("OctaneRenderAOVGroup"),
                OctaneRenderAovNodeCategory("OCTANE_RENDER_AOV_AUXILIARY", "Auxiliary",
                    octane_pin_type=consts.PinType.PT_RENDER_PASSES,
                    items=[
                        OctaneNodeItem("OctaneCryptomatteAOV"),
                        OctaneNodeItem("OctaneIrradianceAOV"),
                        OctaneNodeItem("OctaneLightDirectionAOV"),
                        OctaneNodeItem("OctaneNoiseAOV"),
                        OctaneNodeItem("OctanePostProcessingAOV"),
                        OctaneNodeItem("OctaneShadowAOV"),
                    ]
                ),
                OctaneRenderAovNodeCategory("OCTANE_RENDER_AOV_BEUATY_SURFACES", "Beauty - surfaces",
                    octane_pin_type=consts.PinType.PT_RENDER_PASSES,
                    items=[
                        OctaneNodeItem("OctaneDiffuseAOV"),
                        OctaneNodeItem("OctaneDiffuseDirectAOV"),
                        OctaneNodeItem("OctaneDiffuseFilterBeautyAOV"),
                        OctaneNodeItem("OctaneDiffuseIndirectAOV"),
                        OctaneNodeItem("OctaneEmittersAOV"),
                        OctaneNodeItem("OctaneEnvironmentAOV"),
                        OctaneNodeItem("OctaneReflectionAOV"),
                        OctaneNodeItem("OctaneReflectionDirectAOV"),
                        OctaneNodeItem("OctaneReflectionFilterBeautyAOV"),
                        OctaneNodeItem("OctaneReflectionIndirectAOV"),
                        OctaneNodeItem("OctaneRefractionAOV"),
                        OctaneNodeItem("OctaneRefractionFilterBeautyAOV"),
                        OctaneNodeItem("OctaneSubsurfaceScatteringAOV"),
                        OctaneNodeItem("OctaneTransmissionAOV"),
                        OctaneNodeItem("OctaneTransmissionFilterBeautyAOV"),
                    ]
                ),
                OctaneRenderAovNodeCategory("OCTANE_RENDER_AOV_BEUATY_VOLUMES", "Beauty - volumes",
                    octane_pin_type=consts.PinType.PT_RENDER_PASSES,
                    items=[
                        OctaneNodeItem("OctaneVolumeAOV"),
                        OctaneNodeItem("OctaneVolumeEmissionAOV"),
                        OctaneNodeItem("OctaneVolumeMaskAOV"),
                        OctaneNodeItem("OctaneVolumeZDepthBackAOV"),
                        OctaneNodeItem("OctaneVolumeZDepthFrontAOV"),
                    ]
                ), 
                OctaneRenderAovNodeCategory("OCTANE_RENDER_AOV_CUSTOM", "Custom",
                    octane_pin_type=consts.PinType.PT_RENDER_PASSES,
                    items=[
                        OctaneNodeItem("OctaneCustomAOV"),
                        OctaneNodeItem("OctaneGlobalTextureAOV"),
                    ]
                ),
                OctaneRenderAovNodeCategory("OCTANE_RENDER_AOV_DENOISED", "Denoised",
                    octane_pin_type=consts.PinType.PT_RENDER_PASSES,
                    items=[
                        OctaneNodeItem("OctaneDenoisedDiffuseDirectAOV"),
                        OctaneNodeItem("OctaneDenoisedDiffuseIndirectAOV"),
                        OctaneNodeItem("OctaneDenoisedEmissionAOV"),
                        OctaneNodeItem("OctaneDenoisedReflectionDirectAOV"),
                        OctaneNodeItem("OctaneDenoisedReflectionIndirectAOV"),
                        OctaneNodeItem("OctaneDenoisedRemainderAOV"),
                        OctaneNodeItem("OctaneDenoisedVolumeAOV"),
                        OctaneNodeItem("OctaneDenoisedVolumeEmissionAOV"),
                    ]
                ),
                OctaneRenderAovNodeCategory("OCTANE_RENDER_AOV_INFO", "Info",
                    octane_pin_type=consts.PinType.PT_RENDER_PASSES,
                    items=[
                        OctaneNodeItem("OctaneAmbientOcclusionAOV"),
                        OctaneNodeItem("OctaneBakingGroupIDAOV"),
                        OctaneNodeItem("OctaneDiffuseFilterInfoAOV"),
                        OctaneNodeItem("OctaneGeometricNormalAOV"),
                        OctaneNodeItem("OctaneIndexOfRefractionAOV"),
                        OctaneNodeItem("OctaneLightPassIDAOV"),
                        OctaneNodeItem("OctaneMaterialIDAOV"),
                        OctaneNodeItem("OctaneMotionVectorAOV"),
                        OctaneNodeItem("OctaneObjectIDAOV"),
                        OctaneNodeItem("OctaneObjectLayerColorAOV"),
                        OctaneNodeItem("OctaneOpacityAOV"),
                        OctaneNodeItem("OctanePositionAOV"),
                        OctaneNodeItem("OctaneReflectionFilterInfoAOV"),
                        OctaneNodeItem("OctaneRefractionFilterInfoAOV"),
                        OctaneNodeItem("OctaneRenderLayerIDAOV"),
                        OctaneNodeItem("OctaneRenderLayerMaskAOV"),
                        OctaneNodeItem("OctaneRoughnessAOV"),
                        OctaneNodeItem("OctaneShadingNormalAOV"),
                        OctaneNodeItem("OctaneSmoothNormalAOV"),
                        OctaneNodeItem("OctaneTangentNormalAOV"),
                        OctaneNodeItem("OctaneTextureTangentAOV"),
                        OctaneNodeItem("OctaneTransmissionFilterInfoAOV"),
                        OctaneNodeItem("OctaneUVCoordinatesAOV"),
                        OctaneNodeItem("OctaneWireframeAOV"),
                        OctaneNodeItem("OctaneZDepthAOV"),
                    ]
                ),
                OctaneRenderAovNodeCategory("OCTANE_RENDER_AOV_LIGHT", "Light",
                    octane_pin_type=consts.PinType.PT_RENDER_PASSES,
                    items=[
                        OctaneNodeItem("OctaneLightAOV"),
                        OctaneNodeItem("OctaneLightDirectAOV"),
                        OctaneNodeItem("OctaneLightIndirectAOV"),
                    ]
                ), 
                OctaneRenderAovNodeCategory("OCTANE_RENDER_AOV_RENDER_LAYER", "Render layer",
                    octane_pin_type=consts.PinType.PT_RENDER_PASSES,
                    items=[
                        OctaneNodeItem("OctaneBlackLayerShadowsAOV"),
                        OctaneNodeItem("OctaneLayerReflectionsAOV"),
                        OctaneNodeItem("OctaneLayerShadowsAOV"),
                    ]
                ),                                                          
            ]        
        ),
    ],
    "OCTANE_SHADER": [
        OctaneShaderNodeCategory("OCTANE_SHADER", "Octane Material", 
            octane_pin_type=consts.PinType.PT_MATERIAL,
            items=[
                OctaneNodeItem("OctaneClippingMaterial"),
                OctaneNodeItem("OctaneCompositeMaterial"),
                OctaneNodeItem("OctaneDiffuseMaterial"),
                OctaneNodeItem("OctaneGlossyMaterial"),
                OctaneNodeItem("OctaneHairMaterial"),
                OctaneNodeItem("OctaneLayeredMaterial"),
                OctaneNodeItem("OctaneMetallicMaterial"),
                OctaneNodeItem("OctaneMixMaterial"),
                OctaneNodeItem("OctaneNullMaterial"),
                OctaneNodeItem("OctanePortalMaterial"),
                OctaneNodeItem("OctaneShadowCatcherMaterial"),
                OctaneNodeItem("OctaneSpecularMaterial"),
                OctaneNodeItem("OctaneToonMaterial"),
                # OctaneNodeItem("OctaneToonRamp"),
                OctaneNodeItem("ShaderNodeOctToonRampTex", octane_pin_type=consts.PinType.PT_TOON_RAMP),       
                OctaneNodeItem("OctaneUniversalMaterial"),
            ]            
        ),
    ],
    "OCTANE_LAYER": [
        OctaneShaderNodeCategory("OCTANE_MATERIAL_LAYER", "Octane Material Layer", 
            octane_pin_type=consts.PinType.PT_MATERIAL_LAYER,
            items=[
                OctaneNodeItem("OctaneDiffuseLayer"),
                OctaneNodeItem("OctaneMaterialLayerGroup"),
                OctaneNodeItem("OctaneMetallicLayer"),
                OctaneNodeItem("OctaneSheenLayer"),
                OctaneNodeItem("OctaneSpecularLayer"),
            ]  
        ),
    ],    
    "OCTANE_MEDIUM": [
        OctaneShaderNodeCategory("OCTANE_MEDIUM", "Octane Medium", 
            octane_pin_type=consts.PinType.PT_MEDIUM,
            items=[
                OctaneNodeItem("OctaneAbsorption"),
                OctaneNodeItem("OctaneRandomWalk"),
                OctaneNodeItem("OctaneScattering"),
                OctaneNodeItem("OctaneSchlick", octane_pin_type=consts.PinType.PT_PHASEFUNCTION),
                # OctaneNodeItem("OctaneVolumeGradient"),
                OctaneNodeItem("ShaderNodeOctVolumeRampTex", octane_pin_type=consts.PinType.PT_VOLUME_RAMP),
                OctaneNodeItem("OctaneVolumeMedium"),
            ]  
        ),
    ],
    "OCTANE_EMISSION": [
        OctaneShaderNodeCategory("OCTANE_EMISSION", "Octane Emission", 
            octane_pin_type=consts.PinType.PT_EMISSION,
            items=[
                OctaneNodeItem("OctaneBlackBodyEmission"),
                OctaneNodeItem("OctaneTextureEmission"),
                OctaneNodeItem("ShaderNodeOctToonDirectionLight", octane_pin_type=consts.PinType.PT_GEOMETRY),
                OctaneNodeItem("ShaderNodeOctToonPointLight", octane_pin_type=consts.PinType.PT_GEOMETRY),                
                # OctaneNodeItem("OctaneToonDirectionalLight", octane_pin_type=consts.PinType.PT_GEOMETRY),
                # OctaneNodeItem("OctaneToonPointLight", octane_pin_type=consts.PinType.PT_GEOMETRY),
            ]  
        ),
    ],
    "OCTANE_ENVIRONMENT": [
        OctaneShaderNodeCategory("OCTANE_ENVIRONMENT", "Octane Environment", 
            octane_pin_type=consts.PinType.PT_ENVIRONMENT,
            items=[
                OctaneNodeItem("OctaneDaylightEnvironment"),
                OctaneNodeItem("OctanePlanetaryEnvironment"),
                OctaneNodeItem("OctaneTextureEnvironment"),
            ]  
        ),
    ],
    "OCTANE_CAMERA": [
        OctaneShaderNodeCategory("OCTANE_CAMERA", "Octane Camera", 
            octane_pin_type=consts.PinType.PT_CAMERA,
            items=[
                OctaneNodeItem("ShaderNodeOctOSLCamera"),
                OctaneNodeItem("ShaderNodeOctOSLBakingCamera"),
            ]  
        ),
    ],
    "OCTANE_ROUND_EDGE": [
        OctaneShaderNodeCategory("OCTANE_ROUND_EDGE", "Octane Round Edge", 
            octane_pin_type=consts.PinType.PT_ROUND_EDGES,
            items=[
                OctaneNodeItem("OctaneRoundEdges"),
            ]  
        ),
    ],
    "OCTANE_GEOMETRY": [
        OctaneShaderNodeCategory("OCTANE_GEOMETRY", "Octane Geometry", 
            octane_pin_type=consts.PinType.PT_GEOMETRY,
            items=[
                OctaneNodeItem("ShaderNodeOctVectron", poll=shader_poll),
                OctaneNodeItem("OctaneScatterInVolume"),
                OctaneNodeItem("OctaneScatterOnSurface"),
            ]  
        ),
    ],           
    "OCTANE_TEXTURE": [
        OctaneTextureNodeCategory("OCTANE_TEXTURE", "Octane Texture", 
            octane_pin_type=consts.PinType.PT_TEXTURE,
            items=[
                OctaneNodeItem("OctaneGaussianSpectrum"),
                OctaneNodeItem("OctaneGreyscaleColor"),
                # OctaneNodeItem("OctaneOSLTexture"),
                OctaneNodeItem("ShaderNodeOctOSLTex", poll=shader_poll),
                OctaneNodeItem("OctaneRGBColor"),
                OctaneTextureNodeCategory("OCTANE_TEXTURE_CONVERTERS", "Converters", 
                    octane_pin_type=consts.PinType.PT_TEXTURE,
                    items=[
                        OctaneNodeItem("OctaneFloat3ToColor"),
                        OctaneNodeItem("OctaneFloatToGreyscale"),
                        OctaneNodeItem("OctaneFloatsToColor"),
                        OctaneNodeItem("OctaneVolumeToTexture"),
                    ]
                ),
                OctaneTextureNodeCategory("OCTANE_TEXTURE_GEOMETRICS", "Geometric", 
                    octane_pin_type=consts.PinType.PT_TEXTURE,
                    items=[
                        OctaneNodeItem("OctaneColorVertexAttribute"),
                        OctaneNodeItem("OctaneCurvatureTexture"),
                        OctaneNodeItem("OctaneDirtTexture"),
                        OctaneNodeItem("OctaneFalloffMap"),
                        OctaneNodeItem("OctaneGreyscaleVertexAttribute"),
                        OctaneNodeItem("OctaneInstanceColor"),
                        OctaneNodeItem("OctaneInstanceRange"),
                        OctaneNodeItem("OctaneNormal"),
                        OctaneNodeItem("OctanePolygonSide"),
                        OctaneNodeItem("OctanePosition"),
                        OctaneNodeItem("OctaneRandomColorTexture"),
                        OctaneNodeItem("OctaneRayDirection"),
                        OctaneNodeItem("OctaneRelativeDistance"),
                        OctaneNodeItem("OctaneSamplePosition"),
                        OctaneNodeItem("OctaneSurfaceTangentDPdu"),
                        OctaneNodeItem("OctaneSurfaceTangentDPdv"),
                        OctaneNodeItem("OctaneUVCoordinate"),
                        OctaneNodeItem("OctaneWCoordinate"),
                        OctaneNodeItem("OctaneZDepth"),
                    ]
                ),
                OctaneTextureNodeCategory("OCTANE_TEXTURE_IMAGE", "Image", 
                    octane_pin_type=consts.PinType.PT_TEXTURE,
                    items=[
                        OctaneNodeItem("ShaderNodeOctAlphaImageTex"),
                        OctaneNodeItem("ShaderNodeOctFloatImageTex"),
                        OctaneNodeItem("ShaderNodeOctImageTex"),
                        OctaneNodeItem("ShaderNodeOctImageTileTex"),  
                    ]
                ), 
                OctaneTextureNodeCategory("OCTANE_TEXTURE_MAPPING", "Mapping", 
                    octane_pin_type=consts.PinType.PT_TEXTURE,
                    items=[
                        OctaneNodeItem("OctaneChaosTexture"),
                        OctaneNodeItem("OctaneTriplanarMap"),
                        OctaneNodeItem("OctaneUVWTransform"),  
                    ]
                ),
                OctaneTextureNodeCategory("OCTANE_TEXTURE_OPERATORS", "Operators", 
                    octane_pin_type=consts.PinType.PT_TEXTURE,
                    items=[
                        OctaneNodeItem("OctaneAddTexture"),
                        OctaneNodeItem("OctaneBinaryMathOperation"),
                        OctaneNodeItem("OctaneClampTexture"),
                        OctaneNodeItem("OctaneColorCorrection"),
                        OctaneNodeItem("OctaneComparison"),
                        OctaneNodeItem("OctaneCosineMixTexture"),
                        # OctaneNodeItem("OctaneGradientMap"),
                        OctaneNodeItem("ShaderNodeOctGradientTex"),
                        OctaneNodeItem("OctaneInvertTexture"),
                        OctaneNodeItem("OctaneMixTexture"),
                        OctaneNodeItem("OctaneMultiplyTexture"),
                        OctaneNodeItem("OctaneRandomMap"),
                        OctaneNodeItem("OctaneRange"),
                        OctaneNodeItem("OctaneSubtractTexture"),
                        OctaneNodeItem("OctaneUnaryMathOperation"),  
                    ]
                ),
                OctaneTextureNodeCategory("OCTANE_TEXTURE_PROCEDURAL", "Procedural", 
                    octane_pin_type=consts.PinType.PT_TEXTURE,
                    items=[
                        OctaneNodeItem("OctaneChainmail"),
                        OctaneNodeItem("OctaneChecksTexture"),
                        # OctaneNodeItem("OctaneCinema4DNoise"),
                        OctaneNodeItem("OctaneColorSquares"),
                        OctaneNodeItem("OctaneFlakes"),
                        OctaneNodeItem("OctaneFractal"),
                        OctaneNodeItem("OctaneGlowingCircle"),
                        OctaneNodeItem("OctaneGradientGenerator"),
                        OctaneNodeItem("OctaneHagelslag"),
                        OctaneNodeItem("OctaneIridescent"),
                        OctaneNodeItem("OctaneMarbleTexture"),
                        OctaneNodeItem("OctaneMoireMosaic"),
                        OctaneNodeItem("OctaneNoiseTexture"),
                        OctaneNodeItem("OctaneProceduralEffects"),
                        OctaneNodeItem("OctaneRidgedFractalTexture"),
                        OctaneNodeItem("OctaneSawWaveTexture"),
                        OctaneNodeItem("OctaneSineWaveTexture"),
                        OctaneNodeItem("OctaneSmoothVoronoiContours"),
                        OctaneNodeItem("OctaneStripes"),
                        OctaneNodeItem("OctaneTilePatterns"),
                        OctaneNodeItem("OctaneTriangleWaveTexture"),
                        OctaneNodeItem("OctaneTurbulenceTexture"),  
                    ]
                ),
                OctaneTextureNodeCategory("OCTANE_TEXTURE_UTILITY", "Utility", 
                    octane_pin_type=consts.PinType.PT_TEXTURE,
                    items=[
                        OctaneNodeItem("OctaneCaptureToCustomAOV"),
                        OctaneNodeItem("OctaneChannelInverter"),
                        OctaneNodeItem("OctaneChannelMapper"),
                        OctaneNodeItem("OctaneChannelMerger"),
                        OctaneNodeItem("OctaneChannelPicker"),
                        OctaneNodeItem("OctaneCompositeTexture"),
                        OctaneNodeItem("OctaneCompositeTextureLayer", octane_pin_type=consts.PinType.PT_TEX_COMPOSITE_LAYER),
                        OctaneNodeItem("OctaneRaySwitch"),
                        OctaneNodeItem("OctaneSpotlight"), 
                    ]
                ),                                                                                                
            ]        
        ),
    ],      
}

_draw_node_categories_menu = None
_octane_node_enum_items = None


def init_octane_node_enum_items():
    global _octane_node_enum_items
    if _octane_node_enum_items is not None:
        return
    # setup _octane_node_enum_items
    _octane_node_enum_items = {}
    data_headings = {}
    data_items = {}
    def add_octane_node_item(node_item, sub_type_name, octane_pin_type):
        if isinstance(node_item, OctaneNodeCategory):
            if octane_pin_type == consts.PinType.PT_UNKNOWN:
                octane_pin_type = node_item.octane_pin_type
            sub_type_name = getattr(node_item, "name", "")
            for _item in node_item.items(None):
                add_octane_node_item(_item, sub_type_name, octane_pin_type)
        else:
            if node_item.octane_pin_type != consts.PinType.PT_UNKNOWN:
                octane_pin_type = node_item.octane_pin_type
            if octane_pin_type not in data_headings:
                data_headings[octane_pin_type] = []
            if octane_pin_type not in data_items:
                data_items[octane_pin_type] = {}
            if sub_type_name not in data_headings[octane_pin_type]:
                data_headings[octane_pin_type].append(sub_type_name)
            if sub_type_name not in data_items[octane_pin_type]:
                data_items[octane_pin_type][sub_type_name] = []
            data_items[octane_pin_type][sub_type_name].append((node_item.nodetype, node_item.label, ""))
    for _id, category in _octane_node_items.items():
        for _item in category:
            add_octane_node_item(_item, "", _item.octane_pin_type)
    for pin_type, categories in data_items.items():
        _octane_node_enum_items[pin_type] = []
        for heading in data_headings[pin_type]:                                
            if len(heading):
                _octane_node_enum_items[pin_type].append(("", heading, ""))
            for _item in categories[heading]:
                _octane_node_enum_items[pin_type].append(_item)
    for pin_type, enum_items in _octane_node_enum_items.items():
        _octane_node_enum_items[pin_type].extend(consts.LINK_UTILITY_MENU)


def get_octane_node_enum_items(octane_pin_type):
    init_octane_node_enum_items() 
    if octane_pin_type in _octane_node_enum_items:
        return _octane_node_enum_items[octane_pin_type]
    return []


def register():
    global _draw_node_categories_menu
    _draw_node_categories_menu = nodeitems_utils.draw_node_categories_menu
    nodeitems_utils.draw_node_categories_menu = draw_octane_node_categories_menu
    for _id, _items in _octane_node_items.items():
        register_octane_node_categories(_id, _items)


def unregister():
    nodeitems_utils.draw_node_categories_menu = _draw_node_categories_menu
    for _id, _items in _octane_node_items.items():
        unregister_octane_node_categories(_id)        