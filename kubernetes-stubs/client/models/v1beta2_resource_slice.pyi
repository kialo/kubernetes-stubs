import kubernetes.client
import typing

class V1beta2ResourceSlice:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    spec: kubernetes.client.V1beta2ResourceSliceSpec

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: kubernetes.client.V1beta2ResourceSliceSpec,
    ) -> None: ...
    def to_dict(self) -> V1beta2ResourceSliceDict: ...

class V1beta2ResourceSliceDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    spec: kubernetes.client.V1beta2ResourceSliceSpecDict
