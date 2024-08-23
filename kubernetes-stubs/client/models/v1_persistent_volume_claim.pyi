from . import V1ObjectMeta

class V1PersistentVolumeClaim:
    @property
    def metadata(self) -> V1ObjectMeta: ...
