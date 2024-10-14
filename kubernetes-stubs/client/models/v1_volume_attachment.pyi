import kubernetes.client
import typing

class V1VolumeAttachment:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    spec: kubernetes.client.V1VolumeAttachmentSpec
    status: kubernetes.client.V1VolumeAttachmentStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: kubernetes.client.V1VolumeAttachmentSpec,
        status: typing.Optional[kubernetes.client.V1VolumeAttachmentStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> V1VolumeAttachmentDict: ...

class V1VolumeAttachmentDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    spec: kubernetes.client.V1VolumeAttachmentSpecDict
    status: kubernetes.client.V1VolumeAttachmentStatusDict
