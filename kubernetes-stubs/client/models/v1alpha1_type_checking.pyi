import kubernetes.client
import typing

class V1alpha1TypeChecking:
    expression_warnings: typing.Optional[
        list[kubernetes.client.V1alpha1ExpressionWarning]
    ]

    def __init__(
        self,
        *,
        expression_warnings: typing.Optional[
            list[kubernetes.client.V1alpha1ExpressionWarning]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha1TypeCheckingDict: ...

class V1alpha1TypeCheckingDict(typing.TypedDict, total=False):
    expressionWarnings: list[kubernetes.client.V1alpha1ExpressionWarningDict]
