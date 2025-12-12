import kubernetes.client
import typing

class V1CSIDriverSpec:
    attach_required: typing.Optional[bool]
    fs_group_policy: typing.Optional[str]
    node_allocatable_update_period_seconds: typing.Optional[int]
    pod_info_on_mount: typing.Optional[bool]
    requires_republish: typing.Optional[bool]
    se_linux_mount: typing.Optional[bool]
    storage_capacity: typing.Optional[bool]
    token_requests: typing.Optional[list[kubernetes.client.StorageV1TokenRequest]]
    volume_lifecycle_modes: typing.Optional[list[str]]

    def __init__(
        self,
        *,
        attach_required: typing.Optional[bool] = ...,
        fs_group_policy: typing.Optional[str] = ...,
        node_allocatable_update_period_seconds: typing.Optional[int] = ...,
        pod_info_on_mount: typing.Optional[bool] = ...,
        requires_republish: typing.Optional[bool] = ...,
        se_linux_mount: typing.Optional[bool] = ...,
        storage_capacity: typing.Optional[bool] = ...,
        token_requests: typing.Optional[
            list[kubernetes.client.StorageV1TokenRequest]
        ] = ...,
        volume_lifecycle_modes: typing.Optional[list[str]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1CSIDriverSpecDict: ...

class V1CSIDriverSpecDict(typing.TypedDict, total=False):
    attachRequired: bool
    fsGroupPolicy: str
    nodeAllocatableUpdatePeriodSeconds: int
    podInfoOnMount: bool
    requiresRepublish: bool
    seLinuxMount: bool
    storageCapacity: bool
    tokenRequests: list[kubernetes.client.StorageV1TokenRequestDict]
    volumeLifecycleModes: list[str]
