import kubernetes.client
import typing

class V1EnvVar:
    name: str
    value: typing.Optional[str]
    value_from: typing.Optional[kubernetes.client.V1EnvVarSource]

    def __init__(
        self,
        *,
        name: str,
        value: typing.Optional[str] = ...,
        value_from: typing.Optional[kubernetes.client.V1EnvVarSource] = ...,
    ) -> None: ...
    def to_dict(self) -> V1EnvVarDict: ...

class V1EnvVarDict(typing.TypedDict, total=False):
    name: str
    value: str
    valueFrom: kubernetes.client.V1EnvVarSourceDict