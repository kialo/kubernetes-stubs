import kubernetes.client
import typing

class V1LeaseList:
    api_version: str
    items: list[kubernetes.client.V1Lease]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1Lease],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1LeaseListDict: ...

class V1LeaseListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1LeaseDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
