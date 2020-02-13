# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common.proto',
  package='hiota',
  syntax='proto3',
  serialized_options=_b('\n\037com.hitachivantara.hiota.modelsP\001ZBgitlab-edge.eng.hitachivantara.com/pandora/shared/proto/pkg/models\370\001\001\242\002\013HiotaModels\252\002\033HitachiVantara.Hiota.Models'),
  serialized_pb=_b('\n\x0c\x63ommon.proto\x12\x05hiota\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc8\x02\n\x05Value\x12\x10\n\x06sint32\x18\x01 \x01(\x11H\x00\x12\x10\n\x06sint64\x18\x02 \x01(\x12H\x00\x12\x10\n\x06uint32\x18\x03 \x01(\rH\x00\x12\x10\n\x06uint64\x18\x04 \x01(\x04H\x00\x12\x11\n\x07\x66loat32\x18\x05 \x01(\x02H\x00\x12\x11\n\x07\x66loat64\x18\x06 \x01(\x01H\x00\x12\x11\n\x07\x62oolean\x18\x07 \x01(\x08H\x00\x12\x10\n\x06string\x18\x08 \x01(\tH\x00\x12\x10\n\x06\x62inary\x18\t \x01(\x0cH\x00\x12\x0e\n\x04json\x18\n \x01(\tH\x00\x12/\n\ttimestamp\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x12#\n\x08location\x18\x0c \x01(\x0b\x32\x0f.hiota.LocationH\x00\x12&\n\x06\x63ustom\x18\x14 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x42\x0c\n\ntypedValue\"/\n\x08Location\x12\x10\n\x08latitude\x18\x01 \x01(\x01\x12\x11\n\tlongitude\x18\x02 \x01(\x01\x42\x96\x01\n\x1f\x63om.hitachivantara.hiota.modelsP\x01ZBgitlab-edge.eng.hitachivantara.com/pandora/shared/proto/pkg/models\xf8\x01\x01\xa2\x02\x0bHiotaModels\xaa\x02\x1bHitachiVantara.Hiota.Modelsb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_VALUE = _descriptor.Descriptor(
  name='Value',
  full_name='hiota.Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sint32', full_name='hiota.Value.sint32', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sint64', full_name='hiota.Value.sint64', index=1,
      number=2, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uint32', full_name='hiota.Value.uint32', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uint64', full_name='hiota.Value.uint64', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float32', full_name='hiota.Value.float32', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float64', full_name='hiota.Value.float64', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boolean', full_name='hiota.Value.boolean', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string', full_name='hiota.Value.string', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='binary', full_name='hiota.Value.binary', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='json', full_name='hiota.Value.json', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='hiota.Value.timestamp', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='hiota.Value.location', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='custom', full_name='hiota.Value.custom', index=12,
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
    _descriptor.OneofDescriptor(
      name='typedValue', full_name='hiota.Value.typedValue',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=84,
  serialized_end=412,
)


_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='hiota.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='hiota.Location.latitude', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='hiota.Location.longitude', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=414,
  serialized_end=461,
)

_VALUE.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_VALUE.fields_by_name['location'].message_type = _LOCATION
_VALUE.fields_by_name['custom'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_VALUE.oneofs_by_name['typedValue'].fields.append(
  _VALUE.fields_by_name['sint32'])
_VALUE.fields_by_name['sint32'].containing_oneof = _VALUE.oneofs_by_name['typedValue']
_VALUE.oneofs_by_name['typedValue'].fields.append(
  _VALUE.fields_by_name['sint64'])
_VALUE.fields_by_name['sint64'].containing_oneof = _VALUE.oneofs_by_name['typedValue']
_VALUE.oneofs_by_name['typedValue'].fields.append(
  _VALUE.fields_by_name['uint32'])
_VALUE.fields_by_name['uint32'].containing_oneof = _VALUE.oneofs_by_name['typedValue']
_VALUE.oneofs_by_name['typedValue'].fields.append(
  _VALUE.fields_by_name['uint64'])
_VALUE.fields_by_name['uint64'].containing_oneof = _VALUE.oneofs_by_name['typedValue']
_VALUE.oneofs_by_name['typedValue'].fields.append(
  _VALUE.fields_by_name['float32'])
_VALUE.fields_by_name['float32'].containing_oneof = _VALUE.oneofs_by_name['typedValue']
_VALUE.oneofs_by_name['typedValue'].fields.append(
  _VALUE.fields_by_name['float64'])
_VALUE.fields_by_name['float64'].containing_oneof = _VALUE.oneofs_by_name['typedValue']
_VALUE.oneofs_by_name['typedValue'].fields.append(
  _VALUE.fields_by_name['boolean'])
_VALUE.fields_by_name['boolean'].containing_oneof = _VALUE.oneofs_by_name['typedValue']
_VALUE.oneofs_by_name['typedValue'].fields.append(
  _VALUE.fields_by_name['string'])
_VALUE.fields_by_name['string'].containing_oneof = _VALUE.oneofs_by_name['typedValue']
_VALUE.oneofs_by_name['typedValue'].fields.append(
  _VALUE.fields_by_name['binary'])
_VALUE.fields_by_name['binary'].containing_oneof = _VALUE.oneofs_by_name['typedValue']
_VALUE.oneofs_by_name['typedValue'].fields.append(
  _VALUE.fields_by_name['json'])
_VALUE.fields_by_name['json'].containing_oneof = _VALUE.oneofs_by_name['typedValue']
_VALUE.oneofs_by_name['typedValue'].fields.append(
  _VALUE.fields_by_name['timestamp'])
_VALUE.fields_by_name['timestamp'].containing_oneof = _VALUE.oneofs_by_name['typedValue']
_VALUE.oneofs_by_name['typedValue'].fields.append(
  _VALUE.fields_by_name['location'])
_VALUE.fields_by_name['location'].containing_oneof = _VALUE.oneofs_by_name['typedValue']
_VALUE.oneofs_by_name['typedValue'].fields.append(
  _VALUE.fields_by_name['custom'])
_VALUE.fields_by_name['custom'].containing_oneof = _VALUE.oneofs_by_name['typedValue']
DESCRIPTOR.message_types_by_name['Value'] = _VALUE
DESCRIPTOR.message_types_by_name['Location'] = _LOCATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), dict(
  DESCRIPTOR = _VALUE,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:hiota.Value)
  ))
_sym_db.RegisterMessage(Value)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), dict(
  DESCRIPTOR = _LOCATION,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:hiota.Location)
  ))
_sym_db.RegisterMessage(Location)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
