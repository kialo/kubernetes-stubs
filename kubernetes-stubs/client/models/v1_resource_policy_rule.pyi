import typing

class V1ResourcePolicyRule:
    api_groups: list[str]
    cluster_scope: typing.Optional[bool]
    namespaces: typing.Optional[list[str]]
    resources: list[str]
    verbs: list[str]

    def __init__(
        self,
        *,
        api_groups: list[str],
        cluster_scope: typing.Optional[bool] = ...,
        namespaces: typing.Optional[list[str]] = ...,
        resources: list[str],
        verbs: list[str],
    ) -> None: ...
    def to_dict(self) -> V1ResourcePolicyRuleDict: ...

class V1ResourcePolicyRuleDict(typing.TypedDict, total=False):
    apiGroups: list[str]
    clusterScope: bool
    namespaces: list[str]
    resources: list[str]
    verbs: list[str]
