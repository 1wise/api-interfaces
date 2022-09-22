# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: generation.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10generation.proto\x12\x07gooseai\"/\n\x05Token\x12\x11\n\x04text\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\n\n\x02id\x18\x02 \x01(\rB\x07\n\x05_text\"T\n\x06Tokens\x12\x1e\n\x06tokens\x18\x01 \x03(\x0b\x32\x0e.gooseai.Token\x12\x19\n\x0ctokenizer_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x0f\n\r_tokenizer_id\"\xb4\x02\n\x08\x41rtifact\x12\n\n\x02id\x18\x01 \x01(\x04\x12#\n\x04type\x18\x02 \x01(\x0e\x32\x15.gooseai.ArtifactType\x12\x0c\n\x04mime\x18\x03 \x01(\t\x12\x12\n\x05magic\x18\x04 \x01(\tH\x01\x88\x01\x01\x12\x10\n\x06\x62inary\x18\x05 \x01(\x0cH\x00\x12\x0e\n\x04text\x18\x06 \x01(\tH\x00\x12!\n\x06tokens\x18\x07 \x01(\x0b\x32\x0f.gooseai.TokensH\x00\x12\x33\n\nclassifier\x18\x0b \x01(\x0b\x32\x1d.gooseai.ClassifierParametersH\x00\x12\r\n\x05index\x18\x08 \x01(\r\x12,\n\rfinish_reason\x18\t \x01(\x0e\x32\x15.gooseai.FinishReason\x12\x0c\n\x04seed\x18\n \x01(\rB\x06\n\x04\x64\x61taB\x08\n\x06_magic\"N\n\x10PromptParameters\x12\x11\n\x04init\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12\x13\n\x06weight\x18\x02 \x01(\x02H\x01\x88\x01\x01\x42\x07\n\x05_initB\t\n\x07_weight\"\xaf\x01\n\x06Prompt\x12\x32\n\nparameters\x18\x01 \x01(\x0b\x32\x19.gooseai.PromptParametersH\x01\x88\x01\x01\x12\x0e\n\x04text\x18\x02 \x01(\tH\x00\x12!\n\x06tokens\x18\x03 \x01(\x0b\x32\x0f.gooseai.TokensH\x00\x12%\n\x08\x61rtifact\x18\x04 \x01(\x0b\x32\x11.gooseai.ArtifactH\x00\x42\x08\n\x06promptB\r\n\x0b_parameters\"\xef\x01\n\x11SamplerParameters\x12\x10\n\x03\x65ta\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12\x1b\n\x0esampling_steps\x18\x02 \x01(\x04H\x01\x88\x01\x01\x12\x1c\n\x0flatent_channels\x18\x03 \x01(\x04H\x02\x88\x01\x01\x12 \n\x13\x64ownsampling_factor\x18\x04 \x01(\x04H\x03\x88\x01\x01\x12\x16\n\tcfg_scale\x18\x05 \x01(\x02H\x04\x88\x01\x01\x42\x06\n\x04_etaB\x11\n\x0f_sampling_stepsB\x12\n\x10_latent_channelsB\x16\n\x14_downsampling_factorB\x0c\n\n_cfg_scale\"\x8b\x01\n\x15\x43onditionerParameters\x12 \n\x13vector_adjust_prior\x18\x01 \x01(\tH\x00\x88\x01\x01\x12(\n\x0b\x63onditioner\x18\x02 \x01(\x0b\x32\x0e.gooseai.ModelH\x01\x88\x01\x01\x42\x16\n\x14_vector_adjust_priorB\x0e\n\x0c_conditioner\"L\n\x12ScheduleParameters\x12\x12\n\x05start\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12\x10\n\x03\x65nd\x18\x02 \x01(\x02H\x01\x88\x01\x01\x42\x08\n\x06_startB\x06\n\x04_end\"\xe4\x01\n\rStepParameter\x12\x13\n\x0bscaled_step\x18\x01 \x01(\x02\x12\x30\n\x07sampler\x18\x02 \x01(\x0b\x32\x1a.gooseai.SamplerParametersH\x00\x88\x01\x01\x12\x32\n\x08schedule\x18\x03 \x01(\x0b\x32\x1b.gooseai.ScheduleParametersH\x01\x88\x01\x01\x12\x32\n\x08guidance\x18\x04 \x01(\x0b\x32\x1b.gooseai.GuidanceParametersH\x02\x88\x01\x01\x42\n\n\x08_samplerB\x0b\n\t_scheduleB\x0b\n\t_guidance\"\x97\x01\n\x05Model\x12\x30\n\x0c\x61rchitecture\x18\x01 \x01(\x0e\x32\x1a.gooseai.ModelArchitecture\x12\x11\n\tpublisher\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x61taset\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\x02\x12\x18\n\x10semantic_version\x18\x05 \x01(\t\x12\r\n\x05\x61lias\x18\x06 \x01(\t\"\xbc\x01\n\x10\x43utoutParameters\x12*\n\x07\x63utouts\x18\x01 \x03(\x0b\x32\x19.gooseai.CutoutParameters\x12\x12\n\x05\x63ount\x18\x02 \x01(\rH\x00\x88\x01\x01\x12\x11\n\x04gray\x18\x03 \x01(\x02H\x01\x88\x01\x01\x12\x11\n\x04\x62lur\x18\x04 \x01(\x02H\x02\x88\x01\x01\x12\x17\n\nsize_power\x18\x05 \x01(\x02H\x03\x88\x01\x01\x42\x08\n\x06_countB\x07\n\x05_grayB\x07\n\x05_blurB\r\n\x0b_size_power\"\x8f\x02\n\x1aGuidanceInstanceParameters\x12\x1e\n\x06models\x18\x02 \x03(\x0b\x32\x0e.gooseai.Model\x12\x1e\n\x11guidance_strength\x18\x03 \x01(\x02H\x00\x88\x01\x01\x12-\n\x08schedule\x18\x04 \x03(\x0b\x32\x1b.gooseai.ScheduleParameters\x12/\n\x07\x63utouts\x18\x05 \x01(\x0b\x32\x19.gooseai.CutoutParametersH\x01\x88\x01\x01\x12$\n\x06prompt\x18\x06 \x01(\x0b\x32\x0f.gooseai.PromptH\x02\x88\x01\x01\x42\x14\n\x12_guidance_strengthB\n\n\x08_cutoutsB\t\n\x07_prompt\"~\n\x12GuidanceParameters\x12\x30\n\x0fguidance_preset\x18\x01 \x01(\x0e\x32\x17.gooseai.GuidancePreset\x12\x36\n\tinstances\x18\x02 \x03(\x0b\x32#.gooseai.GuidanceInstanceParameters\"n\n\rTransformType\x12.\n\tdiffusion\x18\x01 \x01(\x0e\x32\x19.gooseai.DiffusionSamplerH\x00\x12%\n\x08upscaler\x18\x02 \x01(\x0e\x32\x11.gooseai.UpscalerH\x00\x42\x06\n\x04type\"\x87\x02\n\x0fImageParameters\x12\x13\n\x06height\x18\x01 \x01(\x04H\x00\x88\x01\x01\x12\x12\n\x05width\x18\x02 \x01(\x04H\x01\x88\x01\x01\x12\x0c\n\x04seed\x18\x03 \x03(\r\x12\x14\n\x07samples\x18\x04 \x01(\x04H\x02\x88\x01\x01\x12\x12\n\x05steps\x18\x05 \x01(\x04H\x03\x88\x01\x01\x12.\n\ttransform\x18\x06 \x01(\x0b\x32\x16.gooseai.TransformTypeH\x04\x88\x01\x01\x12*\n\nparameters\x18\x07 \x03(\x0b\x32\x16.gooseai.StepParameterB\t\n\x07_heightB\x08\n\x06_widthB\n\n\x08_samplesB\x08\n\x06_stepsB\x0c\n\n_transform\"J\n\x11\x43lassifierConcept\x12\x0f\n\x07\x63oncept\x18\x01 \x01(\t\x12\x16\n\tthreshold\x18\x02 \x01(\x02H\x00\x88\x01\x01\x42\x0c\n\n_threshold\"\xf4\x01\n\x12\x43lassifierCategory\x12\x0c\n\x04name\x18\x01 \x01(\t\x12,\n\x08\x63oncepts\x18\x02 \x03(\x0b\x32\x1a.gooseai.ClassifierConcept\x12\x17\n\nadjustment\x18\x03 \x01(\x02H\x00\x88\x01\x01\x12$\n\x06\x61\x63tion\x18\x04 \x01(\x0e\x32\x0f.gooseai.ActionH\x01\x88\x01\x01\x12\x35\n\x0f\x63lassifier_mode\x18\x05 \x01(\x0e\x32\x17.gooseai.ClassifierModeH\x02\x88\x01\x01\x42\r\n\x0b_adjustmentB\t\n\x07_actionB\x12\n\x10_classifier_mode\"\xb8\x01\n\x14\x43lassifierParameters\x12/\n\ncategories\x18\x01 \x03(\x0b\x32\x1b.gooseai.ClassifierCategory\x12,\n\x07\x65xceeds\x18\x02 \x03(\x0b\x32\x1b.gooseai.ClassifierCategory\x12-\n\x0frealized_action\x18\x03 \x01(\x0e\x32\x0f.gooseai.ActionH\x00\x88\x01\x01\x42\x12\n\x10_realized_action\"H\n\x0f\x41ssetParameters\x12$\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\x14.gooseai.AssetAction\x12\x0f\n\x07project\x18\x02 \x01(\x04\"\x94\x01\n\nAnswerMeta\x12\x13\n\x06gpu_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x13\n\x06\x63pu_id\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x14\n\x07node_id\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x16\n\tengine_id\x18\x04 \x01(\tH\x03\x88\x01\x01\x42\t\n\x07_gpu_idB\t\n\x07_cpu_idB\n\n\x08_node_idB\x0c\n\n_engine_id\"\xa9\x01\n\x06\x41nswer\x12\x11\n\tanswer_id\x18\x01 \x01(\t\x12\x12\n\nrequest_id\x18\x02 \x01(\t\x12\x10\n\x08received\x18\x03 \x01(\x04\x12\x0f\n\x07\x63reated\x18\x04 \x01(\x04\x12&\n\x04meta\x18\x06 \x01(\x0b\x32\x13.gooseai.AnswerMetaH\x00\x88\x01\x01\x12$\n\tartifacts\x18\x07 \x03(\x0b\x32\x11.gooseai.ArtifactB\x07\n\x05_meta\"\xdf\x02\n\x07Request\x12\x11\n\tengine_id\x18\x01 \x01(\t\x12\x12\n\nrequest_id\x18\x02 \x01(\t\x12-\n\x0erequested_type\x18\x03 \x01(\x0e\x32\x15.gooseai.ArtifactType\x12\x1f\n\x06prompt\x18\x04 \x03(\x0b\x32\x0f.gooseai.Prompt\x12)\n\x05image\x18\x05 \x01(\x0b\x32\x18.gooseai.ImageParametersH\x00\x12\x33\n\nclassifier\x18\x07 \x01(\x0b\x32\x1d.gooseai.ClassifierParametersH\x00\x12)\n\x05\x61sset\x18\x08 \x01(\x0b\x32\x18.gooseai.AssetParametersH\x00\x12\x38\n\x0b\x63onditioner\x18\x06 \x01(\x0b\x32\x1e.gooseai.ConditionerParametersH\x01\x88\x01\x01\x42\x08\n\x06paramsB\x0e\n\x0c_conditioner\"w\n\x08OnStatus\x12%\n\x06reason\x18\x01 \x03(\x0e\x32\x15.gooseai.FinishReason\x12\x13\n\x06target\x18\x02 \x01(\tH\x00\x88\x01\x01\x12$\n\x06\x61\x63tion\x18\x03 \x03(\x0e\x32\x14.gooseai.StageActionB\t\n\x07_target\"\\\n\x05Stage\x12\n\n\x02id\x18\x01 \x01(\t\x12!\n\x07request\x18\x02 \x01(\x0b\x32\x10.gooseai.Request\x12$\n\ton_status\x18\x03 \x03(\x0b\x32\x11.gooseai.OnStatus\"A\n\x0c\x43hainRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x1d\n\x05stage\x18\x02 \x03(\x0b\x32\x0e.gooseai.Stage*E\n\x0c\x46inishReason\x12\x08\n\x04NULL\x10\x00\x12\n\n\x06LENGTH\x10\x01\x12\x08\n\x04STOP\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x12\n\n\x06\x46ILTER\x10\x04*\xba\x01\n\x0c\x41rtifactType\x12\x11\n\rARTIFACT_NONE\x10\x00\x12\x12\n\x0e\x41RTIFACT_IMAGE\x10\x01\x12\x12\n\x0e\x41RTIFACT_VIDEO\x10\x02\x12\x11\n\rARTIFACT_TEXT\x10\x03\x12\x13\n\x0f\x41RTIFACT_TOKENS\x10\x04\x12\x16\n\x12\x41RTIFACT_EMBEDDING\x10\x05\x12\x1c\n\x18\x41RTIFACT_CLASSIFICATIONS\x10\x06\x12\x11\n\rARTIFACT_MASK\x10\x07*\xc5\x01\n\x10\x44iffusionSampler\x12\x10\n\x0cSAMPLER_DDIM\x10\x00\x12\x10\n\x0cSAMPLER_DDPM\x10\x01\x12\x13\n\x0fSAMPLER_K_EULER\x10\x02\x12\x1d\n\x19SAMPLER_K_EULER_ANCESTRAL\x10\x03\x12\x12\n\x0eSAMPLER_K_HEUN\x10\x04\x12\x13\n\x0fSAMPLER_K_DPM_2\x10\x05\x12\x1d\n\x19SAMPLER_K_DPM_2_ANCESTRAL\x10\x06\x12\x11\n\rSAMPLER_K_LMS\x10\x07*F\n\x08Upscaler\x12\x10\n\x0cUPSCALER_RGB\x10\x00\x12\x13\n\x0fUPSCALER_GFPGAN\x10\x01\x12\x13\n\x0fUPSCALER_ESRGAN\x10\x02*\x9e\x01\n\x0eGuidancePreset\x12\x18\n\x14GUIDANCE_PRESET_NONE\x10\x00\x12\x18\n\x14GUIDANCE_PRESET_FAST\x10\x01\x12\x1d\n\x19GUIDANCE_PRESET_EFFICIENT\x10\x02\x12\x1c\n\x18GUIDANCE_PRESET_BALANCED\x10\x03\x12\x1b\n\x17GUIDANCE_PRESET_QUALITY\x10\x04*\x91\x01\n\x11ModelArchitecture\x12\x1b\n\x17MODEL_ARCHITECTURE_NONE\x10\x00\x12\x1f\n\x1bMODEL_ARCHITECTURE_CLIP_VIT\x10\x01\x12\"\n\x1eMODEL_ARCHITECTURE_CLIP_RESNET\x10\x02\x12\x1a\n\x16MODEL_ARCHITECTURE_LDM\x10\x03*\xa2\x01\n\x06\x41\x63tion\x12\x16\n\x12\x41\x43TION_PASSTHROUGH\x10\x00\x12\x1f\n\x1b\x41\x43TION_REGENERATE_DUPLICATE\x10\x01\x12\x15\n\x11\x41\x43TION_REGENERATE\x10\x02\x12\x1e\n\x1a\x41\x43TION_OBFUSCATE_DUPLICATE\x10\x03\x12\x14\n\x10\x41\x43TION_OBFUSCATE\x10\x04\x12\x12\n\x0e\x41\x43TION_DISCARD\x10\x05*D\n\x0e\x43lassifierMode\x12\x17\n\x13\x43LSFR_MODE_ZEROSHOT\x10\x00\x12\x19\n\x15\x43LSFR_MODE_MULTICLASS\x10\x01*=\n\x0b\x41ssetAction\x12\r\n\tASSET_PUT\x10\x00\x12\r\n\tASSET_GET\x10\x01\x12\x10\n\x0c\x41SSET_DELETE\x10\x02*W\n\x0bStageAction\x12\x15\n\x11STAGE_ACTION_PASS\x10\x00\x12\x18\n\x14STAGE_ACTION_DISCARD\x10\x01\x12\x17\n\x13STAGE_ACTION_RETURN\x10\x02\x32\x83\x01\n\x11GenerationService\x12\x31\n\x08Generate\x12\x10.gooseai.Request\x1a\x0f.gooseai.Answer\"\x00\x30\x01\x12;\n\rChainGenerate\x12\x15.gooseai.ChainRequest\x1a\x0f.gooseai.Answer\"\x00\x30\x01\x42\x0fZ\r./;generationb\x06proto3')

