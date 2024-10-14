import kubernetes.client
import typing

class V1DeploymentList:
    api_version: str
    items: list[kubernetes.client.V1Deployment]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1Deployment],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1DeploymentListDict: ...

class V1DeploymentListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1DeploymentDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
