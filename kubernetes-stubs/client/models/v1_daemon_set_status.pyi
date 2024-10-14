import kubernetes.client
import typing

class V1DaemonSetStatus:
    collision_count: typing.Optional[int]
    conditions: typing.Optional[list[kubernetes.client.V1DaemonSetCondition]]
    current_number_scheduled: int
    desired_number_scheduled: int
    number_available: typing.Optional[int]
    number_misscheduled: int
    number_ready: int
    number_unavailable: typing.Optional[int]
    observed_generation: typing.Optional[int]
    updated_number_scheduled: typing.Optional[int]

    def __init__(
        self,
        *,
        collision_count: typing.Optional[int] = ...,
        conditions: typing.Optional[list[kubernetes.client.V1DaemonSetCondition]] = ...,
        current_number_scheduled: int,
        desired_number_scheduled: int,
        number_available: typing.Optional[int] = ...,
        number_misscheduled: int,
        number_ready: int,
        number_unavailable: typing.Optional[int] = ...,
        observed_generation: typing.Optional[int] = ...,
        updated_number_scheduled: typing.Optional[int] = ...,
    ) -> None: ...
    def to_dict(self) -> V1DaemonSetStatusDict: ...

class V1DaemonSetStatusDict(typing.TypedDict, total=False):
    collisionCount: int
    conditions: list[kubernetes.client.V1DaemonSetConditionDict]
    currentNumberScheduled: int
    desiredNumberScheduled: int
    numberAvailable: int
    numberMisscheduled: int
    numberReady: int
    numberUnavailable: int
    observedGeneration: int
    updatedNumberScheduled: int
