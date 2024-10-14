import kubernetes.client
import typing

class V1APIServiceList:
    api_version: str
    items: list[kubernetes.client.V1APIService]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1APIService],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1APIServiceListDict: ...

class V1APIServiceListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1APIServiceDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
