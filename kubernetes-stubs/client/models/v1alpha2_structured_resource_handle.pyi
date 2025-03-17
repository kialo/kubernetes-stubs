import kubernetes.client
import typing

class V1alpha2StructuredResourceHandle:
    node_name: typing.Optional[str]
    results: list[kubernetes.client.V1alpha2DriverAllocationResult]
    vendor_claim_parameters: typing.Optional[typing.Any]
    vendor_class_parameters: typing.Optional[typing.Any]

    def __init__(
        self,
        *,
        node_name: typing.Optional[str] = ...,
        results: list[kubernetes.client.V1alpha2DriverAllocationResult],
        vendor_claim_parameters: typing.Optional[typing.Any] = ...,
        vendor_class_parameters: typing.Optional[typing.Any] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha2StructuredResourceHandleDict: ...

class V1alpha2StructuredResourceHandleDict(typing.TypedDict, total=False):
    nodeName: str
    results: list[kubernetes.client.V1alpha2DriverAllocationResultDict]
    vendorClaimParameters: typing.Any
    vendorClassParameters: typing.Any
