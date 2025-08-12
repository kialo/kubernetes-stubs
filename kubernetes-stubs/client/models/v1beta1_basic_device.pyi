import kubernetes.client
import typing

class V1beta1BasicDevice:
    attributes: typing.Optional[dict[str, kubernetes.client.V1beta1DeviceAttribute]]
    capacity: typing.Optional[dict[str, kubernetes.client.V1beta1DeviceCapacity]]

    def __init__(
        self,
        *,
        attributes: typing.Optional[
            dict[str, kubernetes.client.V1beta1DeviceAttribute]
        ] = ...,
        capacity: typing.Optional[
            dict[str, kubernetes.client.V1beta1DeviceCapacity]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1BasicDeviceDict: ...

class V1beta1BasicDeviceDict(typing.TypedDict, total=False):
    attributes: dict[str, kubernetes.client.V1beta1DeviceAttributeDict]
    capacity: dict[str, kubernetes.client.V1beta1DeviceCapacityDict]
