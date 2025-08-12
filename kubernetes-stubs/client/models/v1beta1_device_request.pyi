import kubernetes.client
import typing

class V1beta1DeviceRequest:
    admin_access: typing.Optional[bool]
    allocation_mode: typing.Optional[str]
    count: typing.Optional[int]
    device_class_name: str
    name: str
    selectors: typing.Optional[list[kubernetes.client.V1beta1DeviceSelector]]

    def __init__(
        self,
        *,
        admin_access: typing.Optional[bool] = ...,
        allocation_mode: typing.Optional[str] = ...,
        count: typing.Optional[int] = ...,
        device_class_name: str,
        name: str,
        selectors: typing.Optional[list[kubernetes.client.V1beta1DeviceSelector]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1DeviceRequestDict: ...

class V1beta1DeviceRequestDict(typing.TypedDict, total=False):
    adminAccess: bool
    allocationMode: str
    count: int
    deviceClassName: str
    name: str
    selectors: list[kubernetes.client.V1beta1DeviceSelectorDict]
