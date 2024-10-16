import kubernetes.client
import typing

class V1VolumeAttachmentStatus:
    attach_error: typing.Optional[kubernetes.client.V1VolumeError]
    attached: bool
    attachment_metadata: typing.Optional[dict[str, str]]
    detach_error: typing.Optional[kubernetes.client.V1VolumeError]

    def __init__(
        self,
        *,
        attach_error: typing.Optional[kubernetes.client.V1VolumeError] = ...,
        attached: bool,
        attachment_metadata: typing.Optional[dict[str, str]] = ...,
        detach_error: typing.Optional[kubernetes.client.V1VolumeError] = ...,
    ) -> None: ...
    def to_dict(self) -> V1VolumeAttachmentStatusDict: ...

class V1VolumeAttachmentStatusDict(typing.TypedDict, total=False):
    attachError: kubernetes.client.V1VolumeErrorDict
    attached: bool
    attachmentMetadata: dict[str, str]
    detachError: kubernetes.client.V1VolumeErrorDict
