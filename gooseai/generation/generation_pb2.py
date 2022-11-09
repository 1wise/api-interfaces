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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10generation.proto\x12\x07gooseai\"/\n\x05Token\x12\x11\n\x04text\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\n\n\x02id\x18\x02 \x01(\rB\x07\n\x05_text\"T\n\x06Tokens\x12\x1e\n\x06tokens\x18\x01 \x03(\x0b\x32\x0e.gooseai.Token\x12\x19\n\x0ctokenizer_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x0f\n\r_tokenizer_id\"\xd0\x02\n\x08\x41rtifact\x12\n\n\x02id\x18\x01 \x01(\x04\x12#\n\x04type\x18\x02 \x01(\x0e\x32\x15.gooseai.ArtifactType\x12\x0c\n\x04mime\x18\x03 \x01(\t\x12\x12\n\x05magic\x18\x04 \x01(\tH\x01\x88\x01\x01\x12\x10\n\x06\x62inary\x18\x05 \x01(\x0cH\x00\x12\x0e\n\x04text\x18\x06 \x01(\tH\x00\x12!\n\x06tokens\x18\x07 \x01(\x0b\x32\x0f.gooseai.TokensH\x00\x12\x33\n\nclassifier\x18\x0b \x01(\x0b\x32\x1d.gooseai.ClassifierParametersH\x00\x12\r\n\x05index\x18\x08 \x01(\r\x12,\n\rfinish_reason\x18\t \x01(\x0e\x32\x15.gooseai.FinishReason\x12\x0c\n\x04seed\x18\n \x01(\r\x12\x0c\n\x04uuid\x18\x0c \x01(\t\x12\x0c\n\x04size\x18\r \x01(\x04\x42\x06\n\x04\x64\x61taB\x08\n\x06_magic\"N\n\x10PromptParameters\x12\x11\n\x04init\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12\x13\n\x06weight\x18\x02 \x01(\x02H\x01\x88\x01\x01\x42\x07\n\x05_initB\t\n\x07_weight\"\xaf\x01\n\x06Prompt\x12\x32\n\nparameters\x18\x01 \x01(\x0b\x32\x19.gooseai.PromptParametersH\x01\x88\x01\x01\x12\x0e\n\x04text\x18\x02 \x01(\tH\x00\x12!\n\x06tokens\x18\x03 \x01(\x0b\x32\x0f.gooseai.TokensH\x00\x12%\n\x08\x61rtifact\x18\x04 \x01(\x0b\x32\x11.gooseai.ArtifactH\x00\x42\x08\n\x06promptB\r\n\x0b_parameters\"\xa3\x02\n\x11SamplerParameters\x12\x10\n\x03\x65ta\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12\x1b\n\x0esampling_steps\x18\x02 \x01(\x04H\x01\x88\x01\x01\x12\x1c\n\x0flatent_channels\x18\x03 \x01(\x04H\x02\x88\x01\x01\x12 \n\x13\x64ownsampling_factor\x18\x04 \x01(\x04H\x03\x88\x01\x01\x12\x16\n\tcfg_scale\x18\x05 \x01(\x02H\x04\x88\x01\x01\x12\x1d\n\x10init_noise_scale\x18\x06 \x01(\x02H\x05\x88\x01\x01\x42\x06\n\x04_etaB\x11\n\x0f_sampling_stepsB\x12\n\x10_latent_channelsB\x16\n\x14_downsampling_factorB\x0c\n\n_cfg_scaleB\x13\n\x11_init_noise_scale\"\x8b\x01\n\x15\x43onditionerParameters\x12 \n\x13vector_adjust_prior\x18\x01 \x01(\tH\x00\x88\x01\x01\x12(\n\x0b\x63onditioner\x18\x02 \x01(\x0b\x32\x0e.gooseai.ModelH\x01\x88\x01\x01\x42\x16\n\x14_vector_adjust_priorB\x0e\n\x0c_conditioner\"j\n\x12ScheduleParameters\x12\x12\n\x05start\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12\x10\n\x03\x65nd\x18\x02 \x01(\x02H\x01\x88\x01\x01\x12\x12\n\x05value\x18\x03 \x01(\x02H\x02\x88\x01\x01\x42\x08\n\x06_startB\x06\n\x04_endB\x08\n\x06_value\"\xe4\x01\n\rStepParameter\x12\x13\n\x0bscaled_step\x18\x01 \x01(\x02\x12\x30\n\x07sampler\x18\x02 \x01(\x0b\x32\x1a.gooseai.SamplerParametersH\x00\x88\x01\x01\x12\x32\n\x08schedule\x18\x03 \x01(\x0b\x32\x1b.gooseai.ScheduleParametersH\x01\x88\x01\x01\x12\x32\n\x08guidance\x18\x04 \x01(\x0b\x32\x1b.gooseai.GuidanceParametersH\x02\x88\x01\x01\x42\n\n\x08_samplerB\x0b\n\t_scheduleB\x0b\n\t_guidance\"\x97\x01\n\x05Model\x12\x30\n\x0c\x61rchitecture\x18\x01 \x01(\x0e\x32\x1a.gooseai.ModelArchitecture\x12\x11\n\tpublisher\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x61taset\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\x02\x12\x18\n\x10semantic_version\x18\x05 \x01(\t\x12\r\n\x05\x61lias\x18\x06 \x01(\t\"\xbc\x01\n\x10\x43utoutParameters\x12*\n\x07\x63utouts\x18\x01 \x03(\x0b\x32\x19.gooseai.CutoutParameters\x12\x12\n\x05\x63ount\x18\x02 \x01(\rH\x00\x88\x01\x01\x12\x11\n\x04gray\x18\x03 \x01(\x02H\x01\x88\x01\x01\x12\x11\n\x04\x62lur\x18\x04 \x01(\x02H\x02\x88\x01\x01\x12\x17\n\nsize_power\x18\x05 \x01(\x02H\x03\x88\x01\x01\x42\x08\n\x06_countB\x07\n\x05_grayB\x07\n\x05_blurB\r\n\x0b_size_power\"=\n\x1aGuidanceScheduleParameters\x12\x10\n\x08\x64uration\x18\x01 \x01(\x02\x12\r\n\x05value\x18\x02 \x01(\x02\"\x97\x02\n\x1aGuidanceInstanceParameters\x12\x1e\n\x06models\x18\x02 \x03(\x0b\x32\x0e.gooseai.Model\x12\x1e\n\x11guidance_strength\x18\x03 \x01(\x02H\x00\x88\x01\x01\x12\x35\n\x08schedule\x18\x04 \x03(\x0b\x32#.gooseai.GuidanceScheduleParameters\x12/\n\x07\x63utouts\x18\x05 \x01(\x0b\x32\x19.gooseai.CutoutParametersH\x01\x88\x01\x01\x12$\n\x06prompt\x18\x06 \x01(\x0b\x32\x0f.gooseai.PromptH\x02\x88\x01\x01\x42\x14\n\x12_guidance_strengthB\n\n\x08_cutoutsB\t\n\x07_prompt\"~\n\x12GuidanceParameters\x12\x30\n\x0fguidance_preset\x18\x01 \x01(\x0e\x32\x17.gooseai.GuidancePreset\x12\x36\n\tinstances\x18\x02 \x03(\x0b\x32#.gooseai.GuidanceInstanceParameters\"\x9e\x01\n\rTransformType\x12.\n\tdiffusion\x18\x01 \x01(\x0e\x32\x19.gooseai.DiffusionSamplerH\x00\x12%\n\x08upscaler\x18\x02 \x01(\x0e\x32\x11.gooseai.UpscalerH\x00\x12.\n\x08sequence\x18\x03 \x01(\x0b\x32\x1a.gooseai.TransformSequenceH\x00\x42\x06\n\x04type\"\x87\x02\n\x0fImageParameters\x12\x13\n\x06height\x18\x01 \x01(\x04H\x00\x88\x01\x01\x12\x12\n\x05width\x18\x02 \x01(\x04H\x01\x88\x01\x01\x12\x0c\n\x04seed\x18\x03 \x03(\r\x12\x14\n\x07samples\x18\x04 \x01(\x04H\x02\x88\x01\x01\x12\x12\n\x05steps\x18\x05 \x01(\x04H\x03\x88\x01\x01\x12.\n\ttransform\x18\x06 \x01(\x0b\x32\x16.gooseai.TransformTypeH\x04\x88\x01\x01\x12*\n\nparameters\x18\x07 \x03(\x0b\x32\x16.gooseai.StepParameterB\t\n\x07_heightB\x08\n\x06_widthB\n\n\x08_samplesB\x08\n\x06_stepsB\x0c\n\n_transform\"J\n\x11\x43lassifierConcept\x12\x0f\n\x07\x63oncept\x18\x01 \x01(\t\x12\x16\n\tthreshold\x18\x02 \x01(\x02H\x00\x88\x01\x01\x42\x0c\n\n_threshold\"\xf4\x01\n\x12\x43lassifierCategory\x12\x0c\n\x04name\x18\x01 \x01(\t\x12,\n\x08\x63oncepts\x18\x02 \x03(\x0b\x32\x1a.gooseai.ClassifierConcept\x12\x17\n\nadjustment\x18\x03 \x01(\x02H\x00\x88\x01\x01\x12$\n\x06\x61\x63tion\x18\x04 \x01(\x0e\x32\x0f.gooseai.ActionH\x01\x88\x01\x01\x12\x35\n\x0f\x63lassifier_mode\x18\x05 \x01(\x0e\x32\x17.gooseai.ClassifierModeH\x02\x88\x01\x01\x42\r\n\x0b_adjustmentB\t\n\x07_actionB\x12\n\x10_classifier_mode\"\xb8\x01\n\x14\x43lassifierParameters\x12/\n\ncategories\x18\x01 \x03(\x0b\x32\x1b.gooseai.ClassifierCategory\x12,\n\x07\x65xceeds\x18\x02 \x03(\x0b\x32\x1b.gooseai.ClassifierCategory\x12-\n\x0frealized_action\x18\x03 \x01(\x0e\x32\x0f.gooseai.ActionH\x00\x88\x01\x01\x42\x12\n\x10_realized_action\"?\n\x11TransformAddNoise\x12\x0e\n\x06\x61mount\x18\x01 \x01(\x02\x12\x11\n\x04seed\x18\x02 \x01(\rH\x00\x88\x01\x01\x42\x07\n\x05_seed\"C\n\x0eTransformBlend\x12\x0e\n\x06\x61mount\x18\x01 \x01(\x02\x12!\n\x06target\x18\x02 \x01(\x0b\x32\x11.gooseai.Artifact\"d\n\x13TransformColorMatch\x12+\n\ncolor_mode\x18\x01 \x01(\x0e\x32\x17.gooseai.ColorMatchMode\x12 \n\x05image\x18\x02 \x01(\x0b\x32\x11.gooseai.Artifact\"_\n\x11TransformContrast\x12\x17\n\nbrightness\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12\x15\n\x08\x63ontrast\x18\x02 \x01(\x02H\x01\x88\x01\x01\x42\r\n\x0b_brightnessB\x0b\n\t_contrast\"`\n\x12TransformDepthCalc\x12\x13\n\x06\x65xport\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12\x19\n\x0c\x62lend_weight\x18\x02 \x01(\x02H\x01\x88\x01\x01\x42\t\n\x07_exportB\x0f\n\r_blend_weight\"\x84\x01\n\x0fTransformWarp2d\x12(\n\x0b\x62order_mode\x18\x01 \x01(\x0e\x32\x13.gooseai.BorderMode\x12\x13\n\x0btranslate_x\x18\x04 \x01(\x02\x12\x13\n\x0btranslate_y\x18\x05 \x01(\x02\x12\x0e\n\x06rotate\x18\x02 \x01(\x02\x12\r\n\x05scale\x18\x03 \x01(\x02\"\xe4\x01\n\x0fTransformWarp3d\x12(\n\x0b\x62order_mode\x18\x01 \x01(\x0e\x32\x13.gooseai.BorderMode\x12\x13\n\x0btranslate_x\x18\x03 \x01(\x02\x12\x13\n\x0btranslate_y\x18\x04 \x01(\x02\x12\x13\n\x0btranslate_z\x18\x05 \x01(\x02\x12\x10\n\x08rotate_x\x18\x06 \x01(\x02\x12\x10\n\x08rotate_y\x18\x07 \x01(\x02\x12\x10\n\x08rotate_z\x18\x08 \x01(\x02\x12\x12\n\nnear_plane\x18\t \x01(\x02\x12\x11\n\tfar_plane\x18\n \x01(\x02\x12\x0b\n\x03\x66ov\x18\x0b \x01(\x02\"\xc0\x01\n\x11TransformWarpFlow\x12(\n\x08\x66low_map\x18\x01 \x01(\x0b\x32\x11.gooseai.ArtifactH\x00\x88\x01\x01\x12*\n\nprev_frame\x18\x02 \x01(\x0b\x32\x11.gooseai.ArtifactH\x01\x88\x01\x01\x12*\n\nnext_frame\x18\x03 \x01(\x0b\x32\x11.gooseai.ArtifactH\x02\x88\x01\x01\x42\x0b\n\t_flow_mapB\r\n\x0b_prev_frameB\r\n\x0b_next_frame\"\x99\x03\n\x12TransformOperation\x12/\n\tadd_noise\x18\x01 \x01(\x0b\x32\x1a.gooseai.TransformAddNoiseH\x00\x12(\n\x05\x62lend\x18\x06 \x01(\x0b\x32\x17.gooseai.TransformBlendH\x00\x12\x33\n\x0b\x63olor_match\x18\x02 \x01(\x0b\x32\x1c.gooseai.TransformColorMatchH\x00\x12.\n\x08\x63ontrast\x18\x08 \x01(\x0b\x32\x1a.gooseai.TransformContrastH\x00\x12\x31\n\ndepth_calc\x18\x07 \x01(\x0b\x32\x1b.gooseai.TransformDepthCalcH\x00\x12*\n\x06warp2d\x18\x03 \x01(\x0b\x32\x18.gooseai.TransformWarp2dH\x00\x12*\n\x06warp3d\x18\x04 \x01(\x0b\x32\x18.gooseai.TransformWarp3dH\x00\x12/\n\twarp_flow\x18\x05 \x01(\x0b\x32\x1a.gooseai.TransformWarpFlowH\x00\x42\x07\n\x05xform\"D\n\x11TransformSequence\x12/\n\noperations\x18\x01 \x03(\x0b\x32\x1b.gooseai.TransformOperation\"k\n\x0f\x41ssetParameters\x12$\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\x14.gooseai.AssetAction\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x1e\n\x03use\x18\x03 \x01(\x0e\x32\x11.gooseai.AssetUse\"\x94\x01\n\nAnswerMeta\x12\x13\n\x06gpu_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x13\n\x06\x63pu_id\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x14\n\x07node_id\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x16\n\tengine_id\x18\x04 \x01(\tH\x03\x88\x01\x01\x42\t\n\x07_gpu_idB\t\n\x07_cpu_idB\n\n\x08_node_idB\x0c\n\n_engine_id\"\xa9\x01\n\x06\x41nswer\x12\x11\n\tanswer_id\x18\x01 \x01(\t\x12\x12\n\nrequest_id\x18\x02 \x01(\t\x12\x10\n\x08received\x18\x03 \x01(\x04\x12\x0f\n\x07\x63reated\x18\x04 \x01(\x04\x12&\n\x04meta\x18\x06 \x01(\x0b\x32\x13.gooseai.AnswerMetaH\x00\x88\x01\x01\x12$\n\tartifacts\x18\x07 \x03(\x0b\x32\x11.gooseai.ArtifactB\x07\n\x05_meta\"\'\n\x15InterpolateParameters\x12\x0e\n\x06ratios\x18\x01 \x03(\x02\"\x96\x03\n\x07Request\x12\x11\n\tengine_id\x18\x01 \x01(\t\x12\x12\n\nrequest_id\x18\x02 \x01(\t\x12-\n\x0erequested_type\x18\x03 \x01(\x0e\x32\x15.gooseai.ArtifactType\x12\x1f\n\x06prompt\x18\x04 \x03(\x0b\x32\x0f.gooseai.Prompt\x12)\n\x05image\x18\x05 \x01(\x0b\x32\x18.gooseai.ImageParametersH\x00\x12\x33\n\nclassifier\x18\x07 \x01(\x0b\x32\x1d.gooseai.ClassifierParametersH\x00\x12)\n\x05\x61sset\x18\x08 \x01(\x0b\x32\x18.gooseai.AssetParametersH\x00\x12\x35\n\x0binterpolate\x18\t \x01(\x0b\x32\x1e.gooseai.InterpolateParametersH\x00\x12\x38\n\x0b\x63onditioner\x18\x06 \x01(\x0b\x32\x1e.gooseai.ConditionerParametersH\x01\x88\x01\x01\x42\x08\n\x06paramsB\x0e\n\x0c_conditioner\"w\n\x08OnStatus\x12%\n\x06reason\x18\x01 \x03(\x0e\x32\x15.gooseai.FinishReason\x12\x13\n\x06target\x18\x02 \x01(\tH\x00\x88\x01\x01\x12$\n\x06\x61\x63tion\x18\x03 \x03(\x0e\x32\x14.gooseai.StageActionB\t\n\x07_target\"\\\n\x05Stage\x12\n\n\x02id\x18\x01 \x01(\t\x12!\n\x07request\x18\x02 \x01(\x0b\x32\x10.gooseai.Request\x12$\n\ton_status\x18\x03 \x03(\x0b\x32\x11.gooseai.OnStatus\"A\n\x0c\x43hainRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x1d\n\x05stage\x18\x02 \x03(\x0b\x32\x0e.gooseai.Stage*E\n\x0c\x46inishReason\x12\x08\n\x04NULL\x10\x00\x12\n\n\x06LENGTH\x10\x01\x12\x08\n\x04STOP\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x12\n\n\x06\x46ILTER\x10\x04*\xba\x01\n\x0c\x41rtifactType\x12\x11\n\rARTIFACT_NONE\x10\x00\x12\x12\n\x0e\x41RTIFACT_IMAGE\x10\x01\x12\x12\n\x0e\x41RTIFACT_VIDEO\x10\x02\x12\x11\n\rARTIFACT_TEXT\x10\x03\x12\x13\n\x0f\x41RTIFACT_TOKENS\x10\x04\x12\x16\n\x12\x41RTIFACT_EMBEDDING\x10\x05\x12\x1c\n\x18\x41RTIFACT_CLASSIFICATIONS\x10\x06\x12\x11\n\rARTIFACT_MASK\x10\x07*\xc5\x01\n\x10\x44iffusionSampler\x12\x10\n\x0cSAMPLER_DDIM\x10\x00\x12\x10\n\x0cSAMPLER_DDPM\x10\x01\x12\x13\n\x0fSAMPLER_K_EULER\x10\x02\x12\x1d\n\x19SAMPLER_K_EULER_ANCESTRAL\x10\x03\x12\x12\n\x0eSAMPLER_K_HEUN\x10\x04\x12\x13\n\x0fSAMPLER_K_DPM_2\x10\x05\x12\x1d\n\x19SAMPLER_K_DPM_2_ANCESTRAL\x10\x06\x12\x11\n\rSAMPLER_K_LMS\x10\x07*F\n\x08Upscaler\x12\x10\n\x0cUPSCALER_RGB\x10\x00\x12\x13\n\x0fUPSCALER_GFPGAN\x10\x01\x12\x13\n\x0fUPSCALER_ESRGAN\x10\x02*\xd8\x01\n\x0eGuidancePreset\x12\x18\n\x14GUIDANCE_PRESET_NONE\x10\x00\x12\x1a\n\x16GUIDANCE_PRESET_SIMPLE\x10\x01\x12\x1d\n\x19GUIDANCE_PRESET_FAST_BLUE\x10\x02\x12\x1e\n\x1aGUIDANCE_PRESET_FAST_GREEN\x10\x03\x12\x18\n\x14GUIDANCE_PRESET_SLOW\x10\x04\x12\x1a\n\x16GUIDANCE_PRESET_SLOWER\x10\x05\x12\x1b\n\x17GUIDANCE_PRESET_SLOWEST\x10\x06*\x91\x01\n\x11ModelArchitecture\x12\x1b\n\x17MODEL_ARCHITECTURE_NONE\x10\x00\x12\x1f\n\x1bMODEL_ARCHITECTURE_CLIP_VIT\x10\x01\x12\"\n\x1eMODEL_ARCHITECTURE_CLIP_RESNET\x10\x02\x12\x1a\n\x16MODEL_ARCHITECTURE_LDM\x10\x03*\xa2\x01\n\x06\x41\x63tion\x12\x16\n\x12\x41\x43TION_PASSTHROUGH\x10\x00\x12\x1f\n\x1b\x41\x43TION_REGENERATE_DUPLICATE\x10\x01\x12\x15\n\x11\x41\x43TION_REGENERATE\x10\x02\x12\x1e\n\x1a\x41\x43TION_OBFUSCATE_DUPLICATE\x10\x03\x12\x14\n\x10\x41\x43TION_OBFUSCATE\x10\x04\x12\x12\n\x0e\x41\x43TION_DISCARD\x10\x05*D\n\x0e\x43lassifierMode\x12\x17\n\x13\x43LSFR_MODE_ZEROSHOT\x10\x00\x12\x19\n\x15\x43LSFR_MODE_MULTICLASS\x10\x01*X\n\nBorderMode\x12\x12\n\x0e\x42ORDER_REFLECT\x10\x00\x12\x14\n\x10\x42ORDER_REPLICATE\x10\x01\x12\x0f\n\x0b\x42ORDER_WRAP\x10\x02\x12\x0f\n\x0b\x42ORDER_ZERO\x10\x03*O\n\x0e\x43olorMatchMode\x12\x13\n\x0f\x43OLOR_MATCH_HSV\x10\x00\x12\x13\n\x0f\x43OLOR_MATCH_LAB\x10\x01\x12\x13\n\x0f\x43OLOR_MATCH_RGB\x10\x02*=\n\x0b\x41ssetAction\x12\r\n\tASSET_PUT\x10\x00\x12\r\n\tASSET_GET\x10\x01\x12\x10\n\x0c\x41SSET_DELETE\x10\x02*\x81\x01\n\x08\x41ssetUse\x12\x17\n\x13\x41SSET_USE_UNDEFINED\x10\x00\x12\x13\n\x0f\x41SSET_USE_INPUT\x10\x01\x12\x14\n\x10\x41SSET_USE_OUTPUT\x10\x02\x12\x1a\n\x16\x41SSET_USE_INTERMEDIATE\x10\x03\x12\x15\n\x11\x41SSET_USE_PROJECT\x10\x04*W\n\x0bStageAction\x12\x15\n\x11STAGE_ACTION_PASS\x10\x00\x12\x18\n\x14STAGE_ACTION_DISCARD\x10\x01\x12\x17\n\x13STAGE_ACTION_RETURN\x10\x02\x32\x83\x01\n\x11GenerationService\x12\x31\n\x08Generate\x12\x10.gooseai.Request\x1a\x0f.gooseai.Answer\"\x00\x30\x01\x12;\n\rChainGenerate\x12\x15.gooseai.ChainRequest\x1a\x0f.gooseai.Answer\"\x00\x30\x01\x42\x0fZ\r./;generationb\x06proto3')

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
_BORDERMODE = DESCRIPTOR.enum_types_by_name['BorderMode']
BorderMode = enum_type_wrapper.EnumTypeWrapper(_BORDERMODE)
_COLORMATCHMODE = DESCRIPTOR.enum_types_by_name['ColorMatchMode']
ColorMatchMode = enum_type_wrapper.EnumTypeWrapper(_COLORMATCHMODE)
_ASSETACTION = DESCRIPTOR.enum_types_by_name['AssetAction']
AssetAction = enum_type_wrapper.EnumTypeWrapper(_ASSETACTION)
_ASSETUSE = DESCRIPTOR.enum_types_by_name['AssetUse']
AssetUse = enum_type_wrapper.EnumTypeWrapper(_ASSETUSE)
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
GUIDANCE_PRESET_SIMPLE = 1
GUIDANCE_PRESET_FAST_BLUE = 2
GUIDANCE_PRESET_FAST_GREEN = 3
GUIDANCE_PRESET_SLOW = 4
GUIDANCE_PRESET_SLOWER = 5
GUIDANCE_PRESET_SLOWEST = 6
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
BORDER_REFLECT = 0
BORDER_REPLICATE = 1
BORDER_WRAP = 2
BORDER_ZERO = 3
COLOR_MATCH_HSV = 0
COLOR_MATCH_LAB = 1
COLOR_MATCH_RGB = 2
ASSET_PUT = 0
ASSET_GET = 1
ASSET_DELETE = 2
ASSET_USE_UNDEFINED = 0
ASSET_USE_INPUT = 1
ASSET_USE_OUTPUT = 2
ASSET_USE_INTERMEDIATE = 3
ASSET_USE_PROJECT = 4
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
_GUIDANCESCHEDULEPARAMETERS = DESCRIPTOR.message_types_by_name['GuidanceScheduleParameters']
_GUIDANCEINSTANCEPARAMETERS = DESCRIPTOR.message_types_by_name['GuidanceInstanceParameters']
_GUIDANCEPARAMETERS = DESCRIPTOR.message_types_by_name['GuidanceParameters']
_TRANSFORMTYPE = DESCRIPTOR.message_types_by_name['TransformType']
_IMAGEPARAMETERS = DESCRIPTOR.message_types_by_name['ImageParameters']
_CLASSIFIERCONCEPT = DESCRIPTOR.message_types_by_name['ClassifierConcept']
_CLASSIFIERCATEGORY = DESCRIPTOR.message_types_by_name['ClassifierCategory']
_CLASSIFIERPARAMETERS = DESCRIPTOR.message_types_by_name['ClassifierParameters']
_TRANSFORMADDNOISE = DESCRIPTOR.message_types_by_name['TransformAddNoise']
_TRANSFORMBLEND = DESCRIPTOR.message_types_by_name['TransformBlend']
_TRANSFORMCOLORMATCH = DESCRIPTOR.message_types_by_name['TransformColorMatch']
_TRANSFORMCONTRAST = DESCRIPTOR.message_types_by_name['TransformContrast']
_TRANSFORMDEPTHCALC = DESCRIPTOR.message_types_by_name['TransformDepthCalc']
_TRANSFORMWARP2D = DESCRIPTOR.message_types_by_name['TransformWarp2d']
_TRANSFORMWARP3D = DESCRIPTOR.message_types_by_name['TransformWarp3d']
_TRANSFORMWARPFLOW = DESCRIPTOR.message_types_by_name['TransformWarpFlow']
_TRANSFORMOPERATION = DESCRIPTOR.message_types_by_name['TransformOperation']
_TRANSFORMSEQUENCE = DESCRIPTOR.message_types_by_name['TransformSequence']
_ASSETPARAMETERS = DESCRIPTOR.message_types_by_name['AssetParameters']
_ANSWERMETA = DESCRIPTOR.message_types_by_name['AnswerMeta']
_ANSWER = DESCRIPTOR.message_types_by_name['Answer']
_INTERPOLATEPARAMETERS = DESCRIPTOR.message_types_by_name['InterpolateParameters']
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

