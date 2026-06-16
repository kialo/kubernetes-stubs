import kubernetes.client
import typing

class V1beta2DeviceRequestAllocationResult:
    admin_access: typing.Optional[bool]
    binding_conditions: typing.Optional[list[str]]
    binding_failure_conditions: typing.Optional[list[str]]
    consumed_capacity: typing.Optional[dict[str, str]]
    device: str
    driver: str
    pool: str
    request: str
    share_id: typing.Optional[str]
    tolerations: typing.Optional[list[kubernetes.client.V1beta2DeviceToleration]]

    def __init__(
        self,
        *,
        admin_access: typing.Optional[bool] = ...,
        binding_conditions: typing.Optional[list[str]] = ...,
        binding_failure_conditions: typing.Optional[list[str]] = ...,
        consumed_capacity: typing.Optional[dict[str, str]] = ...,
        device: str,
        driver: str,
        pool: str,
        request: str,
        share_id: typing.Optional[str] = ...,
        tolerations: typing.Optional[
            list[kubernetes.client.V1beta2DeviceToleration]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta2DeviceRequestAllocationResultDict: ...

class V1beta2DeviceRequestAllocationResultDict(typing.TypedDict, total=False):
    adminAccess: bool
    bindingConditions: list[str]
    bindingFailureConditions: list[str]
    consumedCapacity: dict[str, str]
    device: str
    driver: str
    pool: str
    request: str
    shareID: str
    tolerations: list[kubernetes.client.V1beta2DeviceTolerationDict]
