import kubernetes.client
import typing

class V1beta3FlowSchema:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    spec: kubernetes.client.V1beta3FlowSchemaSpec
    status: kubernetes.client.V1beta3FlowSchemaStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1beta3FlowSchemaSpec] = ...,
        status: typing.Optional[kubernetes.client.V1beta3FlowSchemaStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta3FlowSchemaDict: ...

class V1beta3FlowSchemaDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    spec: kubernetes.client.V1beta3FlowSchemaSpecDict
    status: kubernetes.client.V1beta3FlowSchemaStatusDict
