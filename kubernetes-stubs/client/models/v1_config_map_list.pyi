import kubernetes.client
import typing

class V1ConfigMapList:
    api_version: str
    items: list[kubernetes.client.V1ConfigMap]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1ConfigMap],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ConfigMapListDict: ...

class V1ConfigMapListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1ConfigMapDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
