import kubernetes.client
import typing

class V1beta3PriorityLevelConfiguration:
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    spec: kubernetes.client.V1beta3PriorityLevelConfigurationSpec
    status: kubernetes.client.V1beta3PriorityLevelConfigurationStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[
            kubernetes.client.V1beta3PriorityLevelConfigurationSpec
        ] = ...,
        status: typing.Optional[
            kubernetes.client.V1beta3PriorityLevelConfigurationStatus
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta3PriorityLevelConfigurationDict: ...

class V1beta3PriorityLevelConfigurationDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    spec: kubernetes.client.V1beta3PriorityLevelConfigurationSpecDict
    status: kubernetes.client.V1beta3PriorityLevelConfigurationStatusDict
