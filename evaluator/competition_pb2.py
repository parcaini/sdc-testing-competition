# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: competition.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 27, 2, "", "competition.proto")
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x11\x63ompetition.proto"\x07\n\x05\x45mpty"\x19\n\tNameReply\x12\x0c\n\x04name\x18\x01 \x01(\t"\x1d\n\x0bSDCTestCase\x12\x0e\n\x06testId\x18\x01 \x01(\t"\x15\n\x13InitializationReply" \n\x0eSelectionReply\x12\x0e\n\x06testId\x18\x01 \x01(\t2\x94\x01\n\x0f\x43ompetitionTool\x12\x1c\n\x04Name\x12\x06.Empty\x1a\n.NameReply"\x00\x12\x34\n\nInitialize\x12\x0c.SDCTestCase\x1a\x14.InitializationReply"\x00(\x01\x12-\n\x06Select\x12\x0c.SDCTestCase\x1a\x0f.SelectionReply"\x00(\x01\x30\x01\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "competition_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals["_EMPTY"]._serialized_start = 21
    _globals["_EMPTY"]._serialized_end = 28
    _globals["_NAMEREPLY"]._serialized_start = 30
    _globals["_NAMEREPLY"]._serialized_end = 55
    _globals["_SDCTESTCASE"]._serialized_start = 57
    _globals["_SDCTESTCASE"]._serialized_end = 86
    _globals["_INITIALIZATIONREPLY"]._serialized_start = 88
    _globals["_INITIALIZATIONREPLY"]._serialized_end = 109
    _globals["_SELECTIONREPLY"]._serialized_start = 111
    _globals["_SELECTIONREPLY"]._serialized_end = 143
    _globals["_COMPETITIONTOOL"]._serialized_start = 146
    _globals["_COMPETITIONTOOL"]._serialized_end = 294
# @@protoc_insertion_point(module_scope)
