import kubernetes.client
import typing

class V1beta1DeviceClaim:
    config: typing.Optional[list[kubernetes.client.V1beta1DeviceClaimConfiguration]]
    constraints: typing.Optional[list[kubernetes.client.V1beta1DeviceConstraint]]
    requests: typing.Optional[list[kubernetes.client.V1beta1DeviceRequest]]

    def __init__(
        self,
        *,
        config: typing.Optional[
            list[kubernetes.client.V1beta1DeviceClaimConfiguration]
        ] = ...,
        constraints: typing.Optional[
            list[kubernetes.client.V1beta1DeviceConstraint]
        ] = ...,
        requests: typing.Optional[list[kubernetes.client.V1beta1DeviceRequest]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1DeviceClaimDict: ...

class V1beta1DeviceClaimDict(typing.TypedDict, total=False):
    config: list[kubernetes.client.V1beta1DeviceClaimConfigurationDict]
    constraints: list[kubernetes.client.V1beta1DeviceConstraintDict]
    requests: list[kubernetes.client.V1beta1DeviceRequestDict]
