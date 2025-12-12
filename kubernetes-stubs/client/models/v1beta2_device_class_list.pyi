import kubernetes.client
import typing

class V1beta2DeviceClassList:
    api_version: str
    items: list[kubernetes.client.V1beta2DeviceClass]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1beta2DeviceClass],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta2DeviceClassListDict: ...

class V1beta2DeviceClassListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1beta2DeviceClassDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
