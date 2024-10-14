import kubernetes.client
import typing

class V1alpha1IPAddressList:
    api_version: str
    items: list[kubernetes.client.V1alpha1IPAddress]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1alpha1IPAddress],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha1IPAddressListDict: ...

class V1alpha1IPAddressListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1alpha1IPAddressDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict