import kubernetes.client
import typing

class V1PodDNSConfig:
    nameservers: typing.Optional[list[str]]
    options: typing.Optional[list[kubernetes.client.V1PodDNSConfigOption]]
    searches: typing.Optional[list[str]]

    def __init__(
        self,
        *,
        nameservers: typing.Optional[list[str]] = ...,
        options: typing.Optional[list[kubernetes.client.V1PodDNSConfigOption]] = ...,
        searches: typing.Optional[list[str]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1PodDNSConfigDict: ...

class V1PodDNSConfigDict(typing.TypedDict, total=False):
    nameservers: list[str]
    options: list[kubernetes.client.V1PodDNSConfigOptionDict]
    searches: list[str]
