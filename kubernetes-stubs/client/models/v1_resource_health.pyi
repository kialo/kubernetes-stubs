import typing

class V1ResourceHealth:
    health: typing.Optional[str]
    resource_id: str

    def __init__(
        self, *, health: typing.Optional[str] = ..., resource_id: str
    ) -> None: ...
    def to_dict(self) -> V1ResourceHealthDict: ...

class V1ResourceHealthDict(typing.TypedDict, total=False):
    health: str
    resourceID: str
