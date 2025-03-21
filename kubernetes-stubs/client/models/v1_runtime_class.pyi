import kubernetes.client
import typing

class V1RuntimeClass:
    api_version: str
    handler: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    overhead: typing.Optional[kubernetes.client.V1Overhead]
    scheduling: typing.Optional[kubernetes.client.V1Scheduling]

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        handler: str,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        overhead: typing.Optional[kubernetes.client.V1Overhead] = ...,
        scheduling: typing.Optional[kubernetes.client.V1Scheduling] = ...,
    ) -> None: ...
    def to_dict(self) -> V1RuntimeClassDict: ...

class V1RuntimeClassDict(typing.TypedDict, total=False):
    apiVersion: str
    handler: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    overhead: kubernetes.client.V1OverheadDict
    scheduling: kubernetes.client.V1SchedulingDict
