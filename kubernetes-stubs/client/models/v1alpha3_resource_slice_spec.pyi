import kubernetes.client
import typing

class V1alpha3ResourceSliceSpec:
    all_nodes: typing.Optional[bool]
    devices: typing.Optional[list[kubernetes.client.V1alpha3Device]]
    driver: str
    node_name: typing.Optional[str]
    node_selector: typing.Optional[kubernetes.client.V1NodeSelector]
    per_device_node_selection: typing.Optional[bool]
    pool: kubernetes.client.V1alpha3ResourcePool
    shared_counters: typing.Optional[list[kubernetes.client.V1alpha3CounterSet]]

    def __init__(
        self,
        *,
        all_nodes: typing.Optional[bool] = ...,
        devices: typing.Optional[list[kubernetes.client.V1alpha3Device]] = ...,
        driver: str,
        node_name: typing.Optional[str] = ...,
        node_selector: typing.Optional[kubernetes.client.V1NodeSelector] = ...,
        per_device_node_selection: typing.Optional[bool] = ...,
        pool: kubernetes.client.V1alpha3ResourcePool,
        shared_counters: typing.Optional[
            list[kubernetes.client.V1alpha3CounterSet]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha3ResourceSliceSpecDict: ...

class V1alpha3ResourceSliceSpecDict(typing.TypedDict, total=False):
    allNodes: bool
    devices: list[kubernetes.client.V1alpha3DeviceDict]
    driver: str
    nodeName: str
    nodeSelector: kubernetes.client.V1NodeSelectorDict
    perDeviceNodeSelection: bool
    pool: kubernetes.client.V1alpha3ResourcePoolDict
    sharedCounters: list[kubernetes.client.V1alpha3CounterSetDict]
