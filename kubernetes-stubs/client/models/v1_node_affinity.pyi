import kubernetes.client
import typing

class V1NodeAffinity:
    preferred_during_scheduling_ignored_during_execution: typing.Optional[
        list[kubernetes.client.V1PreferredSchedulingTerm]
    ]
    required_during_scheduling_ignored_during_execution: typing.Optional[
        kubernetes.client.V1NodeSelector
    ]

    def __init__(
        self,
        *,
        preferred_during_scheduling_ignored_during_execution: typing.Optional[
            list[kubernetes.client.V1PreferredSchedulingTerm]
        ] = ...,
        required_during_scheduling_ignored_during_execution: typing.Optional[
            kubernetes.client.V1NodeSelector
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1NodeAffinityDict: ...

class V1NodeAffinityDict(typing.TypedDict, total=False):
    preferredDuringSchedulingIgnoredDuringExecution: list[
        kubernetes.client.V1PreferredSchedulingTermDict
    ]
    requiredDuringSchedulingIgnoredDuringExecution: kubernetes.client.V1NodeSelectorDict
