import typing

class V1UserSubject:
    name: str

    def __init__(self, *, name: str) -> None: ...
    def to_dict(self) -> V1UserSubjectDict: ...

class V1UserSubjectDict(typing.TypedDict, total=False):
    name: str
