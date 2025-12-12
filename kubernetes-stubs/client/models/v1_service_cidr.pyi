import kubernetes.client
import typing

class V1ServiceCIDR:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    spec: kubernetes.client.V1ServiceCIDRSpec
    status: kubernetes.client.V1ServiceCIDRStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1ServiceCIDRSpec] = ...,
        status: typing.Optional[kubernetes.client.V1ServiceCIDRStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ServiceCIDRDict: ...

class V1ServiceCIDRDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    spec: kubernetes.client.V1ServiceCIDRSpecDict
    status: kubernetes.client.V1ServiceCIDRStatusDict
