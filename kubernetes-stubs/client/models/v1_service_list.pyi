import kubernetes.client
import typing

class V1ServiceList:
    api_version: str
    items: list[kubernetes.client.V1Service]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1Service],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ServiceListDict: ...

class V1ServiceListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1ServiceDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
