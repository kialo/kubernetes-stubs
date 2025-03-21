import kubernetes.client
import typing

class V1PodDisruptionBudget:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    spec: kubernetes.client.V1PodDisruptionBudgetSpec
    status: kubernetes.client.V1PodDisruptionBudgetStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1PodDisruptionBudgetSpec] = ...,
        status: typing.Optional[kubernetes.client.V1PodDisruptionBudgetStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> V1PodDisruptionBudgetDict: ...

class V1PodDisruptionBudgetDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    spec: kubernetes.client.V1PodDisruptionBudgetSpecDict
    status: kubernetes.client.V1PodDisruptionBudgetStatusDict
