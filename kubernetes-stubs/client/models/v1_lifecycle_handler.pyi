import kubernetes.client
import typing

class V1LifecycleHandler:
    exec: typing.Optional[kubernetes.client.V1ExecAction]
    http_get: typing.Optional[kubernetes.client.V1HTTPGetAction]
    sleep: typing.Optional[kubernetes.client.V1SleepAction]
    tcp_socket: typing.Optional[kubernetes.client.V1TCPSocketAction]

    def __init__(
        self,
        *,
        exec: typing.Optional[kubernetes.client.V1ExecAction] = ...,
        http_get: typing.Optional[kubernetes.client.V1HTTPGetAction] = ...,
        sleep: typing.Optional[kubernetes.client.V1SleepAction] = ...,
        tcp_socket: typing.Optional[kubernetes.client.V1TCPSocketAction] = ...,
    ) -> None: ...
    def to_dict(self) -> V1LifecycleHandlerDict: ...

class V1LifecycleHandlerDict(typing.TypedDict, total=False):
    exec: kubernetes.client.V1ExecActionDict
    httpGet: kubernetes.client.V1HTTPGetActionDict
    sleep: kubernetes.client.V1SleepActionDict
    tcpSocket: kubernetes.client.V1TCPSocketActionDict
