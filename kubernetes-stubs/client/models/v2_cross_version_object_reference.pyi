import typing

class V2CrossVersionObjectReference:
    api_version: str
    kind: str
    name: str

    def __init__(
        self, *, api_version: typing.Optional[str] = ..., kind: str, name: str
    ) -> None: ...
    def to_dict(self) -> V2CrossVersionObjectReferenceDict: ...

class V2CrossVersionObjectReferenceDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    name: str
