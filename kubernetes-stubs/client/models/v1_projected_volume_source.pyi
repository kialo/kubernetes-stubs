import kubernetes.client
import typing

class V1ProjectedVolumeSource:
    default_mode: typing.Optional[int]
    sources: typing.Optional[list[kubernetes.client.V1VolumeProjection]]

    def __init__(
        self,
        *,
        default_mode: typing.Optional[int] = ...,
        sources: typing.Optional[list[kubernetes.client.V1VolumeProjection]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ProjectedVolumeSourceDict: ...

class V1ProjectedVolumeSourceDict(typing.TypedDict, total=False):
    defaultMode: int
    sources: list[kubernetes.client.V1VolumeProjectionDict]
