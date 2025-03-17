import kubernetes.client
import typing

class V1ConfigMapProjection:
    items: typing.Optional[list[kubernetes.client.V1KeyToPath]]
    name: typing.Optional[str]
    optional: typing.Optional[bool]

    def __init__(
        self,
        *,
        items: typing.Optional[list[kubernetes.client.V1KeyToPath]] = ...,
        name: typing.Optional[str] = ...,
        optional: typing.Optional[bool] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ConfigMapProjectionDict: ...

class V1ConfigMapProjectionDict(typing.TypedDict, total=False):
    items: list[kubernetes.client.V1KeyToPathDict]
    name: str
    optional: bool
