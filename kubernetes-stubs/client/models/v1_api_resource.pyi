import typing

class V1APIResource:
    categories: typing.Optional[list[str]]
    group: typing.Optional[str]
    kind: str
    name: str
    namespaced: bool
    short_names: typing.Optional[list[str]]
    singular_name: str
    storage_version_hash: typing.Optional[str]
    verbs: list[str]
    version: typing.Optional[str]

    def __init__(
        self,
        *,
        categories: typing.Optional[list[str]] = ...,
        group: typing.Optional[str] = ...,
        kind: str,
        name: str,
        namespaced: bool,
        short_names: typing.Optional[list[str]] = ...,
        singular_name: str,
        storage_version_hash: typing.Optional[str] = ...,
        verbs: list[str],
        version: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1APIResourceDict: ...

class V1APIResourceDict(typing.TypedDict, total=False):
    categories: list[str]
    group: str
    kind: str
    name: str
    namespaced: bool
    shortNames: list[str]
    singularName: str
    storageVersionHash: str
    verbs: list[str]
    version: str
