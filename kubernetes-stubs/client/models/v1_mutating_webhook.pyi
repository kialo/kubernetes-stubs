import kubernetes.client
import typing

class V1MutatingWebhook:
    admission_review_versions: list[str]
    client_config: kubernetes.client.AdmissionregistrationV1WebhookClientConfig
    failure_policy: typing.Optional[str]
    match_conditions: typing.Optional[list[kubernetes.client.V1MatchCondition]]
    match_policy: typing.Optional[str]
    name: str
    namespace_selector: typing.Optional[kubernetes.client.V1LabelSelector]
    object_selector: typing.Optional[kubernetes.client.V1LabelSelector]
    reinvocation_policy: typing.Optional[str]
    rules: typing.Optional[list[kubernetes.client.V1RuleWithOperations]]
    side_effects: str
    timeout_seconds: typing.Optional[int]

    def __init__(
        self,
        *,
        admission_review_versions: list[str],
        client_config: kubernetes.client.AdmissionregistrationV1WebhookClientConfig,
        failure_policy: typing.Optional[str] = ...,
        match_conditions: typing.Optional[
            list[kubernetes.client.V1MatchCondition]
        ] = ...,
        match_policy: typing.Optional[str] = ...,
        name: str,
        namespace_selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...,
        object_selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...,
        reinvocation_policy: typing.Optional[str] = ...,
        rules: typing.Optional[list[kubernetes.client.V1RuleWithOperations]] = ...,
        side_effects: str,
        timeout_seconds: typing.Optional[int] = ...,
    ) -> None: ...
    def to_dict(self) -> V1MutatingWebhookDict: ...

class V1MutatingWebhookDict(typing.TypedDict, total=False):
    admissionReviewVersions: list[str]
    clientConfig: kubernetes.client.AdmissionregistrationV1WebhookClientConfigDict
    failurePolicy: str
    matchConditions: list[kubernetes.client.V1MatchConditionDict]
    matchPolicy: str
    name: str
    namespaceSelector: kubernetes.client.V1LabelSelectorDict
    objectSelector: kubernetes.client.V1LabelSelectorDict
    reinvocationPolicy: str
    rules: list[kubernetes.client.V1RuleWithOperationsDict]
    sideEffects: str
    timeoutSeconds: int
