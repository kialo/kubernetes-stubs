import kubernetes.client
import typing

class V1HorizontalPodAutoscaler:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    spec: kubernetes.client.V1HorizontalPodAutoscalerSpec
    status: kubernetes.client.V1HorizontalPodAutoscalerStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1HorizontalPodAutoscalerSpec] = ...,
        status: typing.Optional[
            kubernetes.client.V1HorizontalPodAutoscalerStatus
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1HorizontalPodAutoscalerDict: ...

class V1HorizontalPodAutoscalerDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    spec: kubernetes.client.V1HorizontalPodAutoscalerSpecDict
    status: kubernetes.client.V1HorizontalPodAutoscalerStatusDict
