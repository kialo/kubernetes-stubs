import datetime
import typing

class V1beta1LeaseCandidateSpec:
    binary_version: str
    emulation_version: typing.Optional[str]
    lease_name: str
    ping_time: typing.Optional[datetime.datetime]
    renew_time: typing.Optional[datetime.datetime]
    strategy: str

    def __init__(
        self,
        *,
        binary_version: str,
        emulation_version: typing.Optional[str] = ...,
        lease_name: str,
        ping_time: typing.Optional[datetime.datetime] = ...,
        renew_time: typing.Optional[datetime.datetime] = ...,
        strategy: str,
    ) -> None: ...
    def to_dict(self) -> V1beta1LeaseCandidateSpecDict: ...

class V1beta1LeaseCandidateSpecDict(typing.TypedDict, total=False):
    binaryVersion: str
    emulationVersion: str
    leaseName: str
    pingTime: datetime.datetime
    renewTime: datetime.datetime
    strategy: str
