import kubernetes.client
import typing

class V1beta2DeviceSubRequest:
    allocation_mode: typing.Optional[str]
    count: typing.Optional[int]
    device_class_name: str
    name: str
    selectors: typing.Optional[list[kubernetes.client.V1beta2DeviceSelector]]
    tolerations: typing.Optional[list[kubernetes.client.V1beta2DeviceToleration]]

    def __init__(
        self,
        *,
        allocation_mode: typing.Optional[str] = ...,
        count: typing.Optional[int] = ...,
        device_class_name: str,
        name: str,
        selectors: typing.Optional[list[kubernetes.client.V1beta2DeviceSelector]] = ...,
        tolerations: typing.Optional[
            list[kubernetes.client.V1beta2DeviceToleration]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta2DeviceSubRequestDict: ...

class V1beta2DeviceSubRequestDict(typing.TypedDict, total=False):
    allocationMode: str
    count: int
    deviceClassName: str
    name: str
    selectors: list[kubernetes.client.V1beta2DeviceSelectorDict]
    tolerations: list[kubernetes.client.V1beta2DeviceTolerationDict]
