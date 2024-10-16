import kubernetes.client
import typing

class V1Job:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    spec: kubernetes.client.V1JobSpec
    status: kubernetes.client.V1JobStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1JobSpec] = ...,
        status: typing.Optional[kubernetes.client.V1JobStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> V1JobDict: ...

class V1JobDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    spec: kubernetes.client.V1JobSpecDict
    status: kubernetes.client.V1JobStatusDict
