import typing

class V1ValidationRule:
    field_path: typing.Optional[str]
    message: typing.Optional[str]
    message_expression: typing.Optional[str]
    optional_old_self: typing.Optional[bool]
    reason: typing.Optional[str]
    rule: str

    def __init__(
        self,
        *,
        field_path: typing.Optional[str] = ...,
        message: typing.Optional[str] = ...,
        message_expression: typing.Optional[str] = ...,
        optional_old_self: typing.Optional[bool] = ...,
        reason: typing.Optional[str] = ...,
        rule: str,
    ) -> None: ...
    def to_dict(self) -> V1ValidationRuleDict: ...

class V1ValidationRuleDict(typing.TypedDict, total=False):
    fieldPath: str
    message: str
    messageExpression: str
    optionalOldSelf: bool
    reason: str
    rule: str