GuidanceScheduleParameters = _reflection.GeneratedProtocolMessageType('GuidanceScheduleParameters', (_message.Message,), {
  'DESCRIPTOR' : _GUIDANCESCHEDULEPARAMETERS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.GuidanceScheduleParameters)
  })
_sym_db.RegisterMessage(GuidanceScheduleParameters)

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

TransformAddNoise = _reflection.GeneratedProtocolMessageType('TransformAddNoise', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORMADDNOISE,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.TransformAddNoise)
  })
_sym_db.RegisterMessage(TransformAddNoise)

TransformBlend = _reflection.GeneratedProtocolMessageType('TransformBlend', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORMBLEND,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.TransformBlend)
  })
_sym_db.RegisterMessage(TransformBlend)

TransformColorMatch = _reflection.GeneratedProtocolMessageType('TransformColorMatch', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORMCOLORMATCH,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.TransformColorMatch)
  })
_sym_db.RegisterMessage(TransformColorMatch)

TransformContrast = _reflection.GeneratedProtocolMessageType('TransformContrast', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORMCONTRAST,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.TransformContrast)
  })
_sym_db.RegisterMessage(TransformContrast)

TransformDepthCalc = _reflection.GeneratedProtocolMessageType('TransformDepthCalc', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORMDEPTHCALC,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.TransformDepthCalc)
  })
