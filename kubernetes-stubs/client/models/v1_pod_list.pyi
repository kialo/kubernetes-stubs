import kubernetes.client
import typing

class V1PodList:
    api_version: str
    items: list[kubernetes.client.V1Pod]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1Pod],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1PodListDict: ...

class V1PodListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1PodDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
