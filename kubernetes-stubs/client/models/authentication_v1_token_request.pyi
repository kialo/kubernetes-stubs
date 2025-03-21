import kubernetes.client
import typing

class AuthenticationV1TokenRequest:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    spec: kubernetes.client.V1TokenRequestSpec
    status: kubernetes.client.V1TokenRequestStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: kubernetes.client.V1TokenRequestSpec,
        status: typing.Optional[kubernetes.client.V1TokenRequestStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> AuthenticationV1TokenRequestDict: ...

class AuthenticationV1TokenRequestDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    spec: kubernetes.client.V1TokenRequestSpecDict
    status: kubernetes.client.V1TokenRequestStatusDict
