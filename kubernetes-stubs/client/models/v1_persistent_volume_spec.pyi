from . import V1CSIPersistentVolumeSource

class V1PersistentVolumeSpec:
    @property
    def csi(self) -> V1CSIPersistentVolumeSource: ...
