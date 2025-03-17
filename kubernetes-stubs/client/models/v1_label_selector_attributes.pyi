import kubernetes.client
import typing

class V1LabelSelectorAttributes:
    raw_selector: typing.Optional[str]
    requirements: typing.Optional[list[kubernetes.client.V1LabelSelectorRequirement]]

    def __init__(
        self,
        *,
        raw_selector: typing.Optional[str] = ...,
        requirements: typing.Optional[
            list[kubernetes.client.V1LabelSelectorRequirement]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1LabelSelectorAttributesDict: ...

class V1LabelSelectorAttributesDict(typing.TypedDict, total=False):
    rawSelector: str
    requirements: list[kubernetes.client.V1LabelSelectorRequirementDict]
