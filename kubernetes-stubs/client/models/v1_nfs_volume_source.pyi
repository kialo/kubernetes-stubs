import typing

class V1NFSVolumeSource:
    path: str
    read_only: typing.Optional[bool]
    server: str

    def __init__(
        self, *, path: str, read_only: typing.Optional[bool] = ..., server: str
    ) -> None: ...
    def to_dict(self) -> V1NFSVolumeSourceDict: ...

class V1NFSVolumeSourceDict(typing.TypedDict, total=False):
    path: str
    readOnly: bool
    server: str
