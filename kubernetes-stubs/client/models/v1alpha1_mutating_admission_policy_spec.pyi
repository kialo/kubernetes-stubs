import kubernetes.client
import typing

class V1alpha1MutatingAdmissionPolicySpec:
    failure_policy: typing.Optional[str]
    match_conditions: typing.Optional[list[kubernetes.client.V1alpha1MatchCondition]]
    match_constraints: typing.Optional[kubernetes.client.V1alpha1MatchResources]
    mutations: typing.Optional[list[kubernetes.client.V1alpha1Mutation]]
    param_kind: typing.Optional[kubernetes.client.V1alpha1ParamKind]
    reinvocation_policy: typing.Optional[str]
    variables: typing.Optional[list[kubernetes.client.V1alpha1Variable]]

    def __init__(
        self,
        *,
        failure_policy: typing.Optional[str] = ...,
        match_conditions: typing.Optional[
            list[kubernetes.client.V1alpha1MatchCondition]
        ] = ...,
        match_constraints: typing.Optional[
            kubernetes.client.V1alpha1MatchResources
        ] = ...,
        mutations: typing.Optional[list[kubernetes.client.V1alpha1Mutation]] = ...,
        param_kind: typing.Optional[kubernetes.client.V1alpha1ParamKind] = ...,
        reinvocation_policy: typing.Optional[str] = ...,
        variables: typing.Optional[list[kubernetes.client.V1alpha1Variable]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha1MutatingAdmissionPolicySpecDict: ...

class V1alpha1MutatingAdmissionPolicySpecDict(typing.TypedDict, total=False):
    failurePolicy: str
    matchConditions: list[kubernetes.client.V1alpha1MatchConditionDict]
    matchConstraints: kubernetes.client.V1alpha1MatchResourcesDict
    mutations: list[kubernetes.client.V1alpha1MutationDict]
    paramKind: kubernetes.client.V1alpha1ParamKindDict
    reinvocationPolicy: str
    variables: list[kubernetes.client.V1alpha1VariableDict]
