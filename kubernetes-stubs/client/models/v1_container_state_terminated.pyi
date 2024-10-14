import datetime
import typing

class V1ContainerStateTerminated:
    container_id: typing.Optional[str]
    exit_code: int
    finished_at: typing.Optional[datetime.datetime]
    message: typing.Optional[str]
    reason: typing.Optional[str]
    signal: typing.Optional[int]
    started_at: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        container_id: typing.Optional[str] = ...,
        exit_code: int,
        finished_at: typing.Optional[datetime.datetime] = ...,
        message: typing.Optional[str] = ...,
        reason: typing.Optional[str] = ...,
        signal: typing.Optional[int] = ...,
        started_at: typing.Optional[datetime.datetime] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ContainerStateTerminatedDict: ...

class V1ContainerStateTerminatedDict(typing.TypedDict, total=False):
    containerID: str
    exitCode: int
    finishedAt: datetime.datetime
    message: str
    reason: str
    signal: int
    startedAt: datetime.datetime
