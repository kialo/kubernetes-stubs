import kubernetes.client
import typing

class V1ResourceQuotaSpec:
    hard: typing.Optional[dict[str, str]]
    scope_selector: typing.Optional[kubernetes.client.V1ScopeSelector]
    scopes: typing.Optional[list[str]]

    def __init__(
        self,
        *,
        hard: typing.Optional[dict[str, str]] = ...,
        scope_selector: typing.Optional[kubernetes.client.V1ScopeSelector] = ...,
        scopes: typing.Optional[list[str]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ResourceQuotaSpecDict: ...

class V1ResourceQuotaSpecDict(typing.TypedDict, total=False):
    hard: dict[str, str]
    scopeSelector: kubernetes.client.V1ScopeSelectorDict
    scopes: list[str]
