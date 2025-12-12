import kubernetes.client
import typing

class V1alpha3DeviceTaintSelector:
    device: typing.Optional[str]
    device_class_name: typing.Optional[str]
    driver: typing.Optional[str]
    pool: typing.Optional[str]
    selectors: typing.Optional[list[kubernetes.client.V1alpha3DeviceSelector]]

    def __init__(
        self,
        *,
        device: typing.Optional[str] = ...,
        device_class_name: typing.Optional[str] = ...,
        driver: typing.Optional[str] = ...,
        pool: typing.Optional[str] = ...,
        selectors: typing.Optional[
            list[kubernetes.client.V1alpha3DeviceSelector]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha3DeviceTaintSelectorDict: ...

class V1alpha3DeviceTaintSelectorDict(typing.TypedDict, total=False):
    device: str
    deviceClassName: str
    driver: str
    pool: str
    selectors: list[kubernetes.client.V1alpha3DeviceSelectorDict]
