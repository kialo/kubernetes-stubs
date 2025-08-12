import kubernetes.client
import typing

class V1beta1ResourceClaimStatus:
    allocation: typing.Optional[kubernetes.client.V1beta1AllocationResult]
    devices: typing.Optional[list[kubernetes.client.V1beta1AllocatedDeviceStatus]]
    reserved_for: typing.Optional[
        list[kubernetes.client.V1beta1ResourceClaimConsumerReference]
    ]

    def __init__(
        self,
        *,
        allocation: typing.Optional[kubernetes.client.V1beta1AllocationResult] = ...,
        devices: typing.Optional[
            list[kubernetes.client.V1beta1AllocatedDeviceStatus]
        ] = ...,
        reserved_for: typing.Optional[
            list[kubernetes.client.V1beta1ResourceClaimConsumerReference]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1ResourceClaimStatusDict: ...

class V1beta1ResourceClaimStatusDict(typing.TypedDict, total=False):
    allocation: kubernetes.client.V1beta1AllocationResultDict
    devices: list[kubernetes.client.V1beta1AllocatedDeviceStatusDict]
    reservedFor: list[kubernetes.client.V1beta1ResourceClaimConsumerReferenceDict]
