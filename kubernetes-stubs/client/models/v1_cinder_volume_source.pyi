import kubernetes.client
import typing

class V1CinderVolumeSource:
    fs_type: typing.Optional[str]
    read_only: typing.Optional[bool]
    secret_ref: typing.Optional[kubernetes.client.V1LocalObjectReference]
    volume_id: str

    def __init__(
        self,
        *,
        fs_type: typing.Optional[str] = ...,
        read_only: typing.Optional[bool] = ...,
        secret_ref: typing.Optional[kubernetes.client.V1LocalObjectReference] = ...,
        volume_id: str,
    ) -> None: ...
    def to_dict(self) -> V1CinderVolumeSourceDict: ...

class V1CinderVolumeSourceDict(typing.TypedDict, total=False):
    fsType: str
    readOnly: bool
    secretRef: kubernetes.client.V1LocalObjectReferenceDict
    volumeID: str
