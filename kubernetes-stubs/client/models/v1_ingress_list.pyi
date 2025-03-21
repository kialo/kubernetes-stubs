import kubernetes.client
import typing

class V1IngressList:
    api_version: str
    items: list[kubernetes.client.V1Ingress]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1Ingress],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1IngressListDict: ...

class V1IngressListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1IngressDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
