import kubernetes.client
import typing

class V1Lifecycle:
    post_start: typing.Optional[kubernetes.client.V1LifecycleHandler]
    pre_stop: typing.Optional[kubernetes.client.V1LifecycleHandler]

    def __init__(
        self,
        *,
        post_start: typing.Optional[kubernetes.client.V1LifecycleHandler] = ...,
        pre_stop: typing.Optional[kubernetes.client.V1LifecycleHandler] = ...,
    ) -> None: ...
    def to_dict(self) -> V1LifecycleDict: ...

class V1LifecycleDict(typing.TypedDict, total=False):
    postStart: kubernetes.client.V1LifecycleHandlerDict
    preStop: kubernetes.client.V1LifecycleHandlerDict
