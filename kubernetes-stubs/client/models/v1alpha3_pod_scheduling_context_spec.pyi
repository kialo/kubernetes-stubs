import typing

class V1alpha3PodSchedulingContextSpec:
    potential_nodes: typing.Optional[list[str]]
    selected_node: typing.Optional[str]

    def __init__(
        self,
        *,
        potential_nodes: typing.Optional[list[str]] = ...,
        selected_node: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha3PodSchedulingContextSpecDict: ...

class V1alpha3PodSchedulingContextSpecDict(typing.TypedDict, total=False):
    potentialNodes: list[str]
    selectedNode: str
