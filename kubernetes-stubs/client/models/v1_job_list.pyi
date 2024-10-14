import kubernetes.client
import typing

class V1JobList:
    api_version: str
    items: list[kubernetes.client.V1Job]
    kind: str
    metadata: kubernetes.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1Job],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1JobListDict: ...

class V1JobListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes.client.V1JobDict]
    kind: str
    metadata: kubernetes.client.V1ListMetaDict
