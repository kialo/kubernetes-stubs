import kubernetes.client
import typing

class V1CSIStorageCapacity:
    api_version: str
    capacity: typing.Optional[str]
    kind: str
    maximum_volume_size: typing.Optional[str]
    metadata: kubernetes.client.V1ObjectMeta
    node_topology: typing.Optional[kubernetes.client.V1LabelSelector]
    storage_class_name: str

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        capacity: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        maximum_volume_size: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        node_topology: typing.Optional[kubernetes.client.V1LabelSelector] = ...,
        storage_class_name: str,
    ) -> None: ...
    def to_dict(self) -> V1CSIStorageCapacityDict: ...

class V1CSIStorageCapacityDict(typing.TypedDict, total=False):
    apiVersion: str
    capacity: str
    kind: str
    maximumVolumeSize: str
    metadata: kubernetes.client.V1ObjectMetaDict
    nodeTopology: kubernetes.client.V1LabelSelectorDict
    storageClassName: str