_FINISHREASON = DESCRIPTOR.enum_types_by_name['FinishReason']
FinishReason = enum_type_wrapper.EnumTypeWrapper(_FINISHREASON)
_ARTIFACTTYPE = DESCRIPTOR.enum_types_by_name['ArtifactType']
ArtifactType = enum_type_wrapper.EnumTypeWrapper(_ARTIFACTTYPE)
_DIFFUSIONSAMPLER = DESCRIPTOR.enum_types_by_name['DiffusionSampler']
DiffusionSampler = enum_type_wrapper.EnumTypeWrapper(_DIFFUSIONSAMPLER)
_UPSCALER = DESCRIPTOR.enum_types_by_name['Upscaler']
Upscaler = enum_type_wrapper.EnumTypeWrapper(_UPSCALER)
_GUIDANCEPRESET = DESCRIPTOR.enum_types_by_name['GuidancePreset']
GuidancePreset = enum_type_wrapper.EnumTypeWrapper(_GUIDANCEPRESET)
_MODELARCHITECTURE = DESCRIPTOR.enum_types_by_name['ModelArchitecture']
ModelArchitecture = enum_type_wrapper.EnumTypeWrapper(_MODELARCHITECTURE)
_ACTION = DESCRIPTOR.enum_types_by_name['Action']
Action = enum_type_wrapper.EnumTypeWrapper(_ACTION)
_CLASSIFIERMODE = DESCRIPTOR.enum_types_by_name['ClassifierMode']
ClassifierMode = enum_type_wrapper.EnumTypeWrapper(_CLASSIFIERMODE)
_ASSETACTION = DESCRIPTOR.enum_types_by_name['AssetAction']
AssetAction = enum_type_wrapper.EnumTypeWrapper(_ASSETACTION)
_STAGEACTION = DESCRIPTOR.enum_types_by_name['StageAction']
StageAction = enum_type_wrapper.EnumTypeWrapper(_STAGEACTION)
NULL = 0
LENGTH = 1
STOP = 2
ERROR = 3
FILTER = 4
ARTIFACT_NONE = 0
ARTIFACT_IMAGE = 1
ARTIFACT_VIDEO = 2
ARTIFACT_TEXT = 3
ARTIFACT_TOKENS = 4
ARTIFACT_EMBEDDING = 5
ARTIFACT_CLASSIFICATIONS = 6
ARTIFACT_MASK = 7
SAMPLER_DDIM = 0
SAMPLER_DDPM = 1
SAMPLER_K_EULER = 2
SAMPLER_K_EULER_ANCESTRAL = 3
SAMPLER_K_HEUN = 4
SAMPLER_K_DPM_2 = 5
SAMPLER_K_DPM_2_ANCESTRAL = 6
SAMPLER_K_LMS = 7
UPSCALER_RGB = 0
UPSCALER_GFPGAN = 1
UPSCALER_ESRGAN = 2
GUIDANCE_PRESET_NONE = 0
GUIDANCE_PRESET_FAST = 1
GUIDANCE_PRESET_EFFICIENT = 2
GUIDANCE_PRESET_BALANCED = 3
GUIDANCE_PRESET_QUALITY = 4
MODEL_ARCHITECTURE_NONE = 0
MODEL_ARCHITECTURE_CLIP_VIT = 1
MODEL_ARCHITECTURE_CLIP_RESNET = 2
MODEL_ARCHITECTURE_LDM = 3
ACTION_PASSTHROUGH = 0
ACTION_REGENERATE_DUPLICATE = 1
ACTION_REGENERATE = 2
ACTION_OBFUSCATE_DUPLICATE = 3
ACTION_OBFUSCATE = 4
ACTION_DISCARD = 5
CLSFR_MODE_ZEROSHOT = 0
CLSFR_MODE_MULTICLASS = 1
ASSET_PUT = 0
ASSET_GET = 1
ASSET_DELETE = 2
STAGE_ACTION_PASS = 0
STAGE_ACTION_DISCARD = 1
STAGE_ACTION_RETURN = 2


