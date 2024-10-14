import kubernetes.client
import typing

class V1CustomResourceDefinitionList:
    api_version: str
    items: list[kubernetes.client.V1CustomResourceDefinition]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1CustomResourceDefinition],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1CustomResourceDefinitionListDict: ...

class V1CustomResourceDefinitionListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1CustomResourceDefinitionDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
