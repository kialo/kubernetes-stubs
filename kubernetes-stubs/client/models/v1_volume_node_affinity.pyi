import kubernetes.client
import typing

class V1VolumeNodeAffinity:
    required: typing.Optional[kubernetes.client.V1NodeSelector]

    def __init__(
        self, *, required: typing.Optional[kubernetes.client.V1NodeSelector] = ...
    ) -> None: ...
    def to_dict(self) -> V1VolumeNodeAffinityDict: ...

class V1VolumeNodeAffinityDict(typing.TypedDict, total=False):
    required: kubernetes.client.V1NodeSelectorDict
