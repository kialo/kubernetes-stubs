import kubernetes.client
import typing

class V1FlowSchema:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    spec: kubernetes.client.V1FlowSchemaSpec
    status: kubernetes.client.V1FlowSchemaStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1FlowSchemaSpec] = ...,
        status: typing.Optional[kubernetes.client.V1FlowSchemaStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> V1FlowSchemaDict: ...

class V1FlowSchemaDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    spec: kubernetes.client.V1FlowSchemaSpecDict
    status: kubernetes.client.V1FlowSchemaStatusDict
