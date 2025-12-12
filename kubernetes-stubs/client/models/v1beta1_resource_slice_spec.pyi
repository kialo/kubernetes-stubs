import kubernetes.client
import typing

class V1beta1ResourceSliceSpec:
    all_nodes: typing.Optional[bool]
    devices: typing.Optional[list[kubernetes.client.V1beta1Device]]
    driver: str
    node_name: typing.Optional[str]
    node_selector: typing.Optional[kubernetes.client.V1NodeSelector]
    per_device_node_selection: typing.Optional[bool]
    pool: kubernetes.client.V1beta1ResourcePool
    shared_counters: typing.Optional[list[kubernetes.client.V1beta1CounterSet]]

    def __init__(
        self,
        *,
        all_nodes: typing.Optional[bool] = ...,
        devices: typing.Optional[list[kubernetes.client.V1beta1Device]] = ...,
        driver: str,
        node_name: typing.Optional[str] = ...,
        node_selector: typing.Optional[kubernetes.client.V1NodeSelector] = ...,
        per_device_node_selection: typing.Optional[bool] = ...,
        pool: kubernetes.client.V1beta1ResourcePool,
        shared_counters: typing.Optional[
            list[kubernetes.client.V1beta1CounterSet]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1ResourceSliceSpecDict: ...

class V1beta1ResourceSliceSpecDict(typing.TypedDict, total=False):
    allNodes: bool
    devices: list[kubernetes.client.V1beta1DeviceDict]
    driver: str
    nodeName: str
    nodeSelector: kubernetes.client.V1NodeSelectorDict
    perDeviceNodeSelection: bool
    pool: kubernetes.client.V1beta1ResourcePoolDict
    sharedCounters: list[kubernetes.client.V1beta1CounterSetDict]
