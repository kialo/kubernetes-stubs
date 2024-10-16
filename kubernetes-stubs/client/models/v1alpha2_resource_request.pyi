import kubernetes.client
import typing

class V1alpha2ResourceRequest:
    named_resources: typing.Optional[kubernetes.client.V1alpha2NamedResourcesRequest]
    vendor_parameters: typing.Optional[typing.Any]

    def __init__(
        self,
        *,
        named_resources: typing.Optional[
            kubernetes.client.V1alpha2NamedResourcesRequest
        ] = ...,
        vendor_parameters: typing.Optional[typing.Any] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha2ResourceRequestDict: ...

class V1alpha2ResourceRequestDict(typing.TypedDict, total=False):
    namedResources: kubernetes.client.V1alpha2NamedResourcesRequestDict
    vendorParameters: typing.Any