import kubernetes.client
import typing

class V1beta3PriorityLevelConfigurationList:
    api_version: str
    items: list[kubernetes.client.V1beta3PriorityLevelConfiguration]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1beta3PriorityLevelConfiguration],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta3PriorityLevelConfigurationListDict: ...

class V1beta3PriorityLevelConfigurationListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1beta3PriorityLevelConfigurationDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
