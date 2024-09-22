"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Policy(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    ROLE_BASED_POLICY_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the policy."""
    project: builtins.str
    """Name of Feast project."""
    @property
    def role_based_policy(self) -> global___RoleBasedPolicy: ...
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        project: builtins.str = ...,
        role_based_policy: global___RoleBasedPolicy | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["policy_type", b"policy_type", "role_based_policy", b"role_based_policy"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "policy_type", b"policy_type", "project", b"project", "role_based_policy", b"role_based_policy"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["policy_type", b"policy_type"]) -> typing_extensions.Literal["role_based_policy"] | None: ...

global___Policy = Policy

class RoleBasedPolicy(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROLES_FIELD_NUMBER: builtins.int
    @property
    def roles(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of roles in this policy."""
    def __init__(
        self,
        *,
        roles: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["roles", b"roles"]) -> None: ...

global___RoleBasedPolicy = RoleBasedPolicy
