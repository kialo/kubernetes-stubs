import kubernetes.client
import typing

class V1ContainerStatus:
    allocated_resources: typing.Optional[dict[str, str]]
    allocated_resources_status: typing.Optional[
        list[kubernetes.client.V1ResourceStatus]
    ]
    container_id: typing.Optional[str]
    image: str
    image_id: str
    last_state: typing.Optional[kubernetes.client.V1ContainerState]
    name: str
    ready: bool
    resources: typing.Optional[kubernetes.client.V1ResourceRequirements]
    restart_count: int
    started: typing.Optional[bool]
    state: typing.Optional[kubernetes.client.V1ContainerState]
    user: typing.Optional[kubernetes.client.V1ContainerUser]
    volume_mounts: typing.Optional[list[kubernetes.client.V1VolumeMountStatus]]

    def __init__(
        self,
        *,
        allocated_resources: typing.Optional[dict[str, str]] = ...,
        allocated_resources_status: typing.Optional[
            list[kubernetes.client.V1ResourceStatus]
        ] = ...,
        container_id: typing.Optional[str] = ...,
        image: str,
        image_id: str,
        last_state: typing.Optional[kubernetes.client.V1ContainerState] = ...,
        name: str,
        ready: bool,
        resources: typing.Optional[kubernetes.client.V1ResourceRequirements] = ...,
        restart_count: int,
        started: typing.Optional[bool] = ...,
        state: typing.Optional[kubernetes.client.V1ContainerState] = ...,
        user: typing.Optional[kubernetes.client.V1ContainerUser] = ...,
        volume_mounts: typing.Optional[
            list[kubernetes.client.V1VolumeMountStatus]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ContainerStatusDict: ...

class V1ContainerStatusDict(typing.TypedDict, total=False):
    allocatedResources: dict[str, str]
    allocatedResourcesStatus: list[kubernetes.client.V1ResourceStatusDict]
    containerID: str
    image: str
    imageID: str
    lastState: kubernetes.client.V1ContainerStateDict
    name: str
    ready: bool
    resources: kubernetes.client.V1ResourceRequirementsDict
    restartCount: int
    started: bool
    state: kubernetes.client.V1ContainerStateDict
    user: kubernetes.client.V1ContainerUserDict
    volumeMounts: list[kubernetes.client.V1VolumeMountStatusDict]
