import kubernetes.client
import typing

class V1MutatingWebhookConfigurationList:
    api_version: str
    items: list[kubernetes.client.V1MutatingWebhookConfiguration]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1MutatingWebhookConfiguration],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1MutatingWebhookConfigurationListDict: ...

class V1MutatingWebhookConfigurationListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1MutatingWebhookConfigurationDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
