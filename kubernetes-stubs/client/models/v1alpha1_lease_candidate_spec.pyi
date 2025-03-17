import datetime
import typing

class V1alpha1LeaseCandidateSpec:
    binary_version: typing.Optional[str]
    emulation_version: typing.Optional[str]
    lease_name: str
    ping_time: typing.Optional[datetime.datetime]
    preferred_strategies: list[str]
    renew_time: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        binary_version: typing.Optional[str] = ...,
        emulation_version: typing.Optional[str] = ...,
        lease_name: str,
        ping_time: typing.Optional[datetime.datetime] = ...,
        preferred_strategies: list[str],
        renew_time: typing.Optional[datetime.datetime] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha1LeaseCandidateSpecDict: ...

class V1alpha1LeaseCandidateSpecDict(typing.TypedDict, total=False):
    binaryVersion: str
    emulationVersion: str
    leaseName: str
    pingTime: datetime.datetime
    preferredStrategies: list[str]
    renewTime: datetime.datetime
