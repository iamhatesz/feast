"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Aggregation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COLUMN_FIELD_NUMBER: builtins.int
    FUNCTION_FIELD_NUMBER: builtins.int
    TIME_WINDOW_FIELD_NUMBER: builtins.int
    SLIDE_INTERVAL_FIELD_NUMBER: builtins.int
    column: builtins.str
    function: builtins.str
    @property
    def time_window(self) -> google.protobuf.duration_pb2.Duration: ...
    @property
    def slide_interval(self) -> google.protobuf.duration_pb2.Duration: ...
    def __init__(
        self,
        *,
        column: builtins.str = ...,
        function: builtins.str = ...,
        time_window: google.protobuf.duration_pb2.Duration | None = ...,
        slide_interval: google.protobuf.duration_pb2.Duration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["slide_interval", b"slide_interval", "time_window", b"time_window"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["column", b"column", "function", b"function", "slide_interval", b"slide_interval", "time_window", b"time_window"]) -> None: ...

global___Aggregation = Aggregation
