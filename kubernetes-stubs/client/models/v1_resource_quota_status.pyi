import typing

class V1ResourceQuotaStatus:
    hard: typing.Optional[dict[str, str]]
    used: typing.Optional[dict[str, str]]

    def __init__(
        self,
        *,
        hard: typing.Optional[dict[str, str]] = ...,
        used: typing.Optional[dict[str, str]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ResourceQuotaStatusDict: ...

class V1ResourceQuotaStatusDict(typing.TypedDict, total=False):
    hard: dict[str, str]
    used: dict[str, str]
