import kubernetes.client
import typing

class V1NodeRuntimeHandler:
    features: typing.Optional[kubernetes.client.V1NodeRuntimeHandlerFeatures]
    name: typing.Optional[str]

    def __init__(
        self,
        *,
        features: typing.Optional[kubernetes.client.V1NodeRuntimeHandlerFeatures] = ...,
        name: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1NodeRuntimeHandlerDict: ...

class V1NodeRuntimeHandlerDict(typing.TypedDict, total=False):
    features: kubernetes.client.V1NodeRuntimeHandlerFeaturesDict
    name: str
