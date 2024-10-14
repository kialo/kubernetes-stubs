import typing

class V1ResourceRule:
    api_groups: typing.Optional[list[str]]
    resource_names: typing.Optional[list[str]]
    resources: typing.Optional[list[str]]
    verbs: list[str]

    def __init__(
        self,
        *,
        api_groups: typing.Optional[list[str]] = ...,
        resource_names: typing.Optional[list[str]] = ...,
        resources: typing.Optional[list[str]] = ...,
        verbs: list[str],
    ) -> None: ...
    def to_dict(self) -> V1ResourceRuleDict: ...

class V1ResourceRuleDict(typing.TypedDict, total=False):
    apiGroups: list[str]
    resourceNames: list[str]
    resources: list[str]
    verbs: list[str]
