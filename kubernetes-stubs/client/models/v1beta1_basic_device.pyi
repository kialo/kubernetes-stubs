import kubernetes.client
import typing

class V1beta1BasicDevice:
    all_nodes: typing.Optional[bool]
    attributes: typing.Optional[dict[str, kubernetes.client.V1beta1DeviceAttribute]]
    capacity: typing.Optional[dict[str, kubernetes.client.V1beta1DeviceCapacity]]
    consumes_counters: typing.Optional[
        list[kubernetes.client.V1beta1DeviceCounterConsumption]
    ]
    node_name: typing.Optional[str]
    node_selector: typing.Optional[kubernetes.client.V1NodeSelector]
    taints: typing.Optional[list[kubernetes.client.V1beta1DeviceTaint]]

    def __init__(
        self,
        *,
        all_nodes: typing.Optional[bool] = ...,
        attributes: typing.Optional[
            dict[str, kubernetes.client.V1beta1DeviceAttribute]
        ] = ...,
        capacity: typing.Optional[
            dict[str, kubernetes.client.V1beta1DeviceCapacity]
        ] = ...,
        consumes_counters: typing.Optional[
            list[kubernetes.client.V1beta1DeviceCounterConsumption]
        ] = ...,
        node_name: typing.Optional[str] = ...,
        node_selector: typing.Optional[kubernetes.client.V1NodeSelector] = ...,
        taints: typing.Optional[list[kubernetes.client.V1beta1DeviceTaint]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1BasicDeviceDict: ...

class V1beta1BasicDeviceDict(typing.TypedDict, total=False):
    allNodes: bool
    attributes: dict[str, kubernetes.client.V1beta1DeviceAttributeDict]
    capacity: dict[str, kubernetes.client.V1beta1DeviceCapacityDict]
    consumesCounters: list[kubernetes.client.V1beta1DeviceCounterConsumptionDict]
    nodeName: str
    nodeSelector: kubernetes.client.V1NodeSelectorDict
    taints: list[kubernetes.client.V1beta1DeviceTaintDict]
