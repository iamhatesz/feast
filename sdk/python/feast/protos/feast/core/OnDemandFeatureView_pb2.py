# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/core/OnDemandFeatureView.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from feast.protos.feast.core import FeatureView_pb2 as feast_dot_core_dot_FeatureView__pb2
from feast.protos.feast.core import FeatureViewProjection_pb2 as feast_dot_core_dot_FeatureViewProjection__pb2
from feast.protos.feast.core import Feature_pb2 as feast_dot_core_dot_Feature__pb2
from feast.protos.feast.core import DataSource_pb2 as feast_dot_core_dot_DataSource__pb2
from feast.protos.feast.core import Transformation_pb2 as feast_dot_core_dot_Transformation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$feast/core/OnDemandFeatureView.proto\x12\nfeast.core\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1c\x66\x65\x61st/core/FeatureView.proto\x1a&feast/core/FeatureViewProjection.proto\x1a\x18\x66\x65\x61st/core/Feature.proto\x1a\x1b\x66\x65\x61st/core/DataSource.proto\x1a\x1f\x66\x65\x61st/core/Transformation.proto\"{\n\x13OnDemandFeatureView\x12\x31\n\x04spec\x18\x01 \x01(\x0b\x32#.feast.core.OnDemandFeatureViewSpec\x12\x31\n\x04meta\x18\x02 \x01(\x0b\x32#.feast.core.OnDemandFeatureViewMeta\"\x99\x04\n\x17OnDemandFeatureViewSpec\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t\x12+\n\x08\x66\x65\x61tures\x18\x03 \x03(\x0b\x32\x19.feast.core.FeatureSpecV2\x12\x41\n\x07sources\x18\x04 \x03(\x0b\x32\x30.feast.core.OnDemandFeatureViewSpec.SourcesEntry\x12\x42\n\x15user_defined_function\x18\x05 \x01(\x0b\x32\x1f.feast.core.UserDefinedFunctionB\x02\x18\x01\x12\x43\n\x16\x66\x65\x61ture_transformation\x18\n \x01(\x0b\x32#.feast.core.FeatureTransformationV2\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12;\n\x04tags\x18\x07 \x03(\x0b\x32-.feast.core.OnDemandFeatureViewSpec.TagsEntry\x12\r\n\x05owner\x18\x08 \x01(\t\x12\x0c\n\x04mode\x18\x0b \x01(\t\x1aJ\n\x0cSourcesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.feast.core.OnDemandSource:\x02\x38\x01\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8c\x01\n\x17OnDemandFeatureViewMeta\x12\x35\n\x11\x63reated_timestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12:\n\x16last_updated_timestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xc8\x01\n\x0eOnDemandSource\x12/\n\x0c\x66\x65\x61ture_view\x18\x01 \x01(\x0b\x32\x17.feast.core.FeatureViewH\x00\x12\x44\n\x17\x66\x65\x61ture_view_projection\x18\x03 \x01(\x0b\x32!.feast.core.FeatureViewProjectionH\x00\x12\x35\n\x13request_data_source\x18\x02 \x01(\x0b\x32\x16.feast.core.DataSourceH\x00\x42\x08\n\x06source\"H\n\x13UserDefinedFunction\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x62ody\x18\x02 \x01(\x0c\x12\x11\n\tbody_text\x18\x03 \x01(\t:\x02\x18\x01\x42]\n\x10\x66\x65\x61st.proto.coreB\x18OnDemandFeatureViewProtoZ/github.com/feast-dev/feast/go/protos/feast/coreb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'feast.core.OnDemandFeatureView_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\020feast.proto.coreB\030OnDemandFeatureViewProtoZ/github.com/feast-dev/feast/go/protos/feast/core'
  _globals['_ONDEMANDFEATUREVIEWSPEC_SOURCESENTRY']._options = None
  _globals['_ONDEMANDFEATUREVIEWSPEC_SOURCESENTRY']._serialized_options = b'8\001'
  _globals['_ONDEMANDFEATUREVIEWSPEC_TAGSENTRY']._options = None
  _globals['_ONDEMANDFEATUREVIEWSPEC_TAGSENTRY']._serialized_options = b'8\001'
  _globals['_ONDEMANDFEATUREVIEWSPEC'].fields_by_name['user_defined_function']._options = None
  _globals['_ONDEMANDFEATUREVIEWSPEC'].fields_by_name['user_defined_function']._serialized_options = b'\030\001'
  _globals['_USERDEFINEDFUNCTION']._options = None
  _globals['_USERDEFINEDFUNCTION']._serialized_options = b'\030\001'
  _globals['_ONDEMANDFEATUREVIEW']._serialized_start=243
  _globals['_ONDEMANDFEATUREVIEW']._serialized_end=366
  _globals['_ONDEMANDFEATUREVIEWSPEC']._serialized_start=369
  _globals['_ONDEMANDFEATUREVIEWSPEC']._serialized_end=906
  _globals['_ONDEMANDFEATUREVIEWSPEC_SOURCESENTRY']._serialized_start=787
  _globals['_ONDEMANDFEATUREVIEWSPEC_SOURCESENTRY']._serialized_end=861
  _globals['_ONDEMANDFEATUREVIEWSPEC_TAGSENTRY']._serialized_start=863
  _globals['_ONDEMANDFEATUREVIEWSPEC_TAGSENTRY']._serialized_end=906
  _globals['_ONDEMANDFEATUREVIEWMETA']._serialized_start=909
  _globals['_ONDEMANDFEATUREVIEWMETA']._serialized_end=1049
  _globals['_ONDEMANDSOURCE']._serialized_start=1052
  _globals['_ONDEMANDSOURCE']._serialized_end=1252
  _globals['_USERDEFINEDFUNCTION']._serialized_start=1254
  _globals['_USERDEFINEDFUNCTION']._serialized_end=1326
# @@protoc_insertion_point(module_scope)
