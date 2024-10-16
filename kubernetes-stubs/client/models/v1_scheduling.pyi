import kubernetes.client
import typing

class V1Scheduling:
    node_selector: typing.Optional[dict[str, str]]
    tolerations: typing.Optional[list[kubernetes.client.V1Toleration]]

    def __init__(
        self,
        *,
        node_selector: typing.Optional[dict[str, str]] = ...,
        tolerations: typing.Optional[list[kubernetes.client.V1Toleration]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1SchedulingDict: ...

class V1SchedulingDict(typing.TypedDict, total=False):
    nodeSelector: dict[str, str]
    tolerations: list[kubernetes.client.V1TolerationDict]