import kubernetes.client
import typing

class V1beta2DeviceSelector:
    cel: typing.Optional[kubernetes.client.V1beta2CELDeviceSelector]

    def __init__(
        self, *, cel: typing.Optional[kubernetes.client.V1beta2CELDeviceSelector] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta2DeviceSelectorDict: ...

class V1beta2DeviceSelectorDict(typing.TypedDict, total=False):
    cel: kubernetes.client.V1beta2CELDeviceSelectorDict
