import kubernetes.client
import typing

class V1beta1VolumeAttributesClassList:
    api_version: str
    items: list[kubernetes.client.V1beta1VolumeAttributesClass]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1beta1VolumeAttributesClass],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1VolumeAttributesClassListDict: ...

class V1beta1VolumeAttributesClassListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1beta1VolumeAttributesClassDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
