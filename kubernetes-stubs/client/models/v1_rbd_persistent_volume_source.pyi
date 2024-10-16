import kubernetes.client
import typing

class V1RBDPersistentVolumeSource:
    fs_type: typing.Optional[str]
    image: str
    keyring: typing.Optional[str]
    monitors: list[str]
    pool: typing.Optional[str]
    read_only: typing.Optional[bool]
    secret_ref: typing.Optional[kubernetes.client.V1SecretReference]
    user: typing.Optional[str]

    def __init__(
        self,
        *,
        fs_type: typing.Optional[str] = ...,
        image: str,
        keyring: typing.Optional[str] = ...,
        monitors: list[str],
        pool: typing.Optional[str] = ...,
        read_only: typing.Optional[bool] = ...,
        secret_ref: typing.Optional[kubernetes.client.V1SecretReference] = ...,
        user: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1RBDPersistentVolumeSourceDict: ...

class V1RBDPersistentVolumeSourceDict(typing.TypedDict, total=False):
    fsType: str
    image: str
    keyring: str
    monitors: list[str]
    pool: str
    readOnly: bool
    secretRef: kubernetes.client.V1SecretReferenceDict
    user: str
