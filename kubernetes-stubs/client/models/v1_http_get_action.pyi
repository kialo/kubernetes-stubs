import kubernetes.client
import typing

class V1HTTPGetAction:
    host: typing.Optional[str]
    http_headers: typing.Optional[list[kubernetes.client.V1HTTPHeader]]
    path: typing.Optional[str]
    port: typing.Any
    scheme: typing.Optional[str]

    def __init__(
        self,
        *,
        host: typing.Optional[str] = ...,
        http_headers: typing.Optional[list[kubernetes.client.V1HTTPHeader]] = ...,
        path: typing.Optional[str] = ...,
        port: typing.Any,
        scheme: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1HTTPGetActionDict: ...

class V1HTTPGetActionDict(typing.TypedDict, total=False):
    host: str
    httpHeaders: list[kubernetes.client.V1HTTPHeaderDict]
    path: str
    port: typing.Any
    scheme: str
