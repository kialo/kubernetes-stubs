import kubernetes.client
import typing

class V1DeploymentSpec:
    min_ready_seconds: typing.Optional[int]
    paused: typing.Optional[bool]
    progress_deadline_seconds: typing.Optional[int]
    replicas: typing.Optional[int]
    revision_history_limit: typing.Optional[int]
    selector: kubernetes.client.V1LabelSelector
    strategy: typing.Optional[kubernetes.client.V1DeploymentStrategy]
    template: kubernetes.client.V1PodTemplateSpec

    def __init__(
        self,
        *,
        min_ready_seconds: typing.Optional[int] = ...,
        paused: typing.Optional[bool] = ...,
        progress_deadline_seconds: typing.Optional[int] = ...,
        replicas: typing.Optional[int] = ...,
        revision_history_limit: typing.Optional[int] = ...,
        selector: kubernetes.client.V1LabelSelector,
        strategy: typing.Optional[kubernetes.client.V1DeploymentStrategy] = ...,
        template: kubernetes.client.V1PodTemplateSpec,
    ) -> None: ...
    def to_dict(self) -> V1DeploymentSpecDict: ...

class V1DeploymentSpecDict(typing.TypedDict, total=False):
    minReadySeconds: int
    paused: bool
    progressDeadlineSeconds: int
    replicas: int
    revisionHistoryLimit: int
    selector: kubernetes.client.V1LabelSelectorDict
    strategy: kubernetes.client.V1DeploymentStrategyDict
    template: kubernetes.client.V1PodTemplateSpecDict
