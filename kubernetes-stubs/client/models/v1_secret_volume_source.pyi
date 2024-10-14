import kubernetes.client
import typing

class V1SecretVolumeSource:
    default_mode: typing.Optional[int]
    items: typing.Optional[list[kubernetes.client.V1KeyToPath]]
    optional: typing.Optional[bool]
    secret_name: typing.Optional[str]

    def __init__(
        self,
        *,
        default_mode: typing.Optional[int] = ...,
        items: typing.Optional[list[kubernetes.client.V1KeyToPath]] = ...,
        optional: typing.Optional[bool] = ...,
        secret_name: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1SecretVolumeSourceDict: ...

class V1SecretVolumeSourceDict(typing.TypedDict, total=False):
    defaultMode: int
    items: list[kubernetes.client.V1KeyToPathDict]
    optional: bool
    secretName: str
