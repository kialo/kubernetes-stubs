import kubernetes.client
import typing

class V1StorageOSVolumeSource:
    fs_type: typing.Optional[str]
    read_only: typing.Optional[bool]
    secret_ref: typing.Optional[kubernetes.client.V1LocalObjectReference]
    volume_name: typing.Optional[str]
    volume_namespace: typing.Optional[str]

    def __init__(
        self,
        *,
        fs_type: typing.Optional[str] = ...,
        read_only: typing.Optional[bool] = ...,
        secret_ref: typing.Optional[kubernetes.client.V1LocalObjectReference] = ...,
        volume_name: typing.Optional[str] = ...,
        volume_namespace: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1StorageOSVolumeSourceDict: ...

class V1StorageOSVolumeSourceDict(typing.TypedDict, total=False):
    fsType: str
    readOnly: bool
    secretRef: kubernetes.client.V1LocalObjectReferenceDict
    volumeName: str
    volumeNamespace: str
