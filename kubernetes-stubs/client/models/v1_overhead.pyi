import typing

class V1Overhead:
    pod_fixed: typing.Optional[dict[str, str]]

    def __init__(self, *, pod_fixed: typing.Optional[dict[str, str]] = ...) -> None: ...
    def to_dict(self) -> V1OverheadDict: ...

class V1OverheadDict(typing.TypedDict, total=False):
    podFixed: dict[str, str]
