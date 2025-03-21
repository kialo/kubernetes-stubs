import typing

class V1ResourceFieldSelector:
    container_name: typing.Optional[str]
    divisor: typing.Optional[str]
    resource: str

    def __init__(
        self,
        *,
        container_name: typing.Optional[str] = ...,
        divisor: typing.Optional[str] = ...,
        resource: str,
    ) -> None: ...
    def to_dict(self) -> V1ResourceFieldSelectorDict: ...

class V1ResourceFieldSelectorDict(typing.TypedDict, total=False):
    containerName: str
    divisor: str
    resource: str
