import kubernetes.client
import typing

class V1ClusterRoleBinding:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    role_ref: kubernetes.client.V1RoleRef
    subjects: typing.Optional[list[kubernetes.client.RbacV1Subject]]

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        role_ref: kubernetes.client.V1RoleRef,
        subjects: typing.Optional[list[kubernetes.client.RbacV1Subject]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ClusterRoleBindingDict: ...

class V1ClusterRoleBindingDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    roleRef: kubernetes.client.V1RoleRefDict
    subjects: list[kubernetes.client.RbacV1SubjectDict]
