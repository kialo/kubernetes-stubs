import kubernetes.client
import typing

class V1alpha3BasicDevice:
    all_nodes: typing.Optional[bool]
    attributes: typing.Optional[dict[str, kubernetes.client.V1alpha3DeviceAttribute]]
    capacity: typing.Optional[dict[str, str]]
    consumes_counters: typing.Optional[
        list[kubernetes.client.V1alpha3DeviceCounterConsumption]
    ]
    node_name: typing.Optional[str]
    node_selector: typing.Optional[kubernetes.client.V1NodeSelector]
    taints: typing.Optional[list[kubernetes.client.V1alpha3DeviceTaint]]

    def __init__(
        self,
        *,
        all_nodes: typing.Optional[bool] = ...,
        attributes: typing.Optional[
            dict[str, kubernetes.client.V1alpha3DeviceAttribute]
        ] = ...,
        capacity: typing.Optional[dict[str, str]] = ...,
        consumes_counters: typing.Optional[
            list[kubernetes.client.V1alpha3DeviceCounterConsumption]
        ] = ...,
        node_name: typing.Optional[str] = ...,
        node_selector: typing.Optional[kubernetes.client.V1NodeSelector] = ...,
        taints: typing.Optional[list[kubernetes.client.V1alpha3DeviceTaint]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha3BasicDeviceDict: ...

class V1alpha3BasicDeviceDict(typing.TypedDict, total=False):
    allNodes: bool
    attributes: dict[str, kubernetes.client.V1alpha3DeviceAttributeDict]
    capacity: dict[str, str]
    consumesCounters: list[kubernetes.client.V1alpha3DeviceCounterConsumptionDict]
    nodeName: str
    nodeSelector: kubernetes.client.V1NodeSelectorDict
    taints: list[kubernetes.client.V1alpha3DeviceTaintDict]
