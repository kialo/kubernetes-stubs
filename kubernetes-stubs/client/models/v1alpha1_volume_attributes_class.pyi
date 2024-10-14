import kubernetes.client
import typing

class V1alpha1VolumeAttributesClass:
    api_version: str
    driver_name: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    parameters: typing.Optional[dict[str, str]]

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        driver_name: str,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        parameters: typing.Optional[dict[str, str]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha1VolumeAttributesClassDict: ...

class V1alpha1VolumeAttributesClassDict(typing.TypedDict, total=False):
    apiVersion: str
    driverName: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    parameters: dict[str, str]
