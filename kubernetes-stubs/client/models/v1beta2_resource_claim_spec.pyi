import kubernetes.client
import typing

class V1beta2ResourceClaimSpec:
    devices: typing.Optional[kubernetes.client.V1beta2DeviceClaim]

    def __init__(
        self, *, devices: typing.Optional[kubernetes.client.V1beta2DeviceClaim] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta2ResourceClaimSpecDict: ...

class V1beta2ResourceClaimSpecDict(typing.TypedDict, total=False):
    devices: kubernetes.client.V1beta2DeviceClaimDict
