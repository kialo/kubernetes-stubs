import datetime
import typing

class V1beta3FlowSchemaCondition:
    last_transition_time: typing.Optional[datetime.datetime]
    message: typing.Optional[str]
    reason: typing.Optional[str]
    status: typing.Optional[str]
    type: typing.Optional[str]

    def __init__(
        self,
        *,
        last_transition_time: typing.Optional[datetime.datetime] = ...,
        message: typing.Optional[str] = ...,
        reason: typing.Optional[str] = ...,
        status: typing.Optional[str] = ...,
        type: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta3FlowSchemaConditionDict: ...

class V1beta3FlowSchemaConditionDict(typing.TypedDict, total=False):
    lastTransitionTime: datetime.datetime
    message: str
    reason: str
    status: str
    type: str
