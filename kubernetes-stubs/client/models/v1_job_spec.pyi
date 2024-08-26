import datetime
import kubernetes.client
import typing

class V1JobSpec:
    active_deadline_seconds: typing.Optional[int]
    backoff_limit: typing.Optional[int]
    backoff_limit_per_index: typing.Optional[int]
    completion_mode: typing.Optional[str]
    completions: typing.Optional[int]
    manual_selector: typing.Optional[bool]
    max_failed_indexes: typing.Optional[int]
    parallelism: typing.Optional[int]
    pod_failure_policy: typing.Optional[kubernetes.client.V1PodFailurePolicy]
    pod_replacement_policy: typing.Optional[str]
    selector: typing.Optional[kubernetes.client.V1LabelSelector]
    suspend: typing.Optional[bool]
    template: kubernetes.client.V1PodTemplateSpec
    ttl_seconds_after_finished: typing.Optional[int]
    
    def __init__(self, *, active_deadline_seconds: typing.Optional[int] = ..., backoff_limit: typing.Optional[int] = ..., backoff_limit_per_index: typing.Optional[int] = ..., completion_mode: typing.Optional[str] = ..., completions: typing.Optional[int] = ..., manual_selector: typing.Optional[bool] = ..., max_failed_indexes: typing.Optional[int] = ..., parallelism: typing.Optional[int] = ..., pod_failure_policy: typing.Optional[kubernetes.client.V1PodFailurePolicy] = ..., pod_replacement_policy: typing.Optional[str] = ..., selector: typing.Optional[kubernetes.client.V1LabelSelector] = ..., suspend: typing.Optional[bool] = ..., template: kubernetes.client.V1PodTemplateSpec, ttl_seconds_after_finished: typing.Optional[int] = ...) -> None:
        ...
    def to_dict(self) -> V1JobSpecDict:
        ...
class V1JobSpecDict(typing.TypedDict, total=False):
    activeDeadlineSeconds: typing.Optional[int]
    backoffLimit: typing.Optional[int]
    backoffLimitPerIndex: typing.Optional[int]
    completionMode: typing.Optional[str]
    completions: typing.Optional[int]
    manualSelector: typing.Optional[bool]
    maxFailedIndexes: typing.Optional[int]
    parallelism: typing.Optional[int]
    podFailurePolicy: typing.Optional[kubernetes.client.V1PodFailurePolicyDict]
    podReplacementPolicy: typing.Optional[str]
    selector: typing.Optional[kubernetes.client.V1LabelSelectorDict]
    suspend: typing.Optional[bool]
    template: kubernetes.client.V1PodTemplateSpecDict
    ttlSecondsAfterFinished: typing.Optional[int]
