import kubernetes.client
import typing

class V1NodeList:
    api_version: str
    items: list[kubernetes.client.V1Node]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1Node],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1NodeListDict: ...

class V1NodeListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1NodeDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
