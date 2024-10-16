import kubernetes.client
import typing

class FlowcontrolV1Subject:
    group: typing.Optional[kubernetes.client.V1GroupSubject]
    kind: str
    service_account: typing.Optional[kubernetes.client.V1ServiceAccountSubject]
    user: typing.Optional[kubernetes.client.V1UserSubject]

    def __init__(
        self,
        *,
        group: typing.Optional[kubernetes.client.V1GroupSubject] = ...,
        kind: str,
        service_account: typing.Optional[
            kubernetes.client.V1ServiceAccountSubject
        ] = ...,
        user: typing.Optional[kubernetes.client.V1UserSubject] = ...,
    ) -> None: ...
    def to_dict(self) -> FlowcontrolV1SubjectDict: ...

class FlowcontrolV1SubjectDict(typing.TypedDict, total=False):
    group: kubernetes.client.V1GroupSubjectDict
    kind: str
    serviceAccount: kubernetes.client.V1ServiceAccountSubjectDict
    user: kubernetes.client.V1UserSubjectDict