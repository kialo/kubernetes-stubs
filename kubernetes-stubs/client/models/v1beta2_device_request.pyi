import kubernetes.client
import typing

class V1beta2DeviceRequest:
    exactly: typing.Optional[kubernetes.client.V1beta2ExactDeviceRequest]
    first_available: typing.Optional[list[kubernetes.client.V1beta2DeviceSubRequest]]
    name: str

    def __init__(
        self,
        *,
        exactly: typing.Optional[kubernetes.client.V1beta2ExactDeviceRequest] = ...,
        first_available: typing.Optional[
            list[kubernetes.client.V1beta2DeviceSubRequest]
        ] = ...,
        name: str,
    ) -> None: ...
    def to_dict(self) -> V1beta2DeviceRequestDict: ...

class V1beta2DeviceRequestDict(typing.TypedDict, total=False):
    exactly: kubernetes.client.V1beta2ExactDeviceRequestDict
    firstAvailable: list[kubernetes.client.V1beta2DeviceSubRequestDict]
    name: str
