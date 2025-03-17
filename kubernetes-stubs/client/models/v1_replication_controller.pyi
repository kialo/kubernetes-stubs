import kubernetes.client
import typing

class V1ReplicationController:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    spec: kubernetes.client.V1ReplicationControllerSpec
    status: kubernetes.client.V1ReplicationControllerStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1ReplicationControllerSpec] = ...,
        status: typing.Optional[kubernetes.client.V1ReplicationControllerStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ReplicationControllerDict: ...

class V1ReplicationControllerDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    spec: kubernetes.client.V1ReplicationControllerSpecDict
    status: kubernetes.client.V1ReplicationControllerStatusDict
