import kubernetes.client
import typing

class V1PodTemplateList:
    api_version: str
    items: list[kubernetes.client.V1PodTemplate]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1PodTemplate],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1PodTemplateListDict: ...

class V1PodTemplateListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1PodTemplateDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
