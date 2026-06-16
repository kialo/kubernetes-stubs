import typing

class CoreV1ResourceClaim:
    name: str
    request: typing.Optional[str]

    def __init__(self, *, name: str, request: typing.Optional[str] = ...) -> None: ...
    def to_dict(self) -> CoreV1ResourceClaimDict: ...

class CoreV1ResourceClaimDict(typing.TypedDict, total=False):
    name: str
    request: str
