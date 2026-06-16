import typing

class V1DeviceAttribute:
    bool: typing.Optional[bool]
    int: typing.Optional[int]
    string: typing.Optional[str]
    version: typing.Optional[str]

    def __init__(
        self,
        *,
        bool: typing.Optional[bool] = ...,
        int: typing.Optional[int] = ...,
        string: typing.Optional[str] = ...,
        version: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1DeviceAttributeDict: ...

class V1DeviceAttributeDict(typing.TypedDict, total=False):
    bool: bool
    int: int
    string: str
    version: str
