import kubernetes.client
import typing

class V2HorizontalPodAutoscalerList:
    api_version: str
    items: list[kubernetes.client.V2HorizontalPodAutoscaler]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V2HorizontalPodAutoscaler],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V2HorizontalPodAutoscalerListDict: ...

class V2HorizontalPodAutoscalerListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V2HorizontalPodAutoscalerDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
