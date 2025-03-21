import kubernetes.client
import typing

class V1ControllerRevisionList:
    api_version: str
    items: list[kubernetes.client.V1ControllerRevision]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1ControllerRevision],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ControllerRevisionListDict: ...

class V1ControllerRevisionListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1ControllerRevisionDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
