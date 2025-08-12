import kubernetes.client
import typing

class V1beta1DeviceClaimConfiguration:
    opaque: typing.Optional[kubernetes.client.V1beta1OpaqueDeviceConfiguration]
    requests: typing.Optional[list[str]]

    def __init__(
        self,
        *,
        opaque: typing.Optional[
            kubernetes.client.V1beta1OpaqueDeviceConfiguration
        ] = ...,
        requests: typing.Optional[list[str]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1DeviceClaimConfigurationDict: ...

class V1beta1DeviceClaimConfigurationDict(typing.TypedDict, total=False):
    opaque: kubernetes.client.V1beta1OpaqueDeviceConfigurationDict
    requests: list[str]
