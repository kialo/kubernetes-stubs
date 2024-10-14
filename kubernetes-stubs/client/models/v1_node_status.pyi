import kubernetes.client
import typing

class V1NodeStatus:
    addresses: typing.Optional[list[kubernetes.client.V1NodeAddress]]
    allocatable: typing.Optional[dict[str, str]]
    capacity: typing.Optional[dict[str, str]]
    conditions: typing.Optional[list[kubernetes.client.V1NodeCondition]]
    config: typing.Optional[kubernetes.client.V1NodeConfigStatus]
    daemon_endpoints: typing.Optional[kubernetes.client.V1NodeDaemonEndpoints]
    images: typing.Optional[list[kubernetes.client.V1ContainerImage]]
    node_info: typing.Optional[kubernetes.client.V1NodeSystemInfo]
    phase: typing.Optional[str]
    volumes_attached: typing.Optional[list[kubernetes.client.V1AttachedVolume]]
    volumes_in_use: typing.Optional[list[str]]

    def __init__(
        self,
        *,
        addresses: typing.Optional[list[kubernetes.client.V1NodeAddress]] = ...,
        allocatable: typing.Optional[dict[str, str]] = ...,
        capacity: typing.Optional[dict[str, str]] = ...,
        conditions: typing.Optional[list[kubernetes.client.V1NodeCondition]] = ...,
        config: typing.Optional[kubernetes.client.V1NodeConfigStatus] = ...,
        daemon_endpoints: typing.Optional[
            kubernetes.client.V1NodeDaemonEndpoints
        ] = ...,
        images: typing.Optional[list[kubernetes.client.V1ContainerImage]] = ...,
        node_info: typing.Optional[kubernetes.client.V1NodeSystemInfo] = ...,
        phase: typing.Optional[str] = ...,
        volumes_attached: typing.Optional[
            list[kubernetes.client.V1AttachedVolume]
        ] = ...,
        volumes_in_use: typing.Optional[list[str]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1NodeStatusDict: ...

class V1NodeStatusDict(typing.TypedDict, total=False):
    addresses: list[kubernetes.client.V1NodeAddressDict]
    allocatable: dict[str, str]
    capacity: dict[str, str]
    conditions: list[kubernetes.client.V1NodeConditionDict]
    config: kubernetes.client.V1NodeConfigStatusDict
    daemonEndpoints: kubernetes.client.V1NodeDaemonEndpointsDict
    images: list[kubernetes.client.V1ContainerImageDict]
    nodeInfo: kubernetes.client.V1NodeSystemInfoDict
    phase: str
    volumesAttached: list[kubernetes.client.V1AttachedVolumeDict]
    volumesInUse: list[str]
