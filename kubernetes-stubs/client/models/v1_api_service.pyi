import kubernetes.client
import typing

class V1APIService:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    spec: kubernetes.client.V1APIServiceSpec
    status: kubernetes.client.V1APIServiceStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1APIServiceSpec] = ...,
        status: typing.Optional[kubernetes.client.V1APIServiceStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> V1APIServiceDict: ...

class V1APIServiceDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    spec: kubernetes.client.V1APIServiceSpecDict
    status: kubernetes.client.V1APIServiceStatusDict
