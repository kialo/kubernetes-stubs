import kubernetes.client
import typing

class V1IPAddressList:
    api_version: str
    items: list[kubernetes.client.V1IPAddress]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1IPAddress],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1IPAddressListDict: ...

class V1IPAddressListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1IPAddressDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
