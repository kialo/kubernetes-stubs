import kubernetes.client
import typing

class V1beta1ValidatingAdmissionPolicy:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    spec: kubernetes.client.V1beta1ValidatingAdmissionPolicySpec
    status: kubernetes.client.V1beta1ValidatingAdmissionPolicyStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[
            kubernetes.client.V1beta1ValidatingAdmissionPolicySpec
        ] = ...,
        status: typing.Optional[
            kubernetes.client.V1beta1ValidatingAdmissionPolicyStatus
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1ValidatingAdmissionPolicyDict: ...

class V1beta1ValidatingAdmissionPolicyDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    spec: kubernetes.client.V1beta1ValidatingAdmissionPolicySpecDict
    status: kubernetes.client.V1beta1ValidatingAdmissionPolicyStatusDict