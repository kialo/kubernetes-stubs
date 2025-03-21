import kubernetes.client
import typing

class V1alpha1SelfSubjectReview:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    status: kubernetes.client.V1alpha1SelfSubjectReviewStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        status: typing.Optional[
            kubernetes.client.V1alpha1SelfSubjectReviewStatus
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha1SelfSubjectReviewDict: ...

class V1alpha1SelfSubjectReviewDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    status: kubernetes.client.V1alpha1SelfSubjectReviewStatusDict
