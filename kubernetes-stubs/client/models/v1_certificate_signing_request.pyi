import kubernetes.client
import typing

class V1CertificateSigningRequest:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    spec: kubernetes.client.V1CertificateSigningRequestSpec
    status: kubernetes.client.V1CertificateSigningRequestStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: kubernetes.client.V1CertificateSigningRequestSpec,
        status: typing.Optional[
            kubernetes.client.V1CertificateSigningRequestStatus
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1CertificateSigningRequestDict: ...

class V1CertificateSigningRequestDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    spec: kubernetes.client.V1CertificateSigningRequestSpecDict
    status: kubernetes.client.V1CertificateSigningRequestStatusDict
