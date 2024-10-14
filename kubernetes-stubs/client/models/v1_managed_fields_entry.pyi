import datetime
import typing

class V1ManagedFieldsEntry:
    api_version: str
    fields_type: typing.Optional[str]
    fields_v1: typing.Optional[typing.Any]
    manager: typing.Optional[str]
    operation: typing.Optional[str]
    subresource: typing.Optional[str]
    time: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        fields_type: typing.Optional[str] = ...,
        fields_v1: typing.Optional[typing.Any] = ...,
        manager: typing.Optional[str] = ...,
        operation: typing.Optional[str] = ...,
        subresource: typing.Optional[str] = ...,
        time: typing.Optional[datetime.datetime] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ManagedFieldsEntryDict: ...

class V1ManagedFieldsEntryDict(typing.TypedDict, total=False):
    apiVersion: str
    fieldsType: str
    fieldsV1: typing.Any
    manager: str
    operation: str
    subresource: str
    time: datetime.datetime
