import kubernetes.client
import typing

class V1NetworkPolicyEgressRule:
    ports: typing.Optional[list[kubernetes.client.V1NetworkPolicyPort]]
    to: typing.Optional[list[kubernetes.client.V1NetworkPolicyPeer]]

    def __init__(
        self,
        *,
        ports: typing.Optional[list[kubernetes.client.V1NetworkPolicyPort]] = ...,
        to: typing.Optional[list[kubernetes.client.V1NetworkPolicyPeer]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1NetworkPolicyEgressRuleDict: ...

class V1NetworkPolicyEgressRuleDict(typing.TypedDict, total=False):
    ports: list[kubernetes.client.V1NetworkPolicyPortDict]
    to: list[kubernetes.client.V1NetworkPolicyPeerDict]
