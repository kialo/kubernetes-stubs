import datetime
import kubernetes.client
import typing

class V1JobStatus:
    active: typing.Optional[int]
    completed_indexes: typing.Optional[str]
    completion_time: typing.Optional[datetime.datetime]
    conditions: typing.Optional[list[kubernetes.client.V1JobCondition]]
    failed: typing.Optional[int]
    failed_indexes: typing.Optional[str]
    ready: typing.Optional[int]
    start_time: typing.Optional[datetime.datetime]
    succeeded: typing.Optional[int]
    terminating: typing.Optional[int]
    uncounted_terminated_pods: typing.Optional[
        kubernetes.client.V1UncountedTerminatedPods
    ]

    def __init__(
        self,
        *,
        active: typing.Optional[int] = ...,
        completed_indexes: typing.Optional[str] = ...,
        completion_time: typing.Optional[datetime.datetime] = ...,
        conditions: typing.Optional[list[kubernetes.client.V1JobCondition]] = ...,
        failed: typing.Optional[int] = ...,
        failed_indexes: typing.Optional[str] = ...,
        ready: typing.Optional[int] = ...,
        start_time: typing.Optional[datetime.datetime] = ...,
        succeeded: typing.Optional[int] = ...,
        terminating: typing.Optional[int] = ...,
        uncounted_terminated_pods: typing.Optional[
            kubernetes.client.V1UncountedTerminatedPods
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1JobStatusDict: ...

class V1JobStatusDict(typing.TypedDict, total=False):
    active: int
    completedIndexes: str
    completionTime: datetime.datetime
    conditions: list[kubernetes.client.V1JobConditionDict]
    failed: int
    failedIndexes: str
    ready: int
    startTime: datetime.datetime
    succeeded: int
    terminating: int
    uncountedTerminatedPods: kubernetes.client.V1UncountedTerminatedPodsDict