_TOKEN = DESCRIPTOR.message_types_by_name['Token']
_TOKENS = DESCRIPTOR.message_types_by_name['Tokens']
_ARTIFACT = DESCRIPTOR.message_types_by_name['Artifact']
_PROMPTPARAMETERS = DESCRIPTOR.message_types_by_name['PromptParameters']
_PROMPT = DESCRIPTOR.message_types_by_name['Prompt']
_SAMPLERPARAMETERS = DESCRIPTOR.message_types_by_name['SamplerParameters']
_CONDITIONERPARAMETERS = DESCRIPTOR.message_types_by_name['ConditionerParameters']
_SCHEDULEPARAMETERS = DESCRIPTOR.message_types_by_name['ScheduleParameters']
_STEPPARAMETER = DESCRIPTOR.message_types_by_name['StepParameter']
_MODEL = DESCRIPTOR.message_types_by_name['Model']
_CUTOUTPARAMETERS = DESCRIPTOR.message_types_by_name['CutoutParameters']
_GUIDANCEINSTANCEPARAMETERS = DESCRIPTOR.message_types_by_name['GuidanceInstanceParameters']
_GUIDANCEPARAMETERS = DESCRIPTOR.message_types_by_name['GuidanceParameters']
_TRANSFORMTYPE = DESCRIPTOR.message_types_by_name['TransformType']
_IMAGEPARAMETERS = DESCRIPTOR.message_types_by_name['ImageParameters']
_CLASSIFIERCONCEPT = DESCRIPTOR.message_types_by_name['ClassifierConcept']
_CLASSIFIERCATEGORY = DESCRIPTOR.message_types_by_name['ClassifierCategory']
_CLASSIFIERPARAMETERS = DESCRIPTOR.message_types_by_name['ClassifierParameters']
_ASSETPARAMETERS = DESCRIPTOR.message_types_by_name['AssetParameters']
_ANSWERMETA = DESCRIPTOR.message_types_by_name['AnswerMeta']
_ANSWER = DESCRIPTOR.message_types_by_name['Answer']
_REQUEST = DESCRIPTOR.message_types_by_name['Request']
_ONSTATUS = DESCRIPTOR.message_types_by_name['OnStatus']
_STAGE = DESCRIPTOR.message_types_by_name['Stage']
_CHAINREQUEST = DESCRIPTOR.message_types_by_name['ChainRequest']
Token = _reflection.GeneratedProtocolMessageType('Token', (_message.Message,), {
  'DESCRIPTOR' : _TOKEN,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.Token)
  })
