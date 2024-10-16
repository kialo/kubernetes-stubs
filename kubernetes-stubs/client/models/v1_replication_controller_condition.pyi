import datetime
import typing

class V1ReplicationControllerCondition:
    last_transition_time: typing.Optional[datetime.datetime]
    message: typing.Optional[str]
    reason: typing.Optional[str]
    status: str
    type: str

    def __init__(
        self,
        *,
        last_transition_time: typing.Optional[datetime.datetime] = ...,
        message: typing.Optional[str] = ...,
        reason: typing.Optional[str] = ...,
        status: str,
        type: str,
    ) -> None: ...
    def to_dict(self) -> V1ReplicationControllerConditionDict: ...

class V1ReplicationControllerConditionDict(typing.TypedDict, total=False):
    lastTransitionTime: datetime.datetime
    message: str
    reason: str
    status: str
    type: str