import kubernetes.client
import typing

class V1alpha2ResourceClassList:
    api_version: str
    items: list[kubernetes.client.V1alpha2ResourceClass]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1alpha2ResourceClass],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha2ResourceClassListDict: ...

class V1alpha2ResourceClassListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1alpha2ResourceClassDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict