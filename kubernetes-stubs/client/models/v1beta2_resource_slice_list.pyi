import kubernetes.client
import typing

class V1beta2ResourceSliceList:
    api_version: str
    items: list[kubernetes.client.V1beta2ResourceSlice]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1beta2ResourceSlice],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta2ResourceSliceListDict: ...

class V1beta2ResourceSliceListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1beta2ResourceSliceDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