_sym_db.RegisterMessage(Token)

Tokens = _reflection.GeneratedProtocolMessageType('Tokens', (_message.Message,), {
  'DESCRIPTOR' : _TOKENS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.Tokens)
  })
_sym_db.RegisterMessage(Tokens)

Artifact = _reflection.GeneratedProtocolMessageType('Artifact', (_message.Message,), {
  'DESCRIPTOR' : _ARTIFACT,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.Artifact)
  })
_sym_db.RegisterMessage(Artifact)

PromptParameters = _reflection.GeneratedProtocolMessageType('PromptParameters', (_message.Message,), {
  'DESCRIPTOR' : _PROMPTPARAMETERS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.PromptParameters)
  })
_sym_db.RegisterMessage(PromptParameters)

Prompt = _reflection.GeneratedProtocolMessageType('Prompt', (_message.Message,), {
  'DESCRIPTOR' : _PROMPT,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.Prompt)
  })
_sym_db.RegisterMessage(Prompt)

SamplerParameters = _reflection.GeneratedProtocolMessageType('SamplerParameters', (_message.Message,), {
  'DESCRIPTOR' : _SAMPLERPARAMETERS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.SamplerParameters)
  })
_sym_db.RegisterMessage(SamplerParameters)

ConditionerParameters = _reflection.GeneratedProtocolMessageType('ConditionerParameters', (_message.Message,), {
  'DESCRIPTOR' : _CONDITIONERPARAMETERS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.ConditionerParameters)
  })
