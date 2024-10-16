import kubernetes.client
import typing

class V1ReplicaSetList:
    api_version: str
    items: list[kubernetes.client.V1ReplicaSet]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1ReplicaSet],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ReplicaSetListDict: ...

class V1ReplicaSetListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1ReplicaSetDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict