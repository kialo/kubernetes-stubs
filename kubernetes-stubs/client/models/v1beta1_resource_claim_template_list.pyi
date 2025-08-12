import kubernetes.client
import typing

class V1beta1ResourceClaimTemplateList:
    api_version: str
    items: list[kubernetes.client.V1beta1ResourceClaimTemplate]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1beta1ResourceClaimTemplate],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1ResourceClaimTemplateListDict: ...

class V1beta1ResourceClaimTemplateListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1beta1ResourceClaimTemplateDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
