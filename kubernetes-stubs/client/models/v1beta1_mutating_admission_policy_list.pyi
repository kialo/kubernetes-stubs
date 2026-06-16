import kubernetes.client
import typing

class V1beta1MutatingAdmissionPolicyList:
    api_version: str
    items: list[kubernetes.client.V1beta1MutatingAdmissionPolicy]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1beta1MutatingAdmissionPolicy],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1MutatingAdmissionPolicyListDict: ...

class V1beta1MutatingAdmissionPolicyListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1beta1MutatingAdmissionPolicyDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
