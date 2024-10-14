import kubernetes.client
import typing

class V1alpha2AllocationResult:
    available_on_nodes: typing.Optional[kubernetes.client.V1NodeSelector]
    resource_handles: typing.Optional[list[kubernetes.client.V1alpha2ResourceHandle]]
    shareable: typing.Optional[bool]

    def __init__(
        self,
        *,
        available_on_nodes: typing.Optional[kubernetes.client.V1NodeSelector] = ...,
        resource_handles: typing.Optional[
            list[kubernetes.client.V1alpha2ResourceHandle]
        ] = ...,
        shareable: typing.Optional[bool] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha2AllocationResultDict: ...

class V1alpha2AllocationResultDict(typing.TypedDict, total=False):
    availableOnNodes: kubernetes.client.V1NodeSelectorDict
    resourceHandles: list[kubernetes.client.V1alpha2ResourceHandleDict]
    shareable: bool
