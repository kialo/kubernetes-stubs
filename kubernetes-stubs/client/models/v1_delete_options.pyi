import kubernetes.client
import typing

class V1DeleteOptions:
    api_version: str
    dry_run: typing.Optional[list[str]]
    grace_period_seconds: typing.Optional[int]
    ignore_store_read_error_with_cluster_breaking_potential: typing.Optional[bool]
    kind: str
    orphan_dependents: typing.Optional[bool]
    preconditions: typing.Optional[kubernetes.client.V1Preconditions]
    propagation_policy: typing.Optional[str]

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        dry_run: typing.Optional[list[str]] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        ignore_store_read_error_with_cluster_breaking_potential: typing.Optional[
            bool
        ] = ...,
        kind: typing.Optional[str] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        preconditions: typing.Optional[kubernetes.client.V1Preconditions] = ...,
        propagation_policy: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1DeleteOptionsDict: ...

class V1DeleteOptionsDict(typing.TypedDict, total=False):
    apiVersion: str
    dryRun: list[str]
    gracePeriodSeconds: int
    ignoreStoreReadErrorWithClusterBreakingPotential: bool
    kind: str
    orphanDependents: bool
    preconditions: kubernetes.client.V1PreconditionsDict
    propagationPolicy: str
