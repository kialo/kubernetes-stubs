import kubernetes.client
import typing

class V1NodeSpec:
    config_source: typing.Optional[kubernetes.client.V1NodeConfigSource]
    external_id: typing.Optional[str]
    pod_cidr: typing.Optional[str]
    pod_cid_rs: typing.Optional[list[str]]
    provider_id: typing.Optional[str]
    taints: typing.Optional[list[kubernetes.client.V1Taint]]
    unschedulable: typing.Optional[bool]

    def __init__(
        self,
        *,
        config_source: typing.Optional[kubernetes.client.V1NodeConfigSource] = ...,
        external_id: typing.Optional[str] = ...,
        pod_cidr: typing.Optional[str] = ...,
        pod_cid_rs: typing.Optional[list[str]] = ...,
        provider_id: typing.Optional[str] = ...,
        taints: typing.Optional[list[kubernetes.client.V1Taint]] = ...,
        unschedulable: typing.Optional[bool] = ...,
    ) -> None: ...
    def to_dict(self) -> V1NodeSpecDict: ...

class V1NodeSpecDict(typing.TypedDict, total=False):
    configSource: kubernetes.client.V1NodeConfigSourceDict
    externalID: str
    podCIDR: str
    podCIDRs: list[str]
    providerID: str
    taints: list[kubernetes.client.V1TaintDict]
    unschedulable: bool
