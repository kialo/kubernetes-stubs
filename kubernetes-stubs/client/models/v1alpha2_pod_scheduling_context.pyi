import kubernetes.client
import typing

class V1alpha2PodSchedulingContext:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    spec: kubernetes.client.V1alpha2PodSchedulingContextSpec
    status: kubernetes.client.V1alpha2PodSchedulingContextStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: kubernetes.client.V1alpha2PodSchedulingContextSpec,
        status: typing.Optional[
            kubernetes.client.V1alpha2PodSchedulingContextStatus
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha2PodSchedulingContextDict: ...

class V1alpha2PodSchedulingContextDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    spec: kubernetes.client.V1alpha2PodSchedulingContextSpecDict
    status: kubernetes.client.V1alpha2PodSchedulingContextStatusDict