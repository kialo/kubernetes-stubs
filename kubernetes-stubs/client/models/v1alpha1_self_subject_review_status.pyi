import kubernetes.client
import typing

class V1alpha1SelfSubjectReviewStatus:
    user_info: typing.Optional[kubernetes.client.V1UserInfo]

    def __init__(
        self, *, user_info: typing.Optional[kubernetes.client.V1UserInfo] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1SelfSubjectReviewStatusDict: ...

class V1alpha1SelfSubjectReviewStatusDict(typing.TypedDict, total=False):
    userInfo: kubernetes.client.V1UserInfoDict
