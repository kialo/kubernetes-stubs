import kubernetes.client
import typing

class V1PriorityLevelConfigurationList:
    api_version: str
    items: list[kubernetes.client.V1PriorityLevelConfiguration]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1PriorityLevelConfiguration],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1PriorityLevelConfigurationListDict: ...

class V1PriorityLevelConfigurationListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1PriorityLevelConfigurationDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
