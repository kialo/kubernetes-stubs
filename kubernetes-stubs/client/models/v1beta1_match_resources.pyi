import kubernetes.client
import typing

class V1beta1MatchResources:
    exclude_resource_rules: typing.Optional[
        list[kubernetes.client.V1beta1NamedRuleWithOperations]
    ]
    match_policy: typing.Optional[str]
    namespace_selector: typing.Optional[kubernetes.client.V1LabelSelector]
    object_selector: typing.Optional[kubernetes.client.V1LabelSelector]
    resource_rules: typing.Optional[
        list[kubernetes.client.V1beta1NamedRuleWithOperations]
    ]

    def __init__(
        self,
        *,
        exclude_resource_rules: typing.Optional[
            list[kubernetes.client.V1beta1NamedRuleWithOperations]
        ] = ...,
        match_policy: typing.Optional[str] = ...,
        namespace_selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...,
        object_selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...,
        resource_rules: typing.Optional[
            list[kubernetes.client.V1beta1NamedRuleWithOperations]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1MatchResourcesDict: ...

class V1beta1MatchResourcesDict(typing.TypedDict, total=False):
    excludeResourceRules: list[kubernetes.client.V1beta1NamedRuleWithOperationsDict]
    matchPolicy: str
    namespaceSelector: kubernetes.client.V1LabelSelectorDict
    objectSelector: kubernetes.client.V1LabelSelectorDict
    resourceRules: list[kubernetes.client.V1beta1NamedRuleWithOperationsDict]
