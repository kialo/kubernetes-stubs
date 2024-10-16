import kubernetes.client
import typing

class V1IngressLoadBalancerStatus:
    ingress: typing.Optional[list[kubernetes.client.V1IngressLoadBalancerIngress]]

    def __init__(
        self,
        *,
        ingress: typing.Optional[
            list[kubernetes.client.V1IngressLoadBalancerIngress]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1IngressLoadBalancerStatusDict: ...

class V1IngressLoadBalancerStatusDict(typing.TypedDict, total=False):
    ingress: list[kubernetes.client.V1IngressLoadBalancerIngressDict]