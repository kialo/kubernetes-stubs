import typing

class V1CapacityRequestPolicyRange:
    max: typing.Optional[str]
    min: str
    step: typing.Optional[str]

    def __init__(
        self,
        *,
        max: typing.Optional[str] = ...,
        min: str,
        step: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1CapacityRequestPolicyRangeDict: ...

class V1CapacityRequestPolicyRangeDict(typing.TypedDict, total=False):
    max: str
    min: str
    step: str
