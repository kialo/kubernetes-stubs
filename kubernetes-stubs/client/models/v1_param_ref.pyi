import kubernetes.client
import typing

class V1ParamRef:
    name: typing.Optional[str]
    namespace: typing.Optional[str]
    parameter_not_found_action: typing.Optional[str]
    selector: typing.Optional[kubernetes.client.V1LabelSelector]

    def __init__(
        self,
        *,
        name: typing.Optional[str] = ...,
        namespace: typing.Optional[str] = ...,
        parameter_not_found_action: typing.Optional[str] = ...,
        selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ParamRefDict: ...

class V1ParamRefDict(typing.TypedDict, total=False):
    name: str
    namespace: str
    parameterNotFoundAction: str
    selector: kubernetes.client.V1LabelSelectorDict