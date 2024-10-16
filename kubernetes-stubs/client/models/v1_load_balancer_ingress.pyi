import kubernetes.client
import typing

class V1LoadBalancerIngress:
    hostname: typing.Optional[str]
    ip: typing.Optional[str]
    ip_mode: typing.Optional[str]
    ports: typing.Optional[list[kubernetes.client.V1PortStatus]]

    def __init__(
        self,
        *,
        hostname: typing.Optional[str] = ...,
        ip: typing.Optional[str] = ...,
        ip_mode: typing.Optional[str] = ...,
        ports: typing.Optional[list[kubernetes.client.V1PortStatus]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1LoadBalancerIngressDict: ...

class V1LoadBalancerIngressDict(typing.TypedDict, total=False):
    hostname: str
    ip: str
    ipMode: str
    ports: list[kubernetes.client.V1PortStatusDict]
