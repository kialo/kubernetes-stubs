import kubernetes.client
import typing

class V1alpha3ResourceClaimTemplateList:
    api_version: str
    items: list[kubernetes.client.V1alpha3ResourceClaimTemplate]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1alpha3ResourceClaimTemplate],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha3ResourceClaimTemplateListDict: ...

class V1alpha3ResourceClaimTemplateListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1alpha3ResourceClaimTemplateDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
