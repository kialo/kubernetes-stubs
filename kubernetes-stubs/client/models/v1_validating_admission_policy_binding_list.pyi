import kubernetes.client
import typing

class V1ValidatingAdmissionPolicyBindingList:
    api_version: str
    items: list[kubernetes.client.V1ValidatingAdmissionPolicyBinding]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1ValidatingAdmissionPolicyBinding],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ValidatingAdmissionPolicyBindingListDict: ...

class V1ValidatingAdmissionPolicyBindingListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1ValidatingAdmissionPolicyBindingDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
