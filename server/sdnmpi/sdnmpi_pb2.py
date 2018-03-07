# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sdnmpi.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sdnmpi.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0csdnmpi.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xd8\x01\n\x03Job\x12\x0e\n\x06job_id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03uid\x18\x03 \x01(\r\x12\x0b\n\x03gid\x18\x04 \x01(\r\x12\x14\n\x0c\x63omm_pattern\x18\x05 \x01(\t\x12\x0f\n\x07n_tasks\x18\x06 \x01(\r\x12\x11\n\tn_running\x18\x07 \x01(\r\x12.\n\nstarted_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x66inished_at\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xac\x01\n\x07Process\x12\x0e\n\x06job_id\x18\x01 \x01(\r\x12\x0c\n\x04rank\x18\x02 \x01(\r\x12\x0f\n\x07node_id\x18\x03 \x01(\r\x12\x11\n\tnode_name\x18\x04 \x01(\t\x12.\n\nstarted_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x66inished_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"%\n\x0fListJobResponse\x12\x12\n\x04jobs\x18\x01 \x03(\x0b\x32\x04.Job\"\x1f\n\rGetJobRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\r\"#\n\x0eGetJobResponse\x12\x11\n\x03job\x18\x01 \x01(\x0b\x32\x04.Job\"%\n\x10\x43reateJobRequest\x12\x11\n\x03job\x18\x01 \x01(\x0b\x32\x04.Job\"!\n\x0fStartJobRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\r\"\"\n\x10\x46inishJobRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\r\"$\n\x12ListProcessRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\r\"2\n\x13ListProcessResponse\x12\x1b\n\tprocesses\x18\x01 \x03(\x0b\x32\x08.Process\"1\n\x11GetProcessRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\r\x12\x0c\n\x04rank\x18\x02 \x01(\r\"/\n\x12GetProcessResponse\x12\x19\n\x07process\x18\x01 \x01(\x0b\x32\x08.Process\"1\n\x14\x43reateProcessRequest\x12\x19\n\x07process\x18\x01 \x01(\x0b\x32\x08.Process\"3\n\x13StartProcessRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\r\x12\x0c\n\x04rank\x18\x02 \x01(\r\"4\n\x14\x46inishProcessRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\r\x12\x0c\n\x04rank\x18\x02 \x01(\r2\xd4\x04\n\x06SDNMPI\x12\x35\n\x07ListJob\x12\x16.google.protobuf.Empty\x1a\x10.ListJobResponse\"\x00\x12+\n\x06GetJob\x12\x0e.GetJobRequest\x1a\x0f.GetJobResponse\"\x00\x12\x38\n\tCreateJob\x12\x11.CreateJobRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x36\n\x08StartJob\x12\x10.StartJobRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x38\n\tFinishJob\x12\x11.FinishJobRequest\x1a\x16.google.protobuf.Empty\"\x00\x12=\n\x0bListProcess\x12\x16.google.protobuf.Empty\x1a\x14.ListProcessResponse\"\x00\x12\x37\n\nGetProcess\x12\x12.GetProcessRequest\x1a\x13.GetProcessResponse\"\x00\x12@\n\rCreateProcess\x12\x15.CreateProcessRequest\x1a\x16.google.protobuf.Empty\"\x00\x12>\n\x0cStartProcess\x12\x14.StartProcessRequest\x1a\x16.google.protobuf.Empty\"\x00\x12@\n\rFinishProcess\x12\x15.FinishProcessRequest\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_JOB = _descriptor.Descriptor(
  name='Job',
  full_name='Job',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_id', full_name='Job.job_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Job.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uid', full_name='Job.uid', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gid', full_name='Job.gid', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comm_pattern', full_name='Job.comm_pattern', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='n_tasks', full_name='Job.n_tasks', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='n_running', full_name='Job.n_running', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='started_at', full_name='Job.started_at', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='finished_at', full_name='Job.finished_at', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=295,
)