_sym_db.RegisterMessage(TransformDepthCalc)

TransformWarp2d = _reflection.GeneratedProtocolMessageType('TransformWarp2d', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORMWARP2D,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.TransformWarp2d)
  })
_sym_db.RegisterMessage(TransformWarp2d)

TransformWarp3d = _reflection.GeneratedProtocolMessageType('TransformWarp3d', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORMWARP3D,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.TransformWarp3d)
  })
_sym_db.RegisterMessage(TransformWarp3d)

TransformWarpFlow = _reflection.GeneratedProtocolMessageType('TransformWarpFlow', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORMWARPFLOW,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.TransformWarpFlow)
  })
_sym_db.RegisterMessage(TransformWarpFlow)

TransformOperation = _reflection.GeneratedProtocolMessageType('TransformOperation', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORMOPERATION,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.TransformOperation)
  })
_sym_db.RegisterMessage(TransformOperation)

TransformSequence = _reflection.GeneratedProtocolMessageType('TransformSequence', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORMSEQUENCE,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.TransformSequence)
  })
_sym_db.RegisterMessage(TransformSequence)

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

InterpolateParameters = _reflection.GeneratedProtocolMessageType('InterpolateParameters', (_message.Message,), {
  'DESCRIPTOR' : _INTERPOLATEPARAMETERS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.InterpolateParameters)
  })
