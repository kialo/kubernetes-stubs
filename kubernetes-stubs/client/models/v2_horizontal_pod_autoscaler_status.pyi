import datetime
import kubernetes.client
import typing

class V2HorizontalPodAutoscalerStatus:
    conditions: typing.Optional[
        list[kubernetes.client.V2HorizontalPodAutoscalerCondition]
    ]
    current_metrics: typing.Optional[list[kubernetes.client.V2MetricStatus]]
    current_replicas: typing.Optional[int]
    desired_replicas: int
    last_scale_time: typing.Optional[datetime.datetime]
    observed_generation: typing.Optional[int]

    def __init__(
        self,
        *,
        conditions: typing.Optional[
            list[kubernetes.client.V2HorizontalPodAutoscalerCondition]
        ] = ...,
        current_metrics: typing.Optional[list[kubernetes.client.V2MetricStatus]] = ...,
        current_replicas: typing.Optional[int] = ...,
        desired_replicas: int,
        last_scale_time: typing.Optional[datetime.datetime] = ...,
        observed_generation: typing.Optional[int] = ...,
    ) -> None: ...
    def to_dict(self) -> V2HorizontalPodAutoscalerStatusDict: ...

class V2HorizontalPodAutoscalerStatusDict(typing.TypedDict, total=False):
    conditions: list[kubernetes.client.V2HorizontalPodAutoscalerConditionDict]
    currentMetrics: list[kubernetes.client.V2MetricStatusDict]
    currentReplicas: int
    desiredReplicas: int
    lastScaleTime: datetime.datetime
    observedGeneration: int
