import kubernetes.client
import typing

class V1CertificateSigningRequestList:
    api_version: str
    items: list[kubernetes.client.V1CertificateSigningRequest]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1CertificateSigningRequest],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1CertificateSigningRequestListDict: ...

class V1CertificateSigningRequestListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1CertificateSigningRequestDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
