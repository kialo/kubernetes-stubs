import kubernetes.client
import typing

class V1EphemeralVolumeSource:
    volume_claim_template: typing.Optional[
        kubernetes.client.V1PersistentVolumeClaimTemplate
    ]

    def __init__(
        self,
        *,
        volume_claim_template: typing.Optional[
            kubernetes.client.V1PersistentVolumeClaimTemplate
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1EphemeralVolumeSourceDict: ...

class V1EphemeralVolumeSourceDict(typing.TypedDict, total=False):
    volumeClaimTemplate: kubernetes.client.V1PersistentVolumeClaimTemplateDict
