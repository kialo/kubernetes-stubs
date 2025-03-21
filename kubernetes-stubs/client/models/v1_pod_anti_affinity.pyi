import kubernetes.client
import typing

class V1PodAntiAffinity:
    preferred_during_scheduling_ignored_during_execution: typing.Optional[
        list[kubernetes.client.V1WeightedPodAffinityTerm]
    ]
    required_during_scheduling_ignored_during_execution: typing.Optional[
        list[kubernetes.client.V1PodAffinityTerm]
    ]

    def __init__(
        self,
        *,
        preferred_during_scheduling_ignored_during_execution: typing.Optional[
            list[kubernetes.client.V1WeightedPodAffinityTerm]
        ] = ...,
        required_during_scheduling_ignored_during_execution: typing.Optional[
            list[kubernetes.client.V1PodAffinityTerm]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1PodAntiAffinityDict: ...

class V1PodAntiAffinityDict(typing.TypedDict, total=False):
    preferredDuringSchedulingIgnoredDuringExecution: list[
        kubernetes.client.V1WeightedPodAffinityTermDict
    ]
    requiredDuringSchedulingIgnoredDuringExecution: list[
        kubernetes.client.V1PodAffinityTermDict
    ]
