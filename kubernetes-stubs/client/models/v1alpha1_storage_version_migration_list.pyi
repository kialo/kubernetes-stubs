import kubernetes.client
import typing

class V1alpha1StorageVersionMigrationList:
    api_version: str
    items: list[kubernetes.client.V1alpha1StorageVersionMigration]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1alpha1StorageVersionMigration],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha1StorageVersionMigrationListDict: ...

class V1alpha1StorageVersionMigrationListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1alpha1StorageVersionMigrationDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
