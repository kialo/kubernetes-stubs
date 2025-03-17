import datetime
import typing

class V1HorizontalPodAutoscalerStatus:
    current_cpu_utilization_percentage: typing.Optional[int]
    current_replicas: int
    desired_replicas: int
    last_scale_time: typing.Optional[datetime.datetime]
    observed_generation: typing.Optional[int]

    def __init__(
        self,
        *,
        current_cpu_utilization_percentage: typing.Optional[int] = ...,
        current_replicas: int,
        desired_replicas: int,
        last_scale_time: typing.Optional[datetime.datetime] = ...,
        observed_generation: typing.Optional[int] = ...,
    ) -> None: ...
    def to_dict(self) -> V1HorizontalPodAutoscalerStatusDict: ...

class V1HorizontalPodAutoscalerStatusDict(typing.TypedDict, total=False):
    currentCPUUtilizationPercentage: int
    currentReplicas: int
    desiredReplicas: int
    lastScaleTime: datetime.datetime
    observedGeneration: int
