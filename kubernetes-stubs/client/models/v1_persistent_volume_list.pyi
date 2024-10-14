import kubernetes.client
import typing

class V1PersistentVolumeList:
    api_version: str
    items: list[kubernetes.client.V1PersistentVolume]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1PersistentVolume],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1PersistentVolumeListDict: ...

class V1PersistentVolumeListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1PersistentVolumeDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
