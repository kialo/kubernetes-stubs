import kubernetes.client
import typing

class V1HorizontalPodAutoscalerList:
    api_version: str
    items: list[kubernetes.client.V1HorizontalPodAutoscaler]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1HorizontalPodAutoscaler],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1HorizontalPodAutoscalerListDict: ...

class V1HorizontalPodAutoscalerListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1HorizontalPodAutoscalerDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
