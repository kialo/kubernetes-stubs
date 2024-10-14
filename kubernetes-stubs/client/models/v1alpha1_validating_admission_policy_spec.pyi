import kubernetes.client
import typing

class V1alpha1ValidatingAdmissionPolicySpec:
    audit_annotations: typing.Optional[list[kubernetes.client.V1alpha1AuditAnnotation]]
    failure_policy: typing.Optional[str]
    match_conditions: typing.Optional[list[kubernetes.client.V1alpha1MatchCondition]]
    match_constraints: typing.Optional[kubernetes.client.V1alpha1MatchResources]
    param_kind: typing.Optional[kubernetes.client.V1alpha1ParamKind]
    validations: typing.Optional[list[kubernetes.client.V1alpha1Validation]]
    variables: typing.Optional[list[kubernetes.client.V1alpha1Variable]]

    def __init__(
        self,
        *,
        audit_annotations: typing.Optional[
            list[kubernetes.client.V1alpha1AuditAnnotation]
        ] = ...,
        failure_policy: typing.Optional[str] = ...,
        match_conditions: typing.Optional[
            list[kubernetes.client.V1alpha1MatchCondition]
        ] = ...,
        match_constraints: typing.Optional[
            kubernetes.client.V1alpha1MatchResources
        ] = ...,
        param_kind: typing.Optional[kubernetes.client.V1alpha1ParamKind] = ...,
        validations: typing.Optional[list[kubernetes.client.V1alpha1Validation]] = ...,
        variables: typing.Optional[list[kubernetes.client.V1alpha1Variable]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha1ValidatingAdmissionPolicySpecDict: ...

class V1alpha1ValidatingAdmissionPolicySpecDict(typing.TypedDict, total=False):
    auditAnnotations: list[kubernetes.client.V1alpha1AuditAnnotationDict]
    failurePolicy: str
    matchConditions: list[kubernetes.client.V1alpha1MatchConditionDict]
    matchConstraints: kubernetes.client.V1alpha1MatchResourcesDict
    paramKind: kubernetes.client.V1alpha1ParamKindDict
    validations: list[kubernetes.client.V1alpha1ValidationDict]
    variables: list[kubernetes.client.V1alpha1VariableDict]
