import kubernetes.client
import typing

class V1alpha3PodSchedulingContextList:
    api_version: str
    items: list[kubernetes.client.V1alpha3PodSchedulingContext]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1alpha3PodSchedulingContext],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha3PodSchedulingContextListDict: ...

class V1alpha3PodSchedulingContextListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1alpha3PodSchedulingContextDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
