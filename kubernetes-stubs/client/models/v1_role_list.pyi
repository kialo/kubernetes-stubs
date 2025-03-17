import kubernetes.client
import typing

class V1RoleList:
    api_version: str
    items: list[kubernetes.client.V1Role]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1Role],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1RoleListDict: ...

class V1RoleListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1RoleDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
