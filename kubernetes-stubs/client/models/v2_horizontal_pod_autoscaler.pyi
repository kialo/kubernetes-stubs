import kubernetes.client
import typing

class V2HorizontalPodAutoscaler:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    spec: kubernetes.client.V2HorizontalPodAutoscalerSpec
    status: kubernetes.client.V2HorizontalPodAutoscalerStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V2HorizontalPodAutoscalerSpec] = ...,
        status: typing.Optional[
            kubernetes.client.V2HorizontalPodAutoscalerStatus
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V2HorizontalPodAutoscalerDict: ...

class V2HorizontalPodAutoscalerDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    spec: kubernetes.client.V2HorizontalPodAutoscalerSpecDict
    status: kubernetes.client.V2HorizontalPodAutoscalerStatusDict
