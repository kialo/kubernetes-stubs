import kubernetes.client
import typing

class V1Pod:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    spec: kubernetes.client.V1PodSpec
    status: kubernetes.client.V1PodStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1PodSpec] = ...,
        status: typing.Optional[kubernetes.client.V1PodStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> V1PodDict: ...

class V1PodDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    spec: kubernetes.client.V1PodSpecDict
    status: kubernetes.client.V1PodStatusDict
