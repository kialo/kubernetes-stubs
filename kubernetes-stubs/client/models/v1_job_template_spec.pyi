import kubernetes.client
import typing

class V1JobTemplateSpec:
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes.client.V1JobSpec]

    def __init__(
        self,
        *,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1JobSpec] = ...,
    ) -> None: ...
    def to_dict(self) -> V1JobTemplateSpecDict: ...

class V1JobTemplateSpecDict(typing.TypedDict, total=False):
    metadata: kubernetes.client.V1ObjectMetaDict
    spec: kubernetes.client.V1JobSpecDict
