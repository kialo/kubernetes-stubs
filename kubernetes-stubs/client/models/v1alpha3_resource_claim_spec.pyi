import kubernetes.client
import typing

class V1alpha3ResourceClaimSpec:
    controller: typing.Optional[str]
    devices: typing.Optional[kubernetes.client.V1alpha3DeviceClaim]

    def __init__(
        self,
        *,
        controller: typing.Optional[str] = ...,
        devices: typing.Optional[kubernetes.client.V1alpha3DeviceClaim] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha3ResourceClaimSpecDict: ...

class V1alpha3ResourceClaimSpecDict(typing.TypedDict, total=False):
    controller: str
    devices: kubernetes.client.V1alpha3DeviceClaimDict
