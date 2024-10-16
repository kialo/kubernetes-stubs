import kubernetes.client
import typing

class V1FlowSchemaList:
    api_version: str
    items: list[kubernetes.client.V1FlowSchema]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1FlowSchema],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1FlowSchemaListDict: ...

class V1FlowSchemaListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1FlowSchemaDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict