import kubernetes.client
import typing

class V1alpha1MutatingAdmissionPolicyBindingSpec:
    match_resources: typing.Optional[kubernetes.client.V1alpha1MatchResources]
    param_ref: typing.Optional[kubernetes.client.V1alpha1ParamRef]
    policy_name: typing.Optional[str]

    def __init__(
        self,
        *,
        match_resources: typing.Optional[
            kubernetes.client.V1alpha1MatchResources
        ] = ...,
        param_ref: typing.Optional[kubernetes.client.V1alpha1ParamRef] = ...,
        policy_name: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha1MutatingAdmissionPolicyBindingSpecDict: ...

class V1alpha1MutatingAdmissionPolicyBindingSpecDict(typing.TypedDict, total=False):
    matchResources: kubernetes.client.V1alpha1MatchResourcesDict
    paramRef: kubernetes.client.V1alpha1ParamRefDict
    policyName: str
