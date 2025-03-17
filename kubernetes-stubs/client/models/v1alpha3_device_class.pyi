import kubernetes.client
import typing

class V1alpha3DeviceClass:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    spec: kubernetes.client.V1alpha3DeviceClassSpec

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: kubernetes.client.V1alpha3DeviceClassSpec,
    ) -> None: ...
    def to_dict(self) -> V1alpha3DeviceClassDict: ...

class V1alpha3DeviceClassDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    spec: kubernetes.client.V1alpha3DeviceClassSpecDict
