import typing

class V1IngressPortStatus:
    error: typing.Optional[str]
    port: int
    protocol: str

    def __init__(
        self, *, error: typing.Optional[str] = ..., port: int, protocol: str
    ) -> None: ...
    def to_dict(self) -> V1IngressPortStatusDict: ...

class V1IngressPortStatusDict(typing.TypedDict, total=False):
    error: str
    port: int
    protocol: str
