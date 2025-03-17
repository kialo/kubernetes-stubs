import kubernetes.client
import typing

class V1ResourceAttributes:
    field_selector: typing.Optional[kubernetes.client.V1FieldSelectorAttributes]
    group: typing.Optional[str]
    label_selector: typing.Optional[kubernetes.client.V1LabelSelectorAttributes]
    name: typing.Optional[str]
    namespace: typing.Optional[str]
    resource: typing.Optional[str]
    subresource: typing.Optional[str]
    verb: typing.Optional[str]
    version: typing.Optional[str]

    def __init__(
        self,
        *,
        field_selector: typing.Optional[
            kubernetes.client.V1FieldSelectorAttributes
        ] = ...,
        group: typing.Optional[str] = ...,
        label_selector: typing.Optional[
            kubernetes.client.V1LabelSelectorAttributes
        ] = ...,
        name: typing.Optional[str] = ...,
        namespace: typing.Optional[str] = ...,
        resource: typing.Optional[str] = ...,
        subresource: typing.Optional[str] = ...,
        verb: typing.Optional[str] = ...,
        version: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ResourceAttributesDict: ...

class V1ResourceAttributesDict(typing.TypedDict, total=False):
    fieldSelector: kubernetes.client.V1FieldSelectorAttributesDict
    group: str
    labelSelector: kubernetes.client.V1LabelSelectorAttributesDict
    name: str
    namespace: str
    resource: str
    subresource: str
    verb: str
    version: str
