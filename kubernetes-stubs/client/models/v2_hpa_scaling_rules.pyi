import kubernetes.client
import typing

class V2HPAScalingRules:
    policies: typing.Optional[list[kubernetes.client.V2HPAScalingPolicy]]
    select_policy: typing.Optional[str]
    stabilization_window_seconds: typing.Optional[int]

    def __init__(
        self,
        *,
        policies: typing.Optional[list[kubernetes.client.V2HPAScalingPolicy]] = ...,
        select_policy: typing.Optional[str] = ...,
        stabilization_window_seconds: typing.Optional[int] = ...,
    ) -> None: ...
    def to_dict(self) -> V2HPAScalingRulesDict: ...

class V2HPAScalingRulesDict(typing.TypedDict, total=False):
    policies: list[kubernetes.client.V2HPAScalingPolicyDict]
    selectPolicy: str
    stabilizationWindowSeconds: int
