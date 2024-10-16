import kubernetes.client
import typing

class V1beta3FlowSchemaList:
    api_version: str
    items: list[kubernetes.client.V1beta3FlowSchema]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1beta3FlowSchema],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta3FlowSchemaListDict: ...

class V1beta3FlowSchemaListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1beta3FlowSchemaDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
