import datetime
import kubernetes.client
import typing

class V1PodReadinessGate:
    condition_type: str
    
    def __init__(self, *, condition_type: str) -> None:
        ...
    def to_dict(self) -> V1PodReadinessGateDict:
        ...
class V1PodReadinessGateDict(typing.TypedDict, total=False):
    conditionType: str
