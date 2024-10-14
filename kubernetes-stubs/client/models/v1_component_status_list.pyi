import kubernetes.client
import typing

class V1ComponentStatusList:
    api_version: str
    items: list[kubernetes.client.V1ComponentStatus]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1ComponentStatus],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ComponentStatusListDict: ...

class V1ComponentStatusListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1ComponentStatusDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
