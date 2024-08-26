import datetime
import kubernetes.client
import typing

class V1SleepAction:
    seconds: int
    
    def __init__(self, *, seconds: int) -> None:
        ...
    def to_dict(self) -> V1SleepActionDict:
        ...
class V1SleepActionDict(typing.TypedDict, total=False):
    seconds: int
