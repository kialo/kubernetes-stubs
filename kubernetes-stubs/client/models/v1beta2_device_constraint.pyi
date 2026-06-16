import typing

class V1beta2DeviceConstraint:
    distinct_attribute: typing.Optional[str]
    match_attribute: typing.Optional[str]
    requests: typing.Optional[list[str]]

    def __init__(
        self,
        *,
        distinct_attribute: typing.Optional[str] = ...,
        match_attribute: typing.Optional[str] = ...,
        requests: typing.Optional[list[str]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta2DeviceConstraintDict: ...

class V1beta2DeviceConstraintDict(typing.TypedDict, total=False):
    distinctAttribute: str
    matchAttribute: str
    requests: list[str]
