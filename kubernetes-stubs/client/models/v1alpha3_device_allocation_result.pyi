import kubernetes.client
import typing

class V1alpha3DeviceAllocationResult:
    config: typing.Optional[
        list[kubernetes.client.V1alpha3DeviceAllocationConfiguration]
    ]
    results: typing.Optional[
        list[kubernetes.client.V1alpha3DeviceRequestAllocationResult]
    ]

    def __init__(
        self,
        *,
        config: typing.Optional[
            list[kubernetes.client.V1alpha3DeviceAllocationConfiguration]
        ] = ...,
        results: typing.Optional[
            list[kubernetes.client.V1alpha3DeviceRequestAllocationResult]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha3DeviceAllocationResultDict: ...

class V1alpha3DeviceAllocationResultDict(typing.TypedDict, total=False):
    config: list[kubernetes.client.V1alpha3DeviceAllocationConfigurationDict]
    results: list[kubernetes.client.V1alpha3DeviceRequestAllocationResultDict]
