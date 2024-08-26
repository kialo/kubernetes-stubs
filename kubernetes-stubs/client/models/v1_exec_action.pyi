import datetime
import kubernetes.client
import typing

class V1ExecAction:
    command: typing.Optional[list[str]]
    
    def __init__(self, *, command: typing.Optional[list[str]] = ...) -> None:
        ...
    def to_dict(self) -> V1ExecActionDict:
        ...
class V1ExecActionDict(typing.TypedDict, total=False):
    command: typing.Optional[list[str]]
