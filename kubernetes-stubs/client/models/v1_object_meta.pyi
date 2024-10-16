import datetime
import kubernetes.client
import typing

class V1ObjectMeta:
    annotations: typing.Optional[dict[str, str]]
    creation_timestamp: typing.Optional[datetime.datetime]
    deletion_grace_period_seconds: typing.Optional[int]
    deletion_timestamp: typing.Optional[datetime.datetime]
    finalizers: typing.Optional[list[str]]
    generate_name: typing.Optional[str]
    generation: typing.Optional[int]
    labels: dict[str, str]
    managed_fields: typing.Optional[list[kubernetes.client.V1ManagedFieldsEntry]]
    name: str
    namespace: str
    owner_references: typing.Optional[list[kubernetes.client.V1OwnerReference]]
    resource_version: typing.Optional[str]
    self_link: typing.Optional[str]
    uid: str

    def __init__(
        self,
        *,
        annotations: typing.Optional[dict[str, str]] = ...,
        creation_timestamp: typing.Optional[datetime.datetime] = ...,
        deletion_grace_period_seconds: typing.Optional[int] = ...,
        deletion_timestamp: typing.Optional[datetime.datetime] = ...,
        finalizers: typing.Optional[list[str]] = ...,
        generate_name: typing.Optional[str] = ...,
        generation: typing.Optional[int] = ...,
        labels: typing.Optional[dict[str, str]] = ...,
        managed_fields: typing.Optional[
            list[kubernetes.client.V1ManagedFieldsEntry]
        ] = ...,
        name: typing.Optional[str] = ...,
        namespace: typing.Optional[str] = ...,
        owner_references: typing.Optional[
            list[kubernetes.client.V1OwnerReference]
        ] = ...,
        resource_version: typing.Optional[str] = ...,
        self_link: typing.Optional[str] = ...,
        uid: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ObjectMetaDict: ...

class V1ObjectMetaDict(typing.TypedDict, total=False):
    annotations: dict[str, str]
    creationTimestamp: datetime.datetime
    deletionGracePeriodSeconds: int
    deletionTimestamp: datetime.datetime
    finalizers: list[str]
    generateName: str
    generation: int
    labels: dict[str, str]
    managedFields: list[kubernetes.client.V1ManagedFieldsEntryDict]
    name: str
    namespace: str
    ownerReferences: list[kubernetes.client.V1OwnerReferenceDict]
    resourceVersion: str
    selfLink: str
    uid: str
