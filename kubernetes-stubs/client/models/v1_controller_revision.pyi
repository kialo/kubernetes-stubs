import kubernetes.client
import typing

class V1ControllerRevision:
    api_version: str
    data: typing.Optional[typing.Any]
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    revision: int

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        data: typing.Optional[typing.Any] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        revision: int,
    ) -> None: ...
    def to_dict(self) -> V1ControllerRevisionDict: ...

class V1ControllerRevisionDict(typing.TypedDict, total=False):
    apiVersion: str
    data: typing.Any
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    revision: int
