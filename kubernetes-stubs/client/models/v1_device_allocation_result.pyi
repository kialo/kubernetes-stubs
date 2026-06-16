import kubernetes.client
import typing

class V1DeviceAllocationResult:
    config: typing.Optional[list[kubernetes.client.V1DeviceAllocationConfiguration]]
    results: typing.Optional[list[kubernetes.client.V1DeviceRequestAllocationResult]]

    def __init__(
        self,
        *,
        config: typing.Optional[
            list[kubernetes.client.V1DeviceAllocationConfiguration]
        ] = ...,
        results: typing.Optional[
            list[kubernetes.client.V1DeviceRequestAllocationResult]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1DeviceAllocationResultDict: ...

class V1DeviceAllocationResultDict(typing.TypedDict, total=False):
    config: list[kubernetes.client.V1DeviceAllocationConfigurationDict]
    results: list[kubernetes.client.V1DeviceRequestAllocationResultDict]
