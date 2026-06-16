import kubernetes.client
import typing

class V1DeviceClassSpec:
    config: typing.Optional[list[kubernetes.client.V1DeviceClassConfiguration]]
    extended_resource_name: typing.Optional[str]
    selectors: typing.Optional[list[kubernetes.client.V1DeviceSelector]]

    def __init__(
        self,
        *,
        config: typing.Optional[
            list[kubernetes.client.V1DeviceClassConfiguration]
        ] = ...,
        extended_resource_name: typing.Optional[str] = ...,
        selectors: typing.Optional[list[kubernetes.client.V1DeviceSelector]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1DeviceClassSpecDict: ...

class V1DeviceClassSpecDict(typing.TypedDict, total=False):
    config: list[kubernetes.client.V1DeviceClassConfigurationDict]
    extendedResourceName: str
    selectors: list[kubernetes.client.V1DeviceSelectorDict]
