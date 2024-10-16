import kubernetes.client
import typing

class V1Endpoints:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    subsets: typing.Optional[list[kubernetes.client.V1EndpointSubset]]

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        subsets: typing.Optional[list[kubernetes.client.V1EndpointSubset]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1EndpointsDict: ...

class V1EndpointsDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    subsets: list[kubernetes.client.V1EndpointSubsetDict]
