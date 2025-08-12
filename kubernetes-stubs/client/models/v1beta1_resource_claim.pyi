import kubernetes.client
import typing

class V1beta1ResourceClaim:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    spec: kubernetes.client.V1beta1ResourceClaimSpec
    status: kubernetes.client.V1beta1ResourceClaimStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: kubernetes.client.V1beta1ResourceClaimSpec,
        status: typing.Optional[kubernetes.client.V1beta1ResourceClaimStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1ResourceClaimDict: ...

class V1beta1ResourceClaimDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    spec: kubernetes.client.V1beta1ResourceClaimSpecDict
    status: kubernetes.client.V1beta1ResourceClaimStatusDict
