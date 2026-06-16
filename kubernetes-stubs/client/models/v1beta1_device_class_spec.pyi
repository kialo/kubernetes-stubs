import kubernetes.client
import typing

class V1beta1DeviceClassSpec:
    config: typing.Optional[list[kubernetes.client.V1beta1DeviceClassConfiguration]]
    extended_resource_name: typing.Optional[str]
    selectors: typing.Optional[list[kubernetes.client.V1beta1DeviceSelector]]

    def __init__(
        self,
        *,
        config: typing.Optional[
            list[kubernetes.client.V1beta1DeviceClassConfiguration]
        ] = ...,
        extended_resource_name: typing.Optional[str] = ...,
        selectors: typing.Optional[list[kubernetes.client.V1beta1DeviceSelector]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1DeviceClassSpecDict: ...

class V1beta1DeviceClassSpecDict(typing.TypedDict, total=False):
    config: list[kubernetes.client.V1beta1DeviceClassConfigurationDict]
    extendedResourceName: str
    selectors: list[kubernetes.client.V1beta1DeviceSelectorDict]
