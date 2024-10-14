import kubernetes.client
import typing

class V1NetworkPolicy:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    spec: kubernetes.client.V1NetworkPolicySpec

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1NetworkPolicySpec] = ...,
    ) -> None: ...
    def to_dict(self) -> V1NetworkPolicyDict: ...

class V1NetworkPolicyDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    spec: kubernetes.client.V1NetworkPolicySpecDict
