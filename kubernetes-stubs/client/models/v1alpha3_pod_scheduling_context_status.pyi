import kubernetes.client
import typing

class V1alpha3PodSchedulingContextStatus:
    resource_claims: typing.Optional[
        list[kubernetes.client.V1alpha3ResourceClaimSchedulingStatus]
    ]

    def __init__(
        self,
        *,
        resource_claims: typing.Optional[
            list[kubernetes.client.V1alpha3ResourceClaimSchedulingStatus]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha3PodSchedulingContextStatusDict: ...

class V1alpha3PodSchedulingContextStatusDict(typing.TypedDict, total=False):
    resourceClaims: list[kubernetes.client.V1alpha3ResourceClaimSchedulingStatusDict]
