import kubernetes.client
import typing

class V1alpha3DeviceClaimConfiguration:
    opaque: typing.Optional[kubernetes.client.V1alpha3OpaqueDeviceConfiguration]
    requests: typing.Optional[list[str]]

    def __init__(
        self,
        *,
        opaque: typing.Optional[
            kubernetes.client.V1alpha3OpaqueDeviceConfiguration
        ] = ...,
        requests: typing.Optional[list[str]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha3DeviceClaimConfigurationDict: ...

class V1alpha3DeviceClaimConfigurationDict(typing.TypedDict, total=False):
    opaque: kubernetes.client.V1alpha3OpaqueDeviceConfigurationDict
    requests: list[str]
