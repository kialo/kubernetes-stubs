import kubernetes.client
import typing

class V1CSINodeList:
    api_version: str
    items: list[kubernetes.client.V1CSINode]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1CSINode],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1CSINodeListDict: ...

class V1CSINodeListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1CSINodeDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
