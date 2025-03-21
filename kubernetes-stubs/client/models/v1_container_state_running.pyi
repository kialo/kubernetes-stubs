import datetime
import typing

class V1ContainerStateRunning:
    started_at: typing.Optional[datetime.datetime]

    def __init__(
        self, *, started_at: typing.Optional[datetime.datetime] = ...
    ) -> None: ...
    def to_dict(self) -> V1ContainerStateRunningDict: ...

class V1ContainerStateRunningDict(typing.TypedDict, total=False):
    startedAt: datetime.datetime
