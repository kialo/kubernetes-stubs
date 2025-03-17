import kubernetes.client
import typing

class V1alpha3ResourceClaim:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    spec: kubernetes.client.V1alpha3ResourceClaimSpec
    status: kubernetes.client.V1alpha3ResourceClaimStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: kubernetes.client.V1alpha3ResourceClaimSpec,
        status: typing.Optional[kubernetes.client.V1alpha3ResourceClaimStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha3ResourceClaimDict: ...

class V1alpha3ResourceClaimDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    spec: kubernetes.client.V1alpha3ResourceClaimSpecDict
    status: kubernetes.client.V1alpha3ResourceClaimStatusDict