_sym_db.RegisterMessage(ConditionerParameters)

ScheduleParameters = _reflection.GeneratedProtocolMessageType('ScheduleParameters', (_message.Message,), {
  'DESCRIPTOR' : _SCHEDULEPARAMETERS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.ScheduleParameters)
  })
_sym_db.RegisterMessage(ScheduleParameters)

StepParameter = _reflection.GeneratedProtocolMessageType('StepParameter', (_message.Message,), {
  'DESCRIPTOR' : _STEPPARAMETER,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.StepParameter)
  })
_sym_db.RegisterMessage(StepParameter)

Model = _reflection.GeneratedProtocolMessageType('Model', (_message.Message,), {
  'DESCRIPTOR' : _MODEL,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.Model)
  })
_sym_db.RegisterMessage(Model)

CutoutParameters = _reflection.GeneratedProtocolMessageType('CutoutParameters', (_message.Message,), {
  'DESCRIPTOR' : _CUTOUTPARAMETERS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.CutoutParameters)
  })
_sym_db.RegisterMessage(CutoutParameters)

GuidanceInstanceParameters = _reflection.GeneratedProtocolMessageType('GuidanceInstanceParameters', (_message.Message,), {
  'DESCRIPTOR' : _GUIDANCEINSTANCEPARAMETERS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.GuidanceInstanceParameters)
  })
