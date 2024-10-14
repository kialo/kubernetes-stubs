import kubernetes.client
import typing

class V1Scale:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    spec: kubernetes.client.V1ScaleSpec
    status: kubernetes.client.V1ScaleStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1ScaleSpec] = ...,
        status: typing.Optional[kubernetes.client.V1ScaleStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ScaleDict: ...

class V1ScaleDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    spec: kubernetes.client.V1ScaleSpecDict
    status: kubernetes.client.V1ScaleStatusDict
