import typing

class V1beta1ParentReference:
    group: typing.Optional[str]
    name: str
    namespace: typing.Optional[str]
    resource: str

    def __init__(
        self,
        *,
        group: typing.Optional[str] = ...,
        name: str,
        namespace: typing.Optional[str] = ...,
        resource: str,
    ) -> None: ...
    def to_dict(self) -> V1beta1ParentReferenceDict: ...

class V1beta1ParentReferenceDict(typing.TypedDict, total=False):
    group: str
    name: str
    namespace: str
    resource: str
