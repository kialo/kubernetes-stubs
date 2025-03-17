import kubernetes.client
import typing

class V1alpha3DeviceClassSpec:
    config: typing.Optional[list[kubernetes.client.V1alpha3DeviceClassConfiguration]]
    selectors: typing.Optional[list[kubernetes.client.V1alpha3DeviceSelector]]
    suitable_nodes: typing.Optional[kubernetes.client.V1NodeSelector]

    def __init__(
        self,
        *,
        config: typing.Optional[
            list[kubernetes.client.V1alpha3DeviceClassConfiguration]
        ] = ...,
        selectors: typing.Optional[
            list[kubernetes.client.V1alpha3DeviceSelector]
        ] = ...,
        suitable_nodes: typing.Optional[kubernetes.client.V1NodeSelector] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha3DeviceClassSpecDict: ...

class V1alpha3DeviceClassSpecDict(typing.TypedDict, total=False):
    config: list[kubernetes.client.V1alpha3DeviceClassConfigurationDict]
    selectors: list[kubernetes.client.V1alpha3DeviceSelectorDict]
    suitableNodes: kubernetes.client.V1NodeSelectorDict
