# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/core/FeatureView.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from feast.protos.feast.core import DataSource_pb2 as feast_dot_core_dot_DataSource__pb2
from feast.protos.feast.core import Feature_pb2 as feast_dot_core_dot_Feature__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x66\x65\x61st/core/FeatureView.proto\x12\nfeast.core\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1b\x66\x65\x61st/core/DataSource.proto\x1a\x18\x66\x65\x61st/core/Feature.proto\"c\n\x0b\x46\x65\x61tureView\x12)\n\x04spec\x18\x01 \x01(\x0b\x32\x1b.feast.core.FeatureViewSpec\x12)\n\x04meta\x18\x02 \x01(\x0b\x32\x1b.feast.core.FeatureViewMeta\"\xbd\x03\n\x0f\x46\x65\x61tureViewSpec\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t\x12\x10\n\x08\x65ntities\x18\x03 \x03(\t\x12+\n\x08\x66\x65\x61tures\x18\x04 \x03(\x0b\x32\x19.feast.core.FeatureSpecV2\x12\x31\n\x0e\x65ntity_columns\x18\x0c \x03(\x0b\x32\x19.feast.core.FeatureSpecV2\x12\x13\n\x0b\x64\x65scription\x18\n \x01(\t\x12\x33\n\x04tags\x18\x05 \x03(\x0b\x32%.feast.core.FeatureViewSpec.TagsEntry\x12\r\n\x05owner\x18\x0b \x01(\t\x12&\n\x03ttl\x18\x06 \x01(\x0b\x32\x19.google.protobuf.Duration\x12,\n\x0c\x62\x61tch_source\x18\x07 \x01(\x0b\x32\x16.feast.core.DataSource\x12-\n\rstream_source\x18\t \x01(\x0b\x32\x16.feast.core.DataSource\x12\x0e\n\x06online\x18\x08 \x01(\x08\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xcc\x01\n\x0f\x46\x65\x61tureViewMeta\x12\x35\n\x11\x63reated_timestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12:\n\x16last_updated_timestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x46\n\x19materialization_intervals\x18\x03 \x03(\x0b\x32#.feast.core.MaterializationInterval\"w\n\x17MaterializationInterval\x12.\n\nstart_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"@\n\x0f\x46\x65\x61tureViewList\x12-\n\x0c\x66\x65\x61tureviews\x18\x01 \x03(\x0b\x32\x17.feast.core.FeatureViewBU\n\x10\x66\x65\x61st.proto.coreB\x10\x46\x65\x61tureViewProtoZ/github.com/feast-dev/feast/go/protos/feast/coreb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'feast.core.FeatureView_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\020feast.proto.coreB\020FeatureViewProtoZ/github.com/feast-dev/feast/go/protos/feast/core'
  _globals['_FEATUREVIEWSPEC_TAGSENTRY']._options = None
  _globals['_FEATUREVIEWSPEC_TAGSENTRY']._serialized_options = b'8\001'
  _globals['_FEATUREVIEW']._serialized_start=164
  _globals['_FEATUREVIEW']._serialized_end=263
  _globals['_FEATUREVIEWSPEC']._serialized_start=266
  _globals['_FEATUREVIEWSPEC']._serialized_end=711
  _globals['_FEATUREVIEWSPEC_TAGSENTRY']._serialized_start=668
  _globals['_FEATUREVIEWSPEC_TAGSENTRY']._serialized_end=711
  _globals['_FEATUREVIEWMETA']._serialized_start=714
  _globals['_FEATUREVIEWMETA']._serialized_end=918
  _globals['_MATERIALIZATIONINTERVAL']._serialized_start=920
  _globals['_MATERIALIZATIONINTERVAL']._serialized_end=1039
  _globals['_FEATUREVIEWLIST']._serialized_start=1041
  _globals['_FEATUREVIEWLIST']._serialized_end=1105
# @@protoc_insertion_point(module_scope)
