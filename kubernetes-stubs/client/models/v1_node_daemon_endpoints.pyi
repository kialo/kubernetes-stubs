import datetime
import kubernetes.client
import typing

class V1NodeDaemonEndpoints:
    kubelet_endpoint: typing.Optional[kubernetes.client.V1DaemonEndpoint]
    
    def __init__(self, *, kubelet_endpoint: typing.Optional[kubernetes.client.V1DaemonEndpoint] = ...) -> None:
        ...
    def to_dict(self) -> V1NodeDaemonEndpointsDict:
        ...
class V1NodeDaemonEndpointsDict(typing.TypedDict, total=False):
    kubeletEndpoint: typing.Optional[kubernetes.client.V1DaemonEndpointDict]
