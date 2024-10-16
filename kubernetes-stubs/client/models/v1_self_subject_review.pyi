import kubernetes.client
import typing

class V1SelfSubjectReview:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    status: kubernetes.client.V1SelfSubjectReviewStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        status: typing.Optional[kubernetes.client.V1SelfSubjectReviewStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> V1SelfSubjectReviewDict: ...

class V1SelfSubjectReviewDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    status: kubernetes.client.V1SelfSubjectReviewStatusDict
