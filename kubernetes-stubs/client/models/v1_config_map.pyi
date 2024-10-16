import kubernetes.client
import typing

class V1ConfigMap:
    api_version: str
    binary_data: typing.Optional[dict[str, str]]
    data: typing.Optional[dict[str, str]]
    immutable: typing.Optional[bool]
    kind: str
    metadata: kubernetes.client.V1ObjectMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        binary_data: typing.Optional[dict[str, str]] = ...,
        data: typing.Optional[dict[str, str]] = ...,
        immutable: typing.Optional[bool] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ConfigMapDict: ...

class V1ConfigMapDict(typing.TypedDict, total=False):
    apiVersion: str
    binaryData: dict[str, str]
    data: dict[str, str]
    immutable: bool
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
