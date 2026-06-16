import kubernetes.client
import typing

class V1ExactDeviceRequest:
    admin_access: typing.Optional[bool]
    allocation_mode: typing.Optional[str]
    capacity: typing.Optional[kubernetes.client.V1CapacityRequirements]
    count: typing.Optional[int]
    device_class_name: str
    selectors: typing.Optional[list[kubernetes.client.V1DeviceSelector]]
    tolerations: typing.Optional[list[kubernetes.client.V1DeviceToleration]]

    def __init__(
        self,
        *,
        admin_access: typing.Optional[bool] = ...,
        allocation_mode: typing.Optional[str] = ...,
        capacity: typing.Optional[kubernetes.client.V1CapacityRequirements] = ...,
        count: typing.Optional[int] = ...,
        device_class_name: str,
        selectors: typing.Optional[list[kubernetes.client.V1DeviceSelector]] = ...,
        tolerations: typing.Optional[list[kubernetes.client.V1DeviceToleration]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ExactDeviceRequestDict: ...

class V1ExactDeviceRequestDict(typing.TypedDict, total=False):
    adminAccess: bool
    allocationMode: str
    capacity: kubernetes.client.V1CapacityRequirementsDict
    count: int
    deviceClassName: str
    selectors: list[kubernetes.client.V1DeviceSelectorDict]
    tolerations: list[kubernetes.client.V1DeviceTolerationDict]
