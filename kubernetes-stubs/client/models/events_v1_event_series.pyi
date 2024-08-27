import datetime
import typing

class EventsV1EventSeries:
    count: int
    last_observed_time: datetime.datetime

    def __init__(
        self, *, count: int, last_observed_time: datetime.datetime
    ) -> None: ...
    def to_dict(self) -> EventsV1EventSeriesDict: ...

class EventsV1EventSeriesDict(typing.TypedDict, total=False):
    count: int
    lastObservedTime: datetime.datetime
