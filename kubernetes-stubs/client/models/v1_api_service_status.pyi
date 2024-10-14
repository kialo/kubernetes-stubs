import kubernetes.client
import typing

class V1APIServiceStatus:
    conditions: typing.Optional[list[kubernetes.client.V1APIServiceCondition]]

    def __init__(
        self,
        *,
        conditions: typing.Optional[
            list[kubernetes.client.V1APIServiceCondition]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1APIServiceStatusDict: ...

class V1APIServiceStatusDict(typing.TypedDict, total=False):
    conditions: list[kubernetes.client.V1APIServiceConditionDict]
