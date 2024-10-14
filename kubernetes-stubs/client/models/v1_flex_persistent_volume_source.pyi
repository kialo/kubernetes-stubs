import kubernetes.client
import typing

class V1FlexPersistentVolumeSource:
    driver: str
    fs_type: typing.Optional[str]
    options: typing.Optional[dict[str, str]]
    read_only: typing.Optional[bool]
    secret_ref: typing.Optional[kubernetes.client.V1SecretReference]

    def __init__(
        self,
        *,
        driver: str,
        fs_type: typing.Optional[str] = ...,
        options: typing.Optional[dict[str, str]] = ...,
        read_only: typing.Optional[bool] = ...,
        secret_ref: typing.Optional[kubernetes.client.V1SecretReference] = ...,
    ) -> None: ...
    def to_dict(self) -> V1FlexPersistentVolumeSourceDict: ...

class V1FlexPersistentVolumeSourceDict(typing.TypedDict, total=False):
    driver: str
    fsType: str
    options: dict[str, str]
    readOnly: bool
    secretRef: kubernetes.client.V1SecretReferenceDict
