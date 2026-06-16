import kubernetes.client
import typing

class V1beta2DeviceClassSpec:
    config: typing.Optional[list[kubernetes.client.V1beta2DeviceClassConfiguration]]
    extended_resource_name: typing.Optional[str]
    selectors: typing.Optional[list[kubernetes.client.V1beta2DeviceSelector]]

    def __init__(
        self,
        *,
        config: typing.Optional[
            list[kubernetes.client.V1beta2DeviceClassConfiguration]
        ] = ...,
        extended_resource_name: typing.Optional[str] = ...,
        selectors: typing.Optional[list[kubernetes.client.V1beta2DeviceSelector]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta2DeviceClassSpecDict: ...

class V1beta2DeviceClassSpecDict(typing.TypedDict, total=False):
    config: list[kubernetes.client.V1beta2DeviceClassConfigurationDict]
    extendedResourceName: str
    selectors: list[kubernetes.client.V1beta2DeviceSelectorDict]
