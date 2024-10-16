import kubernetes.client
import typing

class V1ReplicationControllerList:
    api_version: str
    items: list[kubernetes.client.V1ReplicationController]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1ReplicationController],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ReplicationControllerListDict: ...

class V1ReplicationControllerListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1ReplicationControllerDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
