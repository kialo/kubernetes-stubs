import kubernetes.client
import typing

class V1JobSpec:
    active_deadline_seconds: typing.Optional[int]
    backoff_limit: typing.Optional[int]
    backoff_limit_per_index: typing.Optional[int]
    completion_mode: typing.Optional[str]
    completions: typing.Optional[int]
    managed_by: typing.Optional[str]
    manual_selector: typing.Optional[bool]
    max_failed_indexes: typing.Optional[int]
    parallelism: typing.Optional[int]
    pod_failure_policy: typing.Optional[kubernetes.client.V1PodFailurePolicy]
    pod_replacement_policy: typing.Optional[str]
    selector: typing.Optional[kubernetes.client.V1LabelSelector]
    success_policy: typing.Optional[kubernetes.client.V1SuccessPolicy]
    suspend: typing.Optional[bool]
    template: kubernetes.client.V1PodTemplateSpec
    ttl_seconds_after_finished: typing.Optional[int]

    def __init__(
        self,
        *,
        active_deadline_seconds: typing.Optional[int] = ...,
        backoff_limit: typing.Optional[int] = ...,
        backoff_limit_per_index: typing.Optional[int] = ...,
        completion_mode: typing.Optional[str] = ...,
        completions: typing.Optional[int] = ...,
        managed_by: typing.Optional[str] = ...,
        manual_selector: typing.Optional[bool] = ...,
        max_failed_indexes: typing.Optional[int] = ...,
        parallelism: typing.Optional[int] = ...,
        pod_failure_policy: typing.Optional[kubernetes.client.V1PodFailurePolicy] = ...,
        pod_replacement_policy: typing.Optional[str] = ...,
        selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...,
        success_policy: typing.Optional[kubernetes.client.V1SuccessPolicy] = ...,
        suspend: typing.Optional[bool] = ...,
        template: kubernetes.client.V1PodTemplateSpec,
        ttl_seconds_after_finished: typing.Optional[int] = ...,
    ) -> None: ...
    def to_dict(self) -> V1JobSpecDict: ...

class V1JobSpecDict(typing.TypedDict, total=False):
    activeDeadlineSeconds: int
    backoffLimit: int
    backoffLimitPerIndex: int
    completionMode: str
    completions: int
    managedBy: str
    manualSelector: bool
    maxFailedIndexes: int
    parallelism: int
    podFailurePolicy: kubernetes.client.V1PodFailurePolicyDict
    podReplacementPolicy: str
    selector: kubernetes.client.V1LabelSelectorDict
    successPolicy: kubernetes.client.V1SuccessPolicyDict
    suspend: bool
    template: kubernetes.client.V1PodTemplateSpecDict
    ttlSecondsAfterFinished: int
