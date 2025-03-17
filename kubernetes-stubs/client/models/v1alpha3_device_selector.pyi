import kubernetes.client
import typing

class V1alpha3DeviceSelector:
    cel: typing.Optional[kubernetes.client.V1alpha3CELDeviceSelector]

    def __init__(
        self, *, cel: typing.Optional[kubernetes.client.V1alpha3CELDeviceSelector] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha3DeviceSelectorDict: ...

class V1alpha3DeviceSelectorDict(typing.TypedDict, total=False):
    cel: kubernetes.client.V1alpha3CELDeviceSelectorDict
