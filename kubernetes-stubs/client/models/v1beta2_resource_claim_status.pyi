import kubernetes.client
import typing

class V1beta2ResourceClaimStatus:
    allocation: typing.Optional[kubernetes.client.V1beta2AllocationResult]
    devices: typing.Optional[list[kubernetes.client.V1beta2AllocatedDeviceStatus]]
    reserved_for: typing.Optional[
        list[kubernetes.client.V1beta2ResourceClaimConsumerReference]
    ]

    def __init__(
        self,
        *,
        allocation: typing.Optional[kubernetes.client.V1beta2AllocationResult] = ...,
        devices: typing.Optional[
            list[kubernetes.client.V1beta2AllocatedDeviceStatus]
        ] = ...,
        reserved_for: typing.Optional[
            list[kubernetes.client.V1beta2ResourceClaimConsumerReference]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta2ResourceClaimStatusDict: ...

class V1beta2ResourceClaimStatusDict(typing.TypedDict, total=False):
    allocation: kubernetes.client.V1beta2AllocationResultDict
    devices: list[kubernetes.client.V1beta2AllocatedDeviceStatusDict]
    reservedFor: list[kubernetes.client.V1beta2ResourceClaimConsumerReferenceDict]
