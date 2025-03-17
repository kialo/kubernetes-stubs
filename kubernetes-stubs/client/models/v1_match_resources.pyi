import kubernetes.client
import typing

class V1MatchResources:
    exclude_resource_rules: typing.Optional[
        list[kubernetes.client.V1NamedRuleWithOperations]
    ]
    match_policy: typing.Optional[str]
    namespace_selector: typing.Optional[kubernetes.client.V1LabelSelector]
    object_selector: typing.Optional[kubernetes.client.V1LabelSelector]
    resource_rules: typing.Optional[list[kubernetes.client.V1NamedRuleWithOperations]]

    def __init__(
        self,
        *,
        exclude_resource_rules: typing.Optional[
            list[kubernetes.client.V1NamedRuleWithOperations]
        ] = ...,
        match_policy: typing.Optional[str] = ...,
        namespace_selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...,
        object_selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...,
        resource_rules: typing.Optional[
            list[kubernetes.client.V1NamedRuleWithOperations]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1MatchResourcesDict: ...

class V1MatchResourcesDict(typing.TypedDict, total=False):
    excludeResourceRules: list[kubernetes.client.V1NamedRuleWithOperationsDict]
    matchPolicy: str
    namespaceSelector: kubernetes.client.V1LabelSelectorDict
    objectSelector: kubernetes.client.V1LabelSelectorDict
    resourceRules: list[kubernetes.client.V1NamedRuleWithOperationsDict]