_sym_db.RegisterMessage(GuidanceInstanceParameters)

GuidanceParameters = _reflection.GeneratedProtocolMessageType('GuidanceParameters', (_message.Message,), {
  'DESCRIPTOR' : _GUIDANCEPARAMETERS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.GuidanceParameters)
  })
_sym_db.RegisterMessage(GuidanceParameters)

TransformType = _reflection.GeneratedProtocolMessageType('TransformType', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORMTYPE,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.TransformType)
  })
_sym_db.RegisterMessage(TransformType)

ImageParameters = _reflection.GeneratedProtocolMessageType('ImageParameters', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEPARAMETERS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.ImageParameters)
  })
_sym_db.RegisterMessage(ImageParameters)

ClassifierConcept = _reflection.GeneratedProtocolMessageType('ClassifierConcept', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFIERCONCEPT,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.ClassifierConcept)
  })
_sym_db.RegisterMessage(ClassifierConcept)

ClassifierCategory = _reflection.GeneratedProtocolMessageType('ClassifierCategory', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFIERCATEGORY,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.ClassifierCategory)
  })
_sym_db.RegisterMessage(ClassifierCategory)

ClassifierParameters = _reflection.GeneratedProtocolMessageType('ClassifierParameters', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFIERPARAMETERS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.ClassifierParameters)
  })
