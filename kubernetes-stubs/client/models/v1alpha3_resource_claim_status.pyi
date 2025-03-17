import kubernetes.client
import typing

class V1alpha3ResourceClaimStatus:
    allocation: typing.Optional[kubernetes.client.V1alpha3AllocationResult]
    deallocation_requested: typing.Optional[bool]
    reserved_for: typing.Optional[
        list[kubernetes.client.V1alpha3ResourceClaimConsumerReference]
    ]

    def __init__(
        self,
        *,
        allocation: typing.Optional[kubernetes.client.V1alpha3AllocationResult] = ...,
        deallocation_requested: typing.Optional[bool] = ...,
        reserved_for: typing.Optional[
            list[kubernetes.client.V1alpha3ResourceClaimConsumerReference]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha3ResourceClaimStatusDict: ...

class V1alpha3ResourceClaimStatusDict(typing.TypedDict, total=False):
    allocation: kubernetes.client.V1alpha3AllocationResultDict
    deallocationRequested: bool
    reservedFor: list[kubernetes.client.V1alpha3ResourceClaimConsumerReferenceDict]
