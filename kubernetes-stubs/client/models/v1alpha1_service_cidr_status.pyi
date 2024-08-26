import datetime
import kubernetes.client
import typing

class V1alpha1ServiceCIDRStatus:
    conditions: typing.Optional[list[kubernetes.client.V1Condition]]
    
    def __init__(self, *, conditions: typing.Optional[list[kubernetes.client.V1Condition]] = ...) -> None:
        ...
    def to_dict(self) -> V1alpha1ServiceCIDRStatusDict:
        ...
class V1alpha1ServiceCIDRStatusDict(typing.TypedDict, total=False):
    conditions: typing.Optional[list[kubernetes.client.V1ConditionDict]]
