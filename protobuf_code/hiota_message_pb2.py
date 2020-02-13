# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hiota_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
import it_data_pb2 as it__data__pb2
import ot_data_pb2 as ot__data__pb2
import alert_data_pb2 as alert__data__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hiota_message.proto',
  package='hiota',
  syntax='proto3',
  serialized_options=_b('\n\037com.hitachivantara.hiota.modelsP\001ZBgitlab-edge.eng.hitachivantara.com/pandora/shared/proto/pkg/models\370\001\001\242\002\013HiotaModels\252\002\033HitachiVantara.Hiota.Models'),
  serialized_pb=_b('\n\x13hiota_message.proto\x12\x05hiota\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\rit_data.proto\x1a\rot_data.proto\x1a\x10\x61lert_data.proto\"\xfc\x01\n\x0cHiotaMessage\x12\n\n\x02id\x18\x01 \x01(\t\x12+\n\x07\x63reated\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08trace_id\x18\x03 \x03(\t\x12\x15\n\rerror_message\x18\x04 \x01(\t\x12$\n\nasset_info\x18\t \x01(\x0b\x32\x10.hiota.AssetInfo\x12\x1e\n\x07ot_data\x18\n \x01(\x0b\x32\r.hiota.OTData\x12\x1e\n\x07it_data\x18\x0b \x01(\x0b\x32\r.hiota.ITData\x12$\n\nalert_data\x18\x14 \x01(\x0b\x32\x10.hiota.AlertData\"&\n\tAssetInfo\x12\x0b\n\x03urn\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\tB\x96\x01\n\x1f\x63om.hitachivantara.hiota.modelsP\x01ZBgitlab-edge.eng.hitachivantara.com/pandora/shared/proto/pkg/models\xf8\x01\x01\xa2\x02\x0bHiotaModels\xaa\x02\x1bHitachiVantara.Hiota.Modelsb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,it__data__pb2.DESCRIPTOR,ot__data__pb2.DESCRIPTOR,alert__data__pb2.DESCRIPTOR,])




_HIOTAMESSAGE = _descriptor.Descriptor(
  name='HiotaMessage',
  full_name='hiota.HiotaMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='hiota.HiotaMessage.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created', full_name='hiota.HiotaMessage.created', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trace_id', full_name='hiota.HiotaMessage.trace_id', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='hiota.HiotaMessage.error_message', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='asset_info', full_name='hiota.HiotaMessage.asset_info', index=4,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ot_data', full_name='hiota.HiotaMessage.ot_data', index=5,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='it_data', full_name='hiota.HiotaMessage.it_data', index=6,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alert_data', full_name='hiota.HiotaMessage.alert_data', index=7,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=364,
)


_ASSETINFO = _descriptor.Descriptor(
  name='AssetInfo',
  full_name='hiota.AssetInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='urn', full_name='hiota.AssetInfo.urn', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='hiota.AssetInfo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=366,
  serialized_end=404,
)

_HIOTAMESSAGE.fields_by_name['created'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_HIOTAMESSAGE.fields_by_name['asset_info'].message_type = _ASSETINFO
_HIOTAMESSAGE.fields_by_name['ot_data'].message_type = ot__data__pb2._OTDATA
_HIOTAMESSAGE.fields_by_name['it_data'].message_type = it__data__pb2._ITDATA
_HIOTAMESSAGE.fields_by_name['alert_data'].message_type = alert__data__pb2._ALERTDATA
DESCRIPTOR.message_types_by_name['HiotaMessage'] = _HIOTAMESSAGE
DESCRIPTOR.message_types_by_name['AssetInfo'] = _ASSETINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HiotaMessage = _reflection.GeneratedProtocolMessageType('HiotaMessage', (_message.Message,), dict(
  DESCRIPTOR = _HIOTAMESSAGE,
  __module__ = 'hiota_message_pb2'
  # @@protoc_insertion_point(class_scope:hiota.HiotaMessage)
  ))
_sym_db.RegisterMessage(HiotaMessage)

AssetInfo = _reflection.GeneratedProtocolMessageType('AssetInfo', (_message.Message,), dict(
  DESCRIPTOR = _ASSETINFO,
  __module__ = 'hiota_message_pb2'
  # @@protoc_insertion_point(class_scope:hiota.AssetInfo)
  ))
_sym_db.RegisterMessage(AssetInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
