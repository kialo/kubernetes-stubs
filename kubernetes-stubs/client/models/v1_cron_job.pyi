import kubernetes.client
import typing

class V1CronJob:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    spec: kubernetes.client.V1CronJobSpec
    status: kubernetes.client.V1CronJobStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1CronJobSpec] = ...,
        status: typing.Optional[kubernetes.client.V1CronJobStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> V1CronJobDict: ...

class V1CronJobDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    spec: kubernetes.client.V1CronJobSpecDict
    status: kubernetes.client.V1CronJobStatusDict