_sym_db.RegisterMessage(ClassifierParameters)

AssetParameters = _reflection.GeneratedProtocolMessageType('AssetParameters', (_message.Message,), {
  'DESCRIPTOR' : _ASSETPARAMETERS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.AssetParameters)
  })
_sym_db.RegisterMessage(AssetParameters)

AnswerMeta = _reflection.GeneratedProtocolMessageType('AnswerMeta', (_message.Message,), {
  'DESCRIPTOR' : _ANSWERMETA,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.AnswerMeta)
  })
_sym_db.RegisterMessage(AnswerMeta)

Answer = _reflection.GeneratedProtocolMessageType('Answer', (_message.Message,), {
  'DESCRIPTOR' : _ANSWER,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.Answer)
  })
_sym_db.RegisterMessage(Answer)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.Request)
  })
_sym_db.RegisterMessage(Request)

OnStatus = _reflection.GeneratedProtocolMessageType('OnStatus', (_message.Message,), {
  'DESCRIPTOR' : _ONSTATUS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.OnStatus)
  })
_sym_db.RegisterMessage(OnStatus)

Stage = _reflection.GeneratedProtocolMessageType('Stage', (_message.Message,), {
  'DESCRIPTOR' : _STAGE,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.Stage)
  })
_sym_db.RegisterMessage(Stage)

ChainRequest = _reflection.GeneratedProtocolMessageType('ChainRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHAINREQUEST,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.ChainRequest)
  })
