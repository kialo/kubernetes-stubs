import typing

class V1StatefulSetOrdinals:
    start: typing.Optional[int]

    def __init__(self, *, start: typing.Optional[int] = ...) -> None: ...
    def to_dict(self) -> V1StatefulSetOrdinalsDict: ...

class V1StatefulSetOrdinalsDict(typing.TypedDict, total=False):
    start: int