_sym_db.RegisterMessage(InterpolateParameters)

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
  _FINISHREASON._serialized_start=5929
  _FINISHREASON._serialized_end=5998
  _ARTIFACTTYPE._serialized_start=6001
  _ARTIFACTTYPE._serialized_end=6187
  _DIFFUSIONSAMPLER._serialized_start=6190
  _DIFFUSIONSAMPLER._serialized_end=6387
  _UPSCALER._serialized_start=6389
  _UPSCALER._serialized_end=6459
  _GUIDANCEPRESET._serialized_start=6462
  _GUIDANCEPRESET._serialized_end=6678
  _MODELARCHITECTURE._serialized_start=6681
  _MODELARCHITECTURE._serialized_end=6826
  _ACTION._serialized_start=6829
  _ACTION._serialized_end=6991
  _CLASSIFIERMODE._serialized_start=6993
  _CLASSIFIERMODE._serialized_end=7061
  _BORDERMODE._serialized_start=7063
  _BORDERMODE._serialized_end=7151
  _COLORMATCHMODE._serialized_start=7153
  _COLORMATCHMODE._serialized_end=7232
  _ASSETACTION._serialized_start=7234
  _ASSETACTION._serialized_end=7295
  _ASSETUSE._serialized_start=7298
  _ASSETUSE._serialized_end=7427
  _STAGEACTION._serialized_start=7429
  _STAGEACTION._serialized_end=7516
  _TOKEN._serialized_start=29
  _TOKEN._serialized_end=76
  _TOKENS._serialized_start=78
  _TOKENS._serialized_end=162
  _ARTIFACT._serialized_start=165
  _ARTIFACT._serialized_end=501
  _PROMPTPARAMETERS._serialized_start=503
  _PROMPTPARAMETERS._serialized_end=581
  _PROMPT._serialized_start=584
  _PROMPT._serialized_end=759
  _SAMPLERPARAMETERS._serialized_start=762
  _SAMPLERPARAMETERS._serialized_end=1053
  _CONDITIONERPARAMETERS._serialized_start=1056
  _CONDITIONERPARAMETERS._serialized_end=1195
  _SCHEDULEPARAMETERS._serialized_start=1197
  _SCHEDULEPARAMETERS._serialized_end=1303
  _STEPPARAMETER._serialized_start=1306
  _STEPPARAMETER._serialized_end=1534
  _MODEL._serialized_start=1537
  _MODEL._serialized_end=1688
  _CUTOUTPARAMETERS._serialized_start=1691
  _CUTOUTPARAMETERS._serialized_end=1879
  _GUIDANCESCHEDULEPARAMETERS._serialized_start=1881
  _GUIDANCESCHEDULEPARAMETERS._serialized_end=1942
  _GUIDANCEINSTANCEPARAMETERS._serialized_start=1945
  _GUIDANCEINSTANCEPARAMETERS._serialized_end=2224
  _GUIDANCEPARAMETERS._serialized_start=2226
  _GUIDANCEPARAMETERS._serialized_end=2352
  _TRANSFORMTYPE._serialized_start=2355
  _TRANSFORMTYPE._serialized_end=2513
  _IMAGEPARAMETERS._serialized_start=2516
  _IMAGEPARAMETERS._serialized_end=2779
  _CLASSIFIERCONCEPT._serialized_start=2781
  _CLASSIFIERCONCEPT._serialized_end=2855
  _CLASSIFIERCATEGORY._serialized_start=2858
  _CLASSIFIERCATEGORY._serialized_end=3102
  _CLASSIFIERPARAMETERS._serialized_start=3105
  _CLASSIFIERPARAMETERS._serialized_end=3289
  _TRANSFORMADDNOISE._serialized_start=3291
  _TRANSFORMADDNOISE._serialized_end=3354
  _TRANSFORMBLEND._serialized_start=3356
  _TRANSFORMBLEND._serialized_end=3423
  _TRANSFORMCOLORMATCH._serialized_start=3425
  _TRANSFORMCOLORMATCH._serialized_end=3525
  _TRANSFORMCONTRAST._serialized_start=3527
  _TRANSFORMCONTRAST._serialized_end=3622
  _TRANSFORMDEPTHCALC._serialized_start=3624
  _TRANSFORMDEPTHCALC._serialized_end=3720
  _TRANSFORMWARP2D._serialized_start=3723
  _TRANSFORMWARP2D._serialized_end=3855
  _TRANSFORMWARP3D._serialized_start=3858
  _TRANSFORMWARP3D._serialized_end=4086
  _TRANSFORMWARPFLOW._serialized_start=4089
  _TRANSFORMWARPFLOW._serialized_end=4281
  _TRANSFORMOPERATION._serialized_start=4284
  _TRANSFORMOPERATION._serialized_end=4693
  _TRANSFORMSEQUENCE._serialized_start=4695
  _TRANSFORMSEQUENCE._serialized_end=4763
  _ASSETPARAMETERS._serialized_start=4765
  _ASSETPARAMETERS._serialized_end=4872
  _ANSWERMETA._serialized_start=4875
  _ANSWERMETA._serialized_end=5023
  _ANSWER._serialized_start=5026
  _ANSWER._serialized_end=5195
  _INTERPOLATEPARAMETERS._serialized_start=5197
  _INTERPOLATEPARAMETERS._serialized_end=5236
  _REQUEST._serialized_start=5239
  _REQUEST._serialized_end=5645
  _ONSTATUS._serialized_start=5647
  _ONSTATUS._serialized_end=5766
  _STAGE._serialized_start=5768
  _STAGE._serialized_end=5860
  _CHAINREQUEST._serialized_start=5862
  _CHAINREQUEST._serialized_end=5927
  _GENERATIONSERVICE._serialized_start=7519
  _GENERATIONSERVICE._serialized_end=7650
# @@protoc_insertion_point(module_scope)
