import kubernetes.client
import typing

class V1CSIDriverList:
    api_version: str
    items: list[kubernetes.client.V1CSIDriver]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1CSIDriver],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1CSIDriverListDict: ...

class V1CSIDriverListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1CSIDriverDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
