import typing

class V1AzureFilePersistentVolumeSource:
    read_only: typing.Optional[bool]
    secret_name: str
    secret_namespace: typing.Optional[str]
    share_name: str

    def __init__(
        self,
        *,
        read_only: typing.Optional[bool] = ...,
        secret_name: str,
        secret_namespace: typing.Optional[str] = ...,
        share_name: str,
    ) -> None: ...
    def to_dict(self) -> V1AzureFilePersistentVolumeSourceDict: ...

class V1AzureFilePersistentVolumeSourceDict(typing.TypedDict, total=False):
    readOnly: bool
    secretName: str
    secretNamespace: str
    shareName: str
