import typing

class V1alpha3DeviceRequestAllocationResult:
    admin_access: typing.Optional[bool]
    device: str
    driver: str
    pool: str
    request: str

    def __init__(
        self,
        *,
        admin_access: typing.Optional[bool] = ...,
        device: str,
        driver: str,
        pool: str,
        request: str,
    ) -> None: ...
    def to_dict(self) -> V1alpha3DeviceRequestAllocationResultDict: ...

class V1alpha3DeviceRequestAllocationResultDict(typing.TypedDict, total=False):
    adminAccess: bool
    device: str
    driver: str
    pool: str
    request: str
