import kubernetes.client
import typing

class V1CSIStorageCapacityList:
    api_version: str
    items: list[kubernetes.client.V1CSIStorageCapacity]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1CSIStorageCapacity],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1CSIStorageCapacityListDict: ...

class V1CSIStorageCapacityListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1CSIStorageCapacityDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
