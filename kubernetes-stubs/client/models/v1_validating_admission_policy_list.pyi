import kubernetes.client
import typing

class V1ValidatingAdmissionPolicyList:
    api_version: str
    items: typing.Optional[list[kubernetes.client.V1ValidatingAdmissionPolicy]]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.Optional[
            list[kubernetes.client.V1ValidatingAdmissionPolicy]
        ] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ValidatingAdmissionPolicyListDict: ...

class V1ValidatingAdmissionPolicyListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1ValidatingAdmissionPolicyDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
