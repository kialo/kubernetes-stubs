import kubernetes.client
import typing

class V1ServiceAccountList:
    api_version: str
    items: list[kubernetes.client.V1ServiceAccount]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1ServiceAccount],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ServiceAccountListDict: ...

class V1ServiceAccountListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1ServiceAccountDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
