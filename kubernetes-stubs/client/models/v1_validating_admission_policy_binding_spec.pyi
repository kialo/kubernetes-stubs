import kubernetes.client
import typing

class V1ValidatingAdmissionPolicyBindingSpec:
    match_resources: typing.Optional[kubernetes.client.V1MatchResources]
    param_ref: typing.Optional[kubernetes.client.V1ParamRef]
    policy_name: typing.Optional[str]
    validation_actions: typing.Optional[list[str]]

    def __init__(
        self,
        *,
        match_resources: typing.Optional[kubernetes.client.V1MatchResources] = ...,
        param_ref: typing.Optional[kubernetes.client.V1ParamRef] = ...,
        policy_name: typing.Optional[str] = ...,
        validation_actions: typing.Optional[list[str]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ValidatingAdmissionPolicyBindingSpecDict: ...

class V1ValidatingAdmissionPolicyBindingSpecDict(typing.TypedDict, total=False):
    matchResources: kubernetes.client.V1MatchResourcesDict
    paramRef: kubernetes.client.V1ParamRefDict
    policyName: str
    validationActions: list[str]
