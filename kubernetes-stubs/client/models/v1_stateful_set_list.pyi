import kubernetes.client
import typing

class V1StatefulSetList:
    api_version: str
    items: list[kubernetes.client.V1StatefulSet]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1StatefulSet],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1StatefulSetListDict: ...

class V1StatefulSetListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1StatefulSetDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict