import kubernetes.client
import typing

class V1alpha1ClusterTrustBundleList:
    api_version: str
    items: list[kubernetes.client.V1alpha1ClusterTrustBundle]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1alpha1ClusterTrustBundle],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha1ClusterTrustBundleListDict: ...

class V1alpha1ClusterTrustBundleListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1alpha1ClusterTrustBundleDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
