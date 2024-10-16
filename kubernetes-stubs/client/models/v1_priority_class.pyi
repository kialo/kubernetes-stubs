import kubernetes.client
import typing

class V1PriorityClass:
    api_version: str
    description: typing.Optional[str]
    global_default: typing.Optional[bool]
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    preemption_policy: typing.Optional[str]
    value: int

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        description: typing.Optional[str] = ...,
        global_default: typing.Optional[bool] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        preemption_policy: typing.Optional[str] = ...,
        value: int,
    ) -> None: ...
    def to_dict(self) -> V1PriorityClassDict: ...

class V1PriorityClassDict(typing.TypedDict, total=False):
    apiVersion: str
    description: str
    globalDefault: bool
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    preemptionPolicy: str
    value: int
