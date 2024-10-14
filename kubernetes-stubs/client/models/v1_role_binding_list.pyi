import kubernetes.client
import typing

class V1RoleBindingList:
    api_version: str
    items: list[kubernetes.client.V1RoleBinding]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1RoleBinding],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1RoleBindingListDict: ...

class V1RoleBindingListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1RoleBindingDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