_PROCESS = _descriptor.Descriptor(
  name='Process',
  full_name='Process',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_id', full_name='Process.job_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rank', full_name='Process.rank', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_id', full_name='Process.node_id', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_name', full_name='Process.node_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='started_at', full_name='Process.started_at', index=4,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='finished_at', full_name='Process.finished_at', index=5,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=298,
  serialized_end=470,
)


_LISTJOBRESPONSE = _descriptor.Descriptor(
  name='ListJobResponse',
  full_name='ListJobResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jobs', full_name='ListJobResponse.jobs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=472,
  serialized_end=509,
)


_GETJOBREQUEST = _descriptor.Descriptor(
  name='GetJobRequest',
  full_name='GetJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_id', full_name='GetJobRequest.job_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=511,
  serialized_end=542,
)


_GETJOBRESPONSE = _descriptor.Descriptor(
  name='GetJobResponse',
  full_name='GetJobResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job', full_name='GetJobResponse.job', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=544,
  serialized_end=579,
)


_CREATEJOBREQUEST = _descriptor.Descriptor(
  name='CreateJobRequest',
  full_name='CreateJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job', full_name='CreateJobRequest.job', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=581,
  serialized_end=618,
)


_STARTJOBREQUEST = _descriptor.Descriptor(
  name='StartJobRequest',
  full_name='StartJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_id', full_name='StartJobRequest.job_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=620,
  serialized_end=653,
)


_FINISHJOBREQUEST = _descriptor.Descriptor(
  name='FinishJobRequest',
  full_name='FinishJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_id', full_name='FinishJobRequest.job_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=655,
  serialized_end=689,
)


_LISTPROCESSREQUEST = _descriptor.Descriptor(
  name='ListProcessRequest',
  full_name='ListProcessRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_id', full_name='ListProcessRequest.job_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=691,
  serialized_end=727,
)


_LISTPROCESSRESPONSE = _descriptor.Descriptor(
  name='ListProcessResponse',
  full_name='ListProcessResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='processes', full_name='ListProcessResponse.processes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=729,
  serialized_end=779,
)


_GETPROCESSREQUEST = _descriptor.Descriptor(
  name='GetProcessRequest',
  full_name='GetProcessRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_id', full_name='GetProcessRequest.job_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rank', full_name='GetProcessRequest.rank', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=781,
  serialized_end=830,
)


_GETPROCESSRESPONSE = _descriptor.Descriptor(
  name='GetProcessResponse',
  full_name='GetProcessResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='process', full_name='GetProcessResponse.process', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=832,
  serialized_end=879,
)


_CREATEPROCESSREQUEST = _descriptor.Descriptor(
  name='CreateProcessRequest',
  full_name='CreateProcessRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='process', full_name='CreateProcessRequest.process', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=881,
  serialized_end=930,
)


_STARTPROCESSREQUEST = _descriptor.Descriptor(
  name='StartProcessRequest',
  full_name='StartProcessRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_id', full_name='StartProcessRequest.job_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rank', full_name='StartProcessRequest.rank', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=932,
  serialized_end=983,
)


_FINISHPROCESSREQUEST = _descriptor.Descriptor(
  name='FinishProcessRequest',
  full_name='FinishProcessRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_id', full_name='FinishProcessRequest.job_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rank', full_name='FinishProcessRequest.rank', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=985,
  serialized_end=1037,
)

