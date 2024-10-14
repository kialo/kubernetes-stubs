import kubernetes.client
import typing

class V1StorageClass:
    allow_volume_expansion: typing.Optional[bool]
    allowed_topologies: typing.Optional[list[kubernetes.client.V1TopologySelectorTerm]]
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    mount_options: typing.Optional[list[str]]
    parameters: typing.Optional[dict[str, str]]
    provisioner: str
    reclaim_policy: typing.Optional[str]
    volume_binding_mode: typing.Optional[str]

    def __init__(
        self,
        *,
        allow_volume_expansion: typing.Optional[bool] = ...,
        allowed_topologies: typing.Optional[
            list[kubernetes.client.V1TopologySelectorTerm]
        ] = ...,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        mount_options: typing.Optional[list[str]] = ...,
        parameters: typing.Optional[dict[str, str]] = ...,
        provisioner: str,
        reclaim_policy: typing.Optional[str] = ...,
        volume_binding_mode: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1StorageClassDict: ...

class V1StorageClassDict(typing.TypedDict, total=False):
    allowVolumeExpansion: bool
    allowedTopologies: list[kubernetes.client.V1TopologySelectorTermDict]
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    mountOptions: list[str]
    parameters: dict[str, str]
    provisioner: str
    reclaimPolicy: str
    volumeBindingMode: str