_sym_db.RegisterMessage(ChainRequest)

_GENERATIONSERVICE = DESCRIPTOR.services_by_name['GenerationService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\r./;generation'
  _FINISHREASON._serialized_start=4094
  _FINISHREASON._serialized_end=4163
  _ARTIFACTTYPE._serialized_start=4166
  _ARTIFACTTYPE._serialized_end=4352
  _DIFFUSIONSAMPLER._serialized_start=4355
  _DIFFUSIONSAMPLER._serialized_end=4552
  _UPSCALER._serialized_start=4554
  _UPSCALER._serialized_end=4624
  _GUIDANCEPRESET._serialized_start=4627
  _GUIDANCEPRESET._serialized_end=4785
  _MODELARCHITECTURE._serialized_start=4788
  _MODELARCHITECTURE._serialized_end=4933
  _ACTION._serialized_start=4936
  _ACTION._serialized_end=5098
  _CLASSIFIERMODE._serialized_start=5100
  _CLASSIFIERMODE._serialized_end=5168
  _ASSETACTION._serialized_start=5170
  _ASSETACTION._serialized_end=5231
  _STAGEACTION._serialized_start=5233
  _STAGEACTION._serialized_end=5320
  _TOKEN._serialized_start=29
  _TOKEN._serialized_end=76
  _TOKENS._serialized_start=78
  _TOKENS._serialized_end=162
  _ARTIFACT._serialized_start=165
  _ARTIFACT._serialized_end=473
  _PROMPTPARAMETERS._serialized_start=475
  _PROMPTPARAMETERS._serialized_end=553
  _PROMPT._serialized_start=556
  _PROMPT._serialized_end=731
  _SAMPLERPARAMETERS._serialized_start=734
  _SAMPLERPARAMETERS._serialized_end=973
  _CONDITIONERPARAMETERS._serialized_start=976
  _CONDITIONERPARAMETERS._serialized_end=1115
  _SCHEDULEPARAMETERS._serialized_start=1117
  _SCHEDULEPARAMETERS._serialized_end=1193
  _STEPPARAMETER._serialized_start=1196
  _STEPPARAMETER._serialized_end=1424
  _MODEL._serialized_start=1427
  _MODEL._serialized_end=1578
  _CUTOUTPARAMETERS._serialized_start=1581
  _CUTOUTPARAMETERS._serialized_end=1769
  _GUIDANCEINSTANCEPARAMETERS._serialized_start=1772
  _GUIDANCEINSTANCEPARAMETERS._serialized_end=2043
  _GUIDANCEPARAMETERS._serialized_start=2045
  _GUIDANCEPARAMETERS._serialized_end=2171
  _TRANSFORMTYPE._serialized_start=2173
  _TRANSFORMTYPE._serialized_end=2283
  _IMAGEPARAMETERS._serialized_start=2286
  _IMAGEPARAMETERS._serialized_end=2549
  _CLASSIFIERCONCEPT._serialized_start=2551
  _CLASSIFIERCONCEPT._serialized_end=2625
  _CLASSIFIERCATEGORY._serialized_start=2628
  _CLASSIFIERCATEGORY._serialized_end=2872
  _CLASSIFIERPARAMETERS._serialized_start=2875
  _CLASSIFIERPARAMETERS._serialized_end=3059
  _ASSETPARAMETERS._serialized_start=3061
  _ASSETPARAMETERS._serialized_end=3133
  _ANSWERMETA._serialized_start=3136
  _ANSWERMETA._serialized_end=3284
  _ANSWER._serialized_start=3287
  _ANSWER._serialized_end=3456
  _REQUEST._serialized_start=3459
  _REQUEST._serialized_end=3810
  _ONSTATUS._serialized_start=3812
  _ONSTATUS._serialized_end=3931
  _STAGE._serialized_start=3933
  _STAGE._serialized_end=4025
  _CHAINREQUEST._serialized_start=4027
  _CHAINREQUEST._serialized_end=4092
  _GENERATIONSERVICE._serialized_start=5323
  _GENERATIONSERVICE._serialized_end=5454
# @@protoc_insertion_point(module_scope)
