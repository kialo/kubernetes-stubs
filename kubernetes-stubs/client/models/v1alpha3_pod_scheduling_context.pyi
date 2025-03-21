import kubernetes.client
import typing

class V1alpha3PodSchedulingContext:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    spec: kubernetes.client.V1alpha3PodSchedulingContextSpec
    status: kubernetes.client.V1alpha3PodSchedulingContextStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: kubernetes.client.V1alpha3PodSchedulingContextSpec,
        status: typing.Optional[
            kubernetes.client.V1alpha3PodSchedulingContextStatus
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha3PodSchedulingContextDict: ...

class V1alpha3PodSchedulingContextDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    spec: kubernetes.client.V1alpha3PodSchedulingContextSpecDict
    status: kubernetes.client.V1alpha3PodSchedulingContextStatusDict
