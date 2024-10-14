import typing

class V1alpha1ParamKind:
    api_version: str
    kind: str

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha1ParamKindDict: ...

class V1alpha1ParamKindDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
