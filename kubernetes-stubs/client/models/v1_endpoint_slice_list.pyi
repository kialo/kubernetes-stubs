import kubernetes.client
import typing

class V1EndpointSliceList:
    api_version: str
    items: list[kubernetes.client.V1EndpointSlice]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1EndpointSlice],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1EndpointSliceListDict: ...

class V1EndpointSliceListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1EndpointSliceDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict