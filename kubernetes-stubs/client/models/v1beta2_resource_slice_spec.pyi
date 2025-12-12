import kubernetes.client
import typing

class V1beta2ResourceSliceSpec:
    all_nodes: typing.Optional[bool]
    devices: typing.Optional[list[kubernetes.client.V1beta2Device]]
    driver: str
    node_name: typing.Optional[str]
    node_selector: typing.Optional[kubernetes.client.V1NodeSelector]
    per_device_node_selection: typing.Optional[bool]
    pool: kubernetes.client.V1beta2ResourcePool
    shared_counters: typing.Optional[list[kubernetes.client.V1beta2CounterSet]]

    def __init__(
        self,
        *,
        all_nodes: typing.Optional[bool] = ...,
        devices: typing.Optional[list[kubernetes.client.V1beta2Device]] = ...,
        driver: str,
        node_name: typing.Optional[str] = ...,
        node_selector: typing.Optional[kubernetes.client.V1NodeSelector] = ...,
        per_device_node_selection: typing.Optional[bool] = ...,
        pool: kubernetes.client.V1beta2ResourcePool,
        shared_counters: typing.Optional[
            list[kubernetes.client.V1beta2CounterSet]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta2ResourceSliceSpecDict: ...

class V1beta2ResourceSliceSpecDict(typing.TypedDict, total=False):
    allNodes: bool
    devices: list[kubernetes.client.V1beta2DeviceDict]
    driver: str
    nodeName: str
    nodeSelector: kubernetes.client.V1NodeSelectorDict
    perDeviceNodeSelection: bool
    pool: kubernetes.client.V1beta2ResourcePoolDict
    sharedCounters: list[kubernetes.client.V1beta2CounterSetDict]
