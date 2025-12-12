import kubernetes.client
import typing

class V1beta2Device:
    all_nodes: typing.Optional[bool]
    attributes: typing.Optional[dict[str, kubernetes.client.V1beta2DeviceAttribute]]
    capacity: typing.Optional[dict[str, kubernetes.client.V1beta2DeviceCapacity]]
    consumes_counters: typing.Optional[
        list[kubernetes.client.V1beta2DeviceCounterConsumption]
    ]
    name: str
    node_name: typing.Optional[str]
    node_selector: typing.Optional[kubernetes.client.V1NodeSelector]
    taints: typing.Optional[list[kubernetes.client.V1beta2DeviceTaint]]

    def __init__(
        self,
        *,
        all_nodes: typing.Optional[bool] = ...,
        attributes: typing.Optional[
            dict[str, kubernetes.client.V1beta2DeviceAttribute]
        ] = ...,
        capacity: typing.Optional[
            dict[str, kubernetes.client.V1beta2DeviceCapacity]
        ] = ...,
        consumes_counters: typing.Optional[
            list[kubernetes.client.V1beta2DeviceCounterConsumption]
        ] = ...,
        name: str,
        node_name: typing.Optional[str] = ...,
        node_selector: typing.Optional[kubernetes.client.V1NodeSelector] = ...,
        taints: typing.Optional[list[kubernetes.client.V1beta2DeviceTaint]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta2DeviceDict: ...

class V1beta2DeviceDict(typing.TypedDict, total=False):
    allNodes: bool
    attributes: dict[str, kubernetes.client.V1beta2DeviceAttributeDict]
    capacity: dict[str, kubernetes.client.V1beta2DeviceCapacityDict]
    consumesCounters: list[kubernetes.client.V1beta2DeviceCounterConsumptionDict]
    name: str
    nodeName: str
    nodeSelector: kubernetes.client.V1NodeSelectorDict
    taints: list[kubernetes.client.V1beta2DeviceTaintDict]
