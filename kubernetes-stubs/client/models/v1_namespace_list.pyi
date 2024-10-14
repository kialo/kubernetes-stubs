import kubernetes.client
import typing

class V1NamespaceList:
    api_version: str
    items: list[kubernetes.client.V1Namespace]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1Namespace],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1NamespaceListDict: ...

class V1NamespaceListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1NamespaceDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
