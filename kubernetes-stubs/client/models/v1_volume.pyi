from .v1_persistent_volume_claim_volume_source import V1PersistentVolumeClaimVolumeSource

class V1Volume:
    @property
    def persistent_volume_claim(self) -> V1PersistentVolumeClaimVolumeSource: ...
