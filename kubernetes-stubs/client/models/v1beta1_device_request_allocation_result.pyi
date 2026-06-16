import kubernetes.client
import typing

class V1beta1DeviceRequestAllocationResult:
    admin_access: typing.Optional[bool]
    binding_conditions: typing.Optional[list[str]]
    binding_failure_conditions: typing.Optional[list[str]]
    consumed_capacity: typing.Optional[dict[str, str]]
    device: str
    driver: str
    pool: str
    request: str
    share_id: typing.Optional[str]
    tolerations: typing.Optional[list[kubernetes.client.V1beta1DeviceToleration]]

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
            list[kubernetes.client.V1beta1DeviceToleration]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1DeviceRequestAllocationResultDict: ...

class V1beta1DeviceRequestAllocationResultDict(typing.TypedDict, total=False):
    adminAccess: bool
    bindingConditions: list[str]
    bindingFailureConditions: list[str]
    consumedCapacity: dict[str, str]
    device: str
    driver: str
    pool: str
    request: str
    shareID: str
    tolerations: list[kubernetes.client.V1beta1DeviceTolerationDict]
