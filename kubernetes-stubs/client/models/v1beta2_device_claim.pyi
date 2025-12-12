import kubernetes.client
import typing

class V1beta2DeviceClaim:
    config: typing.Optional[list[kubernetes.client.V1beta2DeviceClaimConfiguration]]
    constraints: typing.Optional[list[kubernetes.client.V1beta2DeviceConstraint]]
    requests: typing.Optional[list[kubernetes.client.V1beta2DeviceRequest]]

    def __init__(
        self,
        *,
        config: typing.Optional[
            list[kubernetes.client.V1beta2DeviceClaimConfiguration]
        ] = ...,
        constraints: typing.Optional[
            list[kubernetes.client.V1beta2DeviceConstraint]
        ] = ...,
        requests: typing.Optional[list[kubernetes.client.V1beta2DeviceRequest]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta2DeviceClaimDict: ...

class V1beta2DeviceClaimDict(typing.TypedDict, total=False):
    config: list[kubernetes.client.V1beta2DeviceClaimConfigurationDict]
    constraints: list[kubernetes.client.V1beta2DeviceConstraintDict]
    requests: list[kubernetes.client.V1beta2DeviceRequestDict]
