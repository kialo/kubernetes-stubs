import kubernetes.client
import typing

class V1TokenReviewStatus:
    audiences: typing.Optional[list[str]]
    authenticated: typing.Optional[bool]
    error: typing.Optional[str]
    user: typing.Optional[kubernetes.client.V1UserInfo]

    def __init__(
        self,
        *,
        audiences: typing.Optional[list[str]] = ...,
        authenticated: typing.Optional[bool] = ...,
        error: typing.Optional[str] = ...,
        user: typing.Optional[kubernetes.client.V1UserInfo] = ...,
    ) -> None: ...
    def to_dict(self) -> V1TokenReviewStatusDict: ...

class V1TokenReviewStatusDict(typing.TypedDict, total=False):
    audiences: list[str]
    authenticated: bool
    error: str
    user: kubernetes.client.V1UserInfoDict
