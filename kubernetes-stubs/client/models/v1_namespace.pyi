import kubernetes.client
import typing

class V1Namespace:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    spec: kubernetes.client.V1NamespaceSpec
    status: kubernetes.client.V1NamespaceStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1NamespaceSpec] = ...,
        status: typing.Optional[kubernetes.client.V1NamespaceStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> V1NamespaceDict: ...

class V1NamespaceDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    spec: kubernetes.client.V1NamespaceSpecDict
    status: kubernetes.client.V1NamespaceStatusDict
