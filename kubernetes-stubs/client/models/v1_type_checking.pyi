import kubernetes.client
import typing

class V1TypeChecking:
    expression_warnings: typing.Optional[list[kubernetes.client.V1ExpressionWarning]]

    def __init__(
        self,
        *,
        expression_warnings: typing.Optional[
            list[kubernetes.client.V1ExpressionWarning]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1TypeCheckingDict: ...

class V1TypeCheckingDict(typing.TypedDict, total=False):
    expressionWarnings: list[kubernetes.client.V1ExpressionWarningDict]
