from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AwesomeMessage(_message.Message):
    __slots__ = ["awesome_field"]
    AWESOME_FIELD_FIELD_NUMBER: _ClassVar[int]
    awesome_field: str
    def __init__(self, awesome_field: _Optional[str] = ...) -> None: ...
