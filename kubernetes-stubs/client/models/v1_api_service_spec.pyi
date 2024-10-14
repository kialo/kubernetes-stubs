import kubernetes.client
import typing

class V1APIServiceSpec:
    ca_bundle: typing.Optional[str]
    group: typing.Optional[str]
    group_priority_minimum: int
    insecure_skip_tls_verify: typing.Optional[bool]
    service: typing.Optional[kubernetes.client.ApiregistrationV1ServiceReference]
    version: typing.Optional[str]
    version_priority: int

    def __init__(
        self,
        *,
        ca_bundle: typing.Optional[str] = ...,
        group: typing.Optional[str] = ...,
        group_priority_minimum: int,
        insecure_skip_tls_verify: typing.Optional[bool] = ...,
        service: typing.Optional[
            kubernetes.client.ApiregistrationV1ServiceReference
        ] = ...,
        version: typing.Optional[str] = ...,
        version_priority: int,
    ) -> None: ...
    def to_dict(self) -> V1APIServiceSpecDict: ...

class V1APIServiceSpecDict(typing.TypedDict, total=False):
    caBundle: str
    group: str
    groupPriorityMinimum: int
    insecureSkipTLSVerify: bool
    service: kubernetes.client.ApiregistrationV1ServiceReferenceDict
    version: str
    versionPriority: int
