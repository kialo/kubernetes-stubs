import kubernetes.client
import typing

class V1beta1TypeChecking:
    expression_warnings: typing.Optional[
        list[kubernetes.client.V1beta1ExpressionWarning]
    ]

    def __init__(
        self,
        *,
        expression_warnings: typing.Optional[
            list[kubernetes.client.V1beta1ExpressionWarning]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1TypeCheckingDict: ...

class V1beta1TypeCheckingDict(typing.TypedDict, total=False):
    expressionWarnings: list[kubernetes.client.V1beta1ExpressionWarningDict]
