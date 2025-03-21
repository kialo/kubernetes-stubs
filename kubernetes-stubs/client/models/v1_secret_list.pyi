import kubernetes.client
import typing

class V1SecretList:
    api_version: str
    items: list[kubernetes.client.V1Secret]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1Secret],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1SecretListDict: ...

class V1SecretListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1SecretDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
