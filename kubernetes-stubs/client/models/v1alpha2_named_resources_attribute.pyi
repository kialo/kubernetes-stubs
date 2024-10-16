import kubernetes.client
import typing

class V1alpha2NamedResourcesAttribute:
    bool: typing.Optional[bool]
    int: typing.Optional[int]
    int_slice: typing.Optional[kubernetes.client.V1alpha2NamedResourcesIntSlice]
    name: str
    quantity: typing.Optional[str]
    string: typing.Optional[str]
    string_slice: typing.Optional[kubernetes.client.V1alpha2NamedResourcesStringSlice]
    version: typing.Optional[str]

    def __init__(
        self,
        *,
        bool: typing.Optional[bool] = ...,
        int: typing.Optional[int] = ...,
        int_slice: typing.Optional[
            kubernetes.client.V1alpha2NamedResourcesIntSlice
        ] = ...,
        name: str,
        quantity: typing.Optional[str] = ...,
        string: typing.Optional[str] = ...,
        string_slice: typing.Optional[
            kubernetes.client.V1alpha2NamedResourcesStringSlice
        ] = ...,
        version: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha2NamedResourcesAttributeDict: ...

class V1alpha2NamedResourcesAttributeDict(typing.TypedDict, total=False):
    bool: bool
    int: int
    intSlice: kubernetes.client.V1alpha2NamedResourcesIntSliceDict
    name: str
    quantity: str
    string: str
    stringSlice: kubernetes.client.V1alpha2NamedResourcesStringSliceDict
    version: str
