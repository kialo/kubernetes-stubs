import kubernetes.client
import typing

class V1Secret:
    api_version: str
    data: typing.Optional[dict[str, str]]
    immutable: typing.Optional[bool]
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    string_data: typing.Optional[dict[str, str]]
    type: typing.Optional[str]

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        data: typing.Optional[dict[str, str]] = ...,
        immutable: typing.Optional[bool] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        string_data: typing.Optional[dict[str, str]] = ...,
        type: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1SecretDict: ...

class V1SecretDict(typing.TypedDict, total=False):
    apiVersion: str
    data: dict[str, str]
    immutable: bool
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    stringData: dict[str, str]
    type: str
