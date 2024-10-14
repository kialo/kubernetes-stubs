import kubernetes.client
import typing

class V1ISCSIVolumeSource:
    chap_auth_discovery: typing.Optional[bool]
    chap_auth_session: typing.Optional[bool]
    fs_type: typing.Optional[str]
    initiator_name: typing.Optional[str]
    iqn: str
    iscsi_interface: typing.Optional[str]
    lun: int
    portals: typing.Optional[list[str]]
    read_only: typing.Optional[bool]
    secret_ref: typing.Optional[kubernetes.client.V1LocalObjectReference]
    target_portal: str

    def __init__(
        self,
        *,
        chap_auth_discovery: typing.Optional[bool] = ...,
        chap_auth_session: typing.Optional[bool] = ...,
        fs_type: typing.Optional[str] = ...,
        initiator_name: typing.Optional[str] = ...,
        iqn: str,
        iscsi_interface: typing.Optional[str] = ...,
        lun: int,
        portals: typing.Optional[list[str]] = ...,
        read_only: typing.Optional[bool] = ...,
        secret_ref: typing.Optional[kubernetes.client.V1LocalObjectReference] = ...,
        target_portal: str,
    ) -> None: ...
    def to_dict(self) -> V1ISCSIVolumeSourceDict: ...

class V1ISCSIVolumeSourceDict(typing.TypedDict, total=False):
    chapAuthDiscovery: bool
    chapAuthSession: bool
    fsType: str
    initiatorName: str
    iqn: str
    iscsiInterface: str
    lun: int
    portals: list[str]
    readOnly: bool
    secretRef: kubernetes.client.V1LocalObjectReferenceDict
    targetPortal: str
