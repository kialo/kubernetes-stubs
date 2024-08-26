import datetime
import kubernetes.client
import typing

class V1ForZone:
    name: str
    
    def __init__(self, *, name: str) -> None:
        ...
    def to_dict(self) -> V1ForZoneDict:
        ...
class V1ForZoneDict(typing.TypedDict, total=False):
    name: str
