import datetime
import kubernetes.client
import typing

class V1ResourceClaim:
    name: str
    
    def __init__(self, *, name: str) -> None:
        ...
    def to_dict(self) -> V1ResourceClaimDict:
        ...
class V1ResourceClaimDict(typing.TypedDict, total=False):
    name: str
