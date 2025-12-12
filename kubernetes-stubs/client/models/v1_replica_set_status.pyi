import kubernetes.client
import typing

class V1ReplicaSetStatus:
    available_replicas: typing.Optional[int]
    conditions: typing.Optional[list[kubernetes.client.V1ReplicaSetCondition]]
    fully_labeled_replicas: typing.Optional[int]
    observed_generation: typing.Optional[int]
    ready_replicas: typing.Optional[int]
    replicas: int
    terminating_replicas: typing.Optional[int]

    def __init__(
        self,
        *,
        available_replicas: typing.Optional[int] = ...,
        conditions: typing.Optional[
            list[kubernetes.client.V1ReplicaSetCondition]
        ] = ...,
        fully_labeled_replicas: typing.Optional[int] = ...,
        observed_generation: typing.Optional[int] = ...,
        ready_replicas: typing.Optional[int] = ...,
        replicas: int,
        terminating_replicas: typing.Optional[int] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ReplicaSetStatusDict: ...

class V1ReplicaSetStatusDict(typing.TypedDict, total=False):
    availableReplicas: int
    conditions: list[kubernetes.client.V1ReplicaSetConditionDict]
    fullyLabeledReplicas: int
    observedGeneration: int
    readyReplicas: int
    replicas: int
    terminatingReplicas: int
