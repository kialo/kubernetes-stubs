import kubernetes.client
import typing

class V1beta2ResourceClaimTemplateList:
    api_version: str
    items: list[kubernetes.client.V1beta2ResourceClaimTemplate]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1beta2ResourceClaimTemplate],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta2ResourceClaimTemplateListDict: ...

class V1beta2ResourceClaimTemplateListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1beta2ResourceClaimTemplateDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
