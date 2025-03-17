import typing

class V1VolumeMount:
    mount_path: str
    mount_propagation: typing.Optional[str]
    name: str
    read_only: typing.Optional[bool]
    recursive_read_only: typing.Optional[str]
    sub_path: typing.Optional[str]
    sub_path_expr: typing.Optional[str]

    def __init__(
        self,
        *,
        mount_path: str,
        mount_propagation: typing.Optional[str] = ...,
        name: str,
        read_only: typing.Optional[bool] = ...,
        recursive_read_only: typing.Optional[str] = ...,
        sub_path: typing.Optional[str] = ...,
        sub_path_expr: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1VolumeMountDict: ...

class V1VolumeMountDict(typing.TypedDict, total=False):
    mountPath: str
    mountPropagation: str
    name: str
    readOnly: bool
    recursiveReadOnly: str
    subPath: str
    subPathExpr: str
