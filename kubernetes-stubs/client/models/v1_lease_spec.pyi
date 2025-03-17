import datetime
import typing

class V1LeaseSpec:
    acquire_time: typing.Optional[datetime.datetime]
    holder_identity: typing.Optional[str]
    lease_duration_seconds: typing.Optional[int]
    lease_transitions: typing.Optional[int]
    preferred_holder: typing.Optional[str]
    renew_time: typing.Optional[datetime.datetime]
    strategy: typing.Optional[str]

    def __init__(
        self,
        *,
        acquire_time: typing.Optional[datetime.datetime] = ...,
        holder_identity: typing.Optional[str] = ...,
        lease_duration_seconds: typing.Optional[int] = ...,
        lease_transitions: typing.Optional[int] = ...,
        preferred_holder: typing.Optional[str] = ...,
        renew_time: typing.Optional[datetime.datetime] = ...,
        strategy: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1LeaseSpecDict: ...

class V1LeaseSpecDict(typing.TypedDict, total=False):
    acquireTime: datetime.datetime
    holderIdentity: str
    leaseDurationSeconds: int
    leaseTransitions: int
    preferredHolder: str
    renewTime: datetime.datetime
    strategy: str
