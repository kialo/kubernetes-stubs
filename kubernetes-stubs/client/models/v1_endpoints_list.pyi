import kubernetes.client
import typing

class V1EndpointsList:
    api_version: str
    items: list[kubernetes.client.V1Endpoints]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1Endpoints],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1EndpointsListDict: ...

class V1EndpointsListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1EndpointsDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