_JOB.fields_by_name['started_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_JOB.fields_by_name['finished_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_PROCESS.fields_by_name['started_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_PROCESS.fields_by_name['finished_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LISTJOBRESPONSE.fields_by_name['jobs'].message_type = _JOB
_GETJOBRESPONSE.fields_by_name['job'].message_type = _JOB
_CREATEJOBREQUEST.fields_by_name['job'].message_type = _JOB
_LISTPROCESSRESPONSE.fields_by_name['processes'].message_type = _PROCESS
_GETPROCESSRESPONSE.fields_by_name['process'].message_type = _PROCESS
_CREATEPROCESSREQUEST.fields_by_name['process'].message_type = _PROCESS
DESCRIPTOR.message_types_by_name['Job'] = _JOB
DESCRIPTOR.message_types_by_name['Process'] = _PROCESS
DESCRIPTOR.message_types_by_name['ListJobResponse'] = _LISTJOBRESPONSE
DESCRIPTOR.message_types_by_name['GetJobRequest'] = _GETJOBREQUEST
DESCRIPTOR.message_types_by_name['GetJobResponse'] = _GETJOBRESPONSE
DESCRIPTOR.message_types_by_name['CreateJobRequest'] = _CREATEJOBREQUEST
DESCRIPTOR.message_types_by_name['StartJobRequest'] = _STARTJOBREQUEST
DESCRIPTOR.message_types_by_name['FinishJobRequest'] = _FINISHJOBREQUEST
DESCRIPTOR.message_types_by_name['ListProcessRequest'] = _LISTPROCESSREQUEST
DESCRIPTOR.message_types_by_name['ListProcessResponse'] = _LISTPROCESSRESPONSE
DESCRIPTOR.message_types_by_name['GetProcessRequest'] = _GETPROCESSREQUEST
DESCRIPTOR.message_types_by_name['GetProcessResponse'] = _GETPROCESSRESPONSE
DESCRIPTOR.message_types_by_name['CreateProcessRequest'] = _CREATEPROCESSREQUEST
DESCRIPTOR.message_types_by_name['StartProcessRequest'] = _STARTPROCESSREQUEST
DESCRIPTOR.message_types_by_name['FinishProcessRequest'] = _FINISHPROCESSREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Job = _reflection.GeneratedProtocolMessageType('Job', (_message.Message,), dict(
  DESCRIPTOR = _JOB,
  __module__ = 'sdnmpi_pb2'
  # @@protoc_insertion_point(class_scope:Job)
  ))
_sym_db.RegisterMessage(Job)

Process = _reflection.GeneratedProtocolMessageType('Process', (_message.Message,), dict(
  DESCRIPTOR = _PROCESS,
  __module__ = 'sdnmpi_pb2'
  # @@protoc_insertion_point(class_scope:Process)
  ))
_sym_db.RegisterMessage(Process)

ListJobResponse = _reflection.GeneratedProtocolMessageType('ListJobResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTJOBRESPONSE,
  __module__ = 'sdnmpi_pb2'
  # @@protoc_insertion_point(class_scope:ListJobResponse)
  ))
_sym_db.RegisterMessage(ListJobResponse)

GetJobRequest = _reflection.GeneratedProtocolMessageType('GetJobRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETJOBREQUEST,
  __module__ = 'sdnmpi_pb2'
  # @@protoc_insertion_point(class_scope:GetJobRequest)
  ))
_sym_db.RegisterMessage(GetJobRequest)

GetJobResponse = _reflection.GeneratedProtocolMessageType('GetJobResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETJOBRESPONSE,
  __module__ = 'sdnmpi_pb2'
  # @@protoc_insertion_point(class_scope:GetJobResponse)
  ))
_sym_db.RegisterMessage(GetJobResponse)

CreateJobRequest = _reflection.GeneratedProtocolMessageType('CreateJobRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEJOBREQUEST,
  __module__ = 'sdnmpi_pb2'
  # @@protoc_insertion_point(class_scope:CreateJobRequest)
  ))
_sym_db.RegisterMessage(CreateJobRequest)

StartJobRequest = _reflection.GeneratedProtocolMessageType('StartJobRequest', (_message.Message,), dict(
  DESCRIPTOR = _STARTJOBREQUEST,
  __module__ = 'sdnmpi_pb2'
  # @@protoc_insertion_point(class_scope:StartJobRequest)
  ))
_sym_db.RegisterMessage(StartJobRequest)

FinishJobRequest = _reflection.GeneratedProtocolMessageType('FinishJobRequest', (_message.Message,), dict(
  DESCRIPTOR = _FINISHJOBREQUEST,
  __module__ = 'sdnmpi_pb2'
  # @@protoc_insertion_point(class_scope:FinishJobRequest)
  ))
_sym_db.RegisterMessage(FinishJobRequest)

