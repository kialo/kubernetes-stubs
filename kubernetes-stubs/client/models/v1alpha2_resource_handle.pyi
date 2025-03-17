import kubernetes.client
import typing

class V1alpha2ResourceHandle:
    data: typing.Optional[str]
    driver_name: typing.Optional[str]
    structured_data: typing.Optional[kubernetes.client.V1alpha2StructuredResourceHandle]

    def __init__(
        self,
        *,
        data: typing.Optional[str] = ...,
        driver_name: typing.Optional[str] = ...,
        structured_data: typing.Optional[
            kubernetes.client.V1alpha2StructuredResourceHandle
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha2ResourceHandleDict: ...

class V1alpha2ResourceHandleDict(typing.TypedDict, total=False):
    data: str
    driverName: str
    structuredData: kubernetes.client.V1alpha2StructuredResourceHandleDict
