import kubernetes.client
import typing

class V1CSIDriver:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    spec: kubernetes.client.V1CSIDriverSpec

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: kubernetes.client.V1CSIDriverSpec,
    ) -> None: ...
    def to_dict(self) -> V1CSIDriverDict: ...

class V1CSIDriverDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    spec: kubernetes.client.V1CSIDriverSpecDict
