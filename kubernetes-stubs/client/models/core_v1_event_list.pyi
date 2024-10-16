import kubernetes.client
import typing

class CoreV1EventList:
    api_version: str
    items: list[kubernetes.client.CoreV1Event]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.CoreV1Event],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> CoreV1EventListDict: ...

class CoreV1EventListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.CoreV1EventDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
