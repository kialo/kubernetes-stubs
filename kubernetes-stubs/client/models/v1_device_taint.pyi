import datetime
import typing

class V1DeviceTaint:
    effect: str
    key: str
    time_added: typing.Optional[datetime.datetime]
    value: typing.Optional[str]

    def __init__(
        self,
        *,
        effect: str,
        key: str,
        time_added: typing.Optional[datetime.datetime] = ...,
        value: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1DeviceTaintDict: ...

class V1DeviceTaintDict(typing.TypedDict, total=False):
    effect: str
    key: str
    timeAdded: datetime.datetime
    value: str
