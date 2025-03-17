import typing

class V1ParamKind:
    api_version: str
    kind: str

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ParamKindDict: ...

class V1ParamKindDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
