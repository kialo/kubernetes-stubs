import kubernetes.client
import typing

class V1alpha3BasicDevice:
    attributes: typing.Optional[dict[str, kubernetes.client.V1alpha3DeviceAttribute]]
    capacity: typing.Optional[dict[str, str]]

    def __init__(
        self,
        *,
        attributes: typing.Optional[
            dict[str, kubernetes.client.V1alpha3DeviceAttribute]
        ] = ...,
        capacity: typing.Optional[dict[str, str]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha3BasicDeviceDict: ...

class V1alpha3BasicDeviceDict(typing.TypedDict, total=False):
    attributes: dict[str, kubernetes.client.V1alpha3DeviceAttributeDict]
    capacity: dict[str, str]
