import kubernetes.client
import typing

class V1IngressClassList:
    api_version: str
    items: list[kubernetes.client.V1IngressClass]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1IngressClass],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1IngressClassListDict: ...

class V1IngressClassListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1IngressClassDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
