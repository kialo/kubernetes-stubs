import kubernetes.client
import typing

class V1SubjectAccessReview:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    spec: kubernetes.client.V1SubjectAccessReviewSpec
    status: kubernetes.client.V1SubjectAccessReviewStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: kubernetes.client.V1SubjectAccessReviewSpec,
        status: typing.Optional[kubernetes.client.V1SubjectAccessReviewStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> V1SubjectAccessReviewDict: ...

class V1SubjectAccessReviewDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    spec: kubernetes.client.V1SubjectAccessReviewSpecDict
    status: kubernetes.client.V1SubjectAccessReviewStatusDict
