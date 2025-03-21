import kubernetes.client
import typing

class V1NetworkPolicySpec:
    egress: typing.Optional[list[kubernetes.client.V1NetworkPolicyEgressRule]]
    ingress: typing.Optional[list[kubernetes.client.V1NetworkPolicyIngressRule]]
    pod_selector: kubernetes.client.V1LabelSelector
    policy_types: typing.Optional[list[str]]

    def __init__(
        self,
        *,
        egress: typing.Optional[
            list[kubernetes.client.V1NetworkPolicyEgressRule]
        ] = ...,
        ingress: typing.Optional[
            list[kubernetes.client.V1NetworkPolicyIngressRule]
        ] = ...,
        pod_selector: kubernetes.client.V1LabelSelector,
        policy_types: typing.Optional[list[str]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1NetworkPolicySpecDict: ...

class V1NetworkPolicySpecDict(typing.TypedDict, total=False):
    egress: list[kubernetes.client.V1NetworkPolicyEgressRuleDict]
    ingress: list[kubernetes.client.V1NetworkPolicyIngressRuleDict]
    podSelector: kubernetes.client.V1LabelSelectorDict
    policyTypes: list[str]
