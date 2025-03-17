import kubernetes.client
import typing

class V1alpha2ResourceSliceList:
    api_version: str
    items: list[kubernetes.client.V1alpha2ResourceSlice]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1alpha2ResourceSlice],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha2ResourceSliceListDict: ...

class V1alpha2ResourceSliceListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1alpha2ResourceSliceDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
