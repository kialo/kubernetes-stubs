import kubernetes.client
import typing

class V1ContainerState:
    running: typing.Optional[kubernetes.client.V1ContainerStateRunning]
    terminated: typing.Optional[kubernetes.client.V1ContainerStateTerminated]
    waiting: typing.Optional[kubernetes.client.V1ContainerStateWaiting]

    def __init__(
        self,
        *,
        running: typing.Optional[kubernetes.client.V1ContainerStateRunning] = ...,
        terminated: typing.Optional[kubernetes.client.V1ContainerStateTerminated] = ...,
        waiting: typing.Optional[kubernetes.client.V1ContainerStateWaiting] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ContainerStateDict: ...

class V1ContainerStateDict(typing.TypedDict, total=False):
    running: kubernetes.client.V1ContainerStateRunningDict
    terminated: kubernetes.client.V1ContainerStateTerminatedDict
    waiting: kubernetes.client.V1ContainerStateWaitingDict
