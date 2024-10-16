import kubernetes.client
import typing

class V1alpha1IPAddress:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    spec: kubernetes.client.V1alpha1IPAddressSpec

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1alpha1IPAddressSpec] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha1IPAddressDict: ...

class V1alpha1IPAddressDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    spec: kubernetes.client.V1alpha1IPAddressSpecDict
