import kubernetes.client
import typing

class V1StorageClassList:
    api_version: str
    items: list[kubernetes.client.V1StorageClass]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1StorageClass],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1StorageClassListDict: ...

class V1StorageClassListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1StorageClassDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
