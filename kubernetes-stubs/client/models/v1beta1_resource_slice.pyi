import kubernetes.client
import typing

class V1beta1ResourceSlice:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    spec: kubernetes.client.V1beta1ResourceSliceSpec

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: kubernetes.client.V1beta1ResourceSliceSpec,
    ) -> None: ...
    def to_dict(self) -> V1beta1ResourceSliceDict: ...

class V1beta1ResourceSliceDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    spec: kubernetes.client.V1beta1ResourceSliceSpecDict
