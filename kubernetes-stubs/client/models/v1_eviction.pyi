import kubernetes.client
import typing

class V1Eviction:
    api_version: str
    delete_options: typing.Optional[kubernetes.client.V1DeleteOptions]
    kind: str
    metadata: kubernetes.client.V1ObjectMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        delete_options: typing.Optional[kubernetes.client.V1DeleteOptions] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1EvictionDict: ...

class V1EvictionDict(typing.TypedDict, total=False):
    apiVersion: str
    deleteOptions: kubernetes.client.V1DeleteOptionsDict
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
