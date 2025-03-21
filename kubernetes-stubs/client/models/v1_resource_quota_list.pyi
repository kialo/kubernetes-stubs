import kubernetes.client
import typing

class V1ResourceQuotaList:
    api_version: str
    items: list[kubernetes.client.V1ResourceQuota]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1ResourceQuota],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ResourceQuotaListDict: ...

class V1ResourceQuotaListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1ResourceQuotaDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
