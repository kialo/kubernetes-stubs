import typing

class V1PodCertificateProjection:
    certificate_chain_path: typing.Optional[str]
    credential_bundle_path: typing.Optional[str]
    key_path: typing.Optional[str]
    key_type: str
    max_expiration_seconds: typing.Optional[int]
    signer_name: str

    def __init__(
        self,
        *,
        certificate_chain_path: typing.Optional[str] = ...,
        credential_bundle_path: typing.Optional[str] = ...,
        key_path: typing.Optional[str] = ...,
        key_type: str,
        max_expiration_seconds: typing.Optional[int] = ...,
        signer_name: str,
    ) -> None: ...
    def to_dict(self) -> V1PodCertificateProjectionDict: ...

class V1PodCertificateProjectionDict(typing.TypedDict, total=False):
    certificateChainPath: str
    credentialBundlePath: str
    keyPath: str
    keyType: str
    maxExpirationSeconds: int
    signerName: str
