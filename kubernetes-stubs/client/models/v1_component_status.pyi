import kubernetes.client
import typing

class V1ComponentStatus:
    api_version: str
    conditions: typing.Optional[list[kubernetes.client.V1ComponentCondition]]
    kind: str
    metadata: kubernetes.client.V1ObjectMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        conditions: typing.Optional[list[kubernetes.client.V1ComponentCondition]] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ComponentStatusDict: ...

class V1ComponentStatusDict(typing.TypedDict, total=False):
    apiVersion: str
    conditions: list[kubernetes.client.V1ComponentConditionDict]
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
