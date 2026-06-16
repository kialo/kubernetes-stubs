import kubernetes.client
import typing

class V1DeviceSubRequest:
    allocation_mode: typing.Optional[str]
    capacity: typing.Optional[kubernetes.client.V1CapacityRequirements]
    count: typing.Optional[int]
    device_class_name: str
    name: str
    selectors: typing.Optional[list[kubernetes.client.V1DeviceSelector]]
    tolerations: typing.Optional[list[kubernetes.client.V1DeviceToleration]]

    def __init__(
        self,
        *,
        allocation_mode: typing.Optional[str] = ...,
        capacity: typing.Optional[kubernetes.client.V1CapacityRequirements] = ...,
        count: typing.Optional[int] = ...,
        device_class_name: str,
        name: str,
        selectors: typing.Optional[list[kubernetes.client.V1DeviceSelector]] = ...,
        tolerations: typing.Optional[list[kubernetes.client.V1DeviceToleration]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1DeviceSubRequestDict: ...

class V1DeviceSubRequestDict(typing.TypedDict, total=False):
    allocationMode: str
    capacity: kubernetes.client.V1CapacityRequirementsDict
    count: int
    deviceClassName: str
    name: str
    selectors: list[kubernetes.client.V1DeviceSelectorDict]
    tolerations: list[kubernetes.client.V1DeviceTolerationDict]
