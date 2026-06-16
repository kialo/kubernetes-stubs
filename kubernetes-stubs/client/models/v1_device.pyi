import kubernetes.client
import typing

class V1Device:
    all_nodes: typing.Optional[bool]
    allow_multiple_allocations: typing.Optional[bool]
    attributes: typing.Optional[dict[str, kubernetes.client.V1DeviceAttribute]]
    binding_conditions: typing.Optional[list[str]]
    binding_failure_conditions: typing.Optional[list[str]]
    binds_to_node: typing.Optional[bool]
    capacity: typing.Optional[dict[str, kubernetes.client.V1DeviceCapacity]]
    consumes_counters: typing.Optional[
        list[kubernetes.client.V1DeviceCounterConsumption]
    ]
    name: str
    node_name: typing.Optional[str]
    node_selector: typing.Optional[kubernetes.client.V1NodeSelector]
    taints: typing.Optional[list[kubernetes.client.V1DeviceTaint]]

    def __init__(
        self,
        *,
        all_nodes: typing.Optional[bool] = ...,
        allow_multiple_allocations: typing.Optional[bool] = ...,
        attributes: typing.Optional[
            dict[str, kubernetes.client.V1DeviceAttribute]
        ] = ...,
        binding_conditions: typing.Optional[list[str]] = ...,
        binding_failure_conditions: typing.Optional[list[str]] = ...,
        binds_to_node: typing.Optional[bool] = ...,
        capacity: typing.Optional[dict[str, kubernetes.client.V1DeviceCapacity]] = ...,
        consumes_counters: typing.Optional[
            list[kubernetes.client.V1DeviceCounterConsumption]
        ] = ...,
        name: str,
        node_name: typing.Optional[str] = ...,
        node_selector: typing.Optional[kubernetes.client.V1NodeSelector] = ...,
        taints: typing.Optional[list[kubernetes.client.V1DeviceTaint]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1DeviceDict: ...

class V1DeviceDict(typing.TypedDict, total=False):
    allNodes: bool
    allowMultipleAllocations: bool
    attributes: dict[str, kubernetes.client.V1DeviceAttributeDict]
    bindingConditions: list[str]
    bindingFailureConditions: list[str]
    bindsToNode: bool
    capacity: dict[str, kubernetes.client.V1DeviceCapacityDict]
    consumesCounters: list[kubernetes.client.V1DeviceCounterConsumptionDict]
    name: str
    nodeName: str
    nodeSelector: kubernetes.client.V1NodeSelectorDict
    taints: list[kubernetes.client.V1DeviceTaintDict]
