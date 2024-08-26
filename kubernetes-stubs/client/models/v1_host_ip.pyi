import datetime
import kubernetes.client
import typing

class V1HostIP:
    ip: typing.Optional[str]
    
    def __init__(self, *, ip: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1HostIPDict:
        ...
class V1HostIPDict(typing.TypedDict, total=False):
    ip: typing.Optional[str]
