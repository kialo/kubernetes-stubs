import kubernetes.client
import typing

class V1StatefulSetStatus:
    available_replicas: typing.Optional[int]
    collision_count: typing.Optional[int]
    conditions: typing.Optional[list[kubernetes.client.V1StatefulSetCondition]]
    current_replicas: typing.Optional[int]
    current_revision: typing.Optional[str]
    observed_generation: typing.Optional[int]
    ready_replicas: typing.Optional[int]
    replicas: int
    update_revision: typing.Optional[str]
    updated_replicas: typing.Optional[int]

    def __init__(
        self,
        *,
        available_replicas: typing.Optional[int] = ...,
        collision_count: typing.Optional[int] = ...,
        conditions: typing.Optional[
            list[kubernetes.client.V1StatefulSetCondition]
        ] = ...,
        current_replicas: typing.Optional[int] = ...,
        current_revision: typing.Optional[str] = ...,
        observed_generation: typing.Optional[int] = ...,
        ready_replicas: typing.Optional[int] = ...,
        replicas: int,
        update_revision: typing.Optional[str] = ...,
        updated_replicas: typing.Optional[int] = ...,
    ) -> None: ...
    def to_dict(self) -> V1StatefulSetStatusDict: ...

class V1StatefulSetStatusDict(typing.TypedDict, total=False):
    availableReplicas: int
    collisionCount: int
    conditions: list[kubernetes.client.V1StatefulSetConditionDict]
    currentReplicas: int
    currentRevision: str
    observedGeneration: int
    readyReplicas: int
    replicas: int
    updateRevision: str
    updatedReplicas: int
