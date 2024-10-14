import kubernetes.client
import typing

class V1PersistentVolume:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    spec: kubernetes.client.V1PersistentVolumeSpec
    status: kubernetes.client.V1PersistentVolumeStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1PersistentVolumeSpec] = ...,
        status: typing.Optional[kubernetes.client.V1PersistentVolumeStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> V1PersistentVolumeDict: ...

class V1PersistentVolumeDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    spec: kubernetes.client.V1PersistentVolumeSpecDict
    status: kubernetes.client.V1PersistentVolumeStatusDict