ListProcessRequest = _reflection.GeneratedProtocolMessageType('ListProcessRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTPROCESSREQUEST,
  __module__ = 'sdnmpi_pb2'
  # @@protoc_insertion_point(class_scope:ListProcessRequest)
  ))
_sym_db.RegisterMessage(ListProcessRequest)

ListProcessResponse = _reflection.GeneratedProtocolMessageType('ListProcessResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTPROCESSRESPONSE,
  __module__ = 'sdnmpi_pb2'
  # @@protoc_insertion_point(class_scope:ListProcessResponse)
  ))
_sym_db.RegisterMessage(ListProcessResponse)

GetProcessRequest = _reflection.GeneratedProtocolMessageType('GetProcessRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETPROCESSREQUEST,
  __module__ = 'sdnmpi_pb2'
  # @@protoc_insertion_point(class_scope:GetProcessRequest)
  ))
_sym_db.RegisterMessage(GetProcessRequest)

GetProcessResponse = _reflection.GeneratedProtocolMessageType('GetProcessResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETPROCESSRESPONSE,
  __module__ = 'sdnmpi_pb2'
  # @@protoc_insertion_point(class_scope:GetProcessResponse)
  ))
_sym_db.RegisterMessage(GetProcessResponse)

CreateProcessRequest = _reflection.GeneratedProtocolMessageType('CreateProcessRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEPROCESSREQUEST,
  __module__ = 'sdnmpi_pb2'
  # @@protoc_insertion_point(class_scope:CreateProcessRequest)
  ))
_sym_db.RegisterMessage(CreateProcessRequest)

StartProcessRequest = _reflection.GeneratedProtocolMessageType('StartProcessRequest', (_message.Message,), dict(
  DESCRIPTOR = _STARTPROCESSREQUEST,
  __module__ = 'sdnmpi_pb2'
  # @@protoc_insertion_point(class_scope:StartProcessRequest)
  ))
_sym_db.RegisterMessage(StartProcessRequest)

FinishProcessRequest = _reflection.GeneratedProtocolMessageType('FinishProcessRequest', (_message.Message,), dict(
  DESCRIPTOR = _FINISHPROCESSREQUEST,
  __module__ = 'sdnmpi_pb2'
  # @@protoc_insertion_point(class_scope:FinishProcessRequest)
  ))
_sym_db.RegisterMessage(FinishProcessRequest)



_SDNMPI = _descriptor.ServiceDescriptor(
  name='SDNMPI',
  full_name='SDNMPI',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1040,
  serialized_end=1636,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListJob',
    full_name='SDNMPI.ListJob',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_LISTJOBRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetJob',
    full_name='SDNMPI.GetJob',
    index=1,
    containing_service=None,
    input_type=_GETJOBREQUEST,
    output_type=_GETJOBRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateJob',
    full_name='SDNMPI.CreateJob',
    index=2,
    containing_service=None,
    input_type=_CREATEJOBREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StartJob',
    full_name='SDNMPI.StartJob',
    index=3,
    containing_service=None,
    input_type=_STARTJOBREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FinishJob',
    full_name='SDNMPI.FinishJob',
    index=4,
    containing_service=None,
    input_type=_FINISHJOBREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListProcess',
    full_name='SDNMPI.ListProcess',
    index=5,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_LISTPROCESSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetProcess',
    full_name='SDNMPI.GetProcess',
    index=6,
    containing_service=None,
    input_type=_GETPROCESSREQUEST,
    output_type=_GETPROCESSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateProcess',
    full_name='SDNMPI.CreateProcess',
    index=7,
    containing_service=None,
    input_type=_CREATEPROCESSREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StartProcess',
    full_name='SDNMPI.StartProcess',
    index=8,
    containing_service=None,
    input_type=_STARTPROCESSREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FinishProcess',
    full_name='SDNMPI.FinishProcess',
    index=9,
    containing_service=None,
    input_type=_FINISHPROCESSREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SDNMPI)

DESCRIPTOR.services_by_name['SDNMPI'] = _SDNMPI

# @@protoc_insertion_point(module_scope)
