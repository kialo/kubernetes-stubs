import kubernetes.client
import typing

class V1ResourceClaimSpec:
    devices: typing.Optional[kubernetes.client.V1DeviceClaim]

    def __init__(
        self, *, devices: typing.Optional[kubernetes.client.V1DeviceClaim] = ...
    ) -> None: ...
    def to_dict(self) -> V1ResourceClaimSpecDict: ...

class V1ResourceClaimSpecDict(typing.TypedDict, total=False):
    devices: kubernetes.client.V1DeviceClaimDict
