import datetime
import kubernetes.client
import typing

class EventsV1Event:
    action: typing.Optional[str]
    api_version: str
    deprecated_count: typing.Optional[int]
    deprecated_first_timestamp: typing.Optional[datetime.datetime]
    deprecated_last_timestamp: typing.Optional[datetime.datetime]
    deprecated_source: typing.Optional[kubernetes.client.V1EventSource]
    event_time: datetime.datetime
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    note: typing.Optional[str]
    reason: typing.Optional[str]
    regarding: typing.Optional[kubernetes.client.V1ObjectReference]
    related: typing.Optional[kubernetes.client.V1ObjectReference]
    reporting_controller: typing.Optional[str]
    reporting_instance: typing.Optional[str]
    series: typing.Optional[kubernetes.client.EventsV1EventSeries]
    type: typing.Optional[str]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = ...,
        api_version: typing.Optional[str] = ...,
        deprecated_count: typing.Optional[int] = ...,
        deprecated_first_timestamp: typing.Optional[datetime.datetime] = ...,
        deprecated_last_timestamp: typing.Optional[datetime.datetime] = ...,
        deprecated_source: typing.Optional[kubernetes.client.V1EventSource] = ...,
        event_time: datetime.datetime,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        note: typing.Optional[str] = ...,
        reason: typing.Optional[str] = ...,
        regarding: typing.Optional[kubernetes.client.V1ObjectReference] = ...,
        related: typing.Optional[kubernetes.client.V1ObjectReference] = ...,
        reporting_controller: typing.Optional[str] = ...,
        reporting_instance: typing.Optional[str] = ...,
        series: typing.Optional[kubernetes.client.EventsV1EventSeries] = ...,
        type: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> EventsV1EventDict: ...

class EventsV1EventDict(typing.TypedDict, total=False):
    action: str
    apiVersion: str
    deprecatedCount: int
    deprecatedFirstTimestamp: datetime.datetime
    deprecatedLastTimestamp: datetime.datetime
    deprecatedSource: kubernetes.client.V1EventSourceDict
    eventTime: datetime.datetime
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    note: str
    reason: str
    regarding: kubernetes.client.V1ObjectReferenceDict
    related: kubernetes.client.V1ObjectReferenceDict
    reportingController: str
    reportingInstance: str
    series: kubernetes.client.EventsV1EventSeriesDict
    type: str
