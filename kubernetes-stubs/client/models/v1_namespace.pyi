from .v1_object_meta import V1ObjectMeta

class V1Namespace:
    @property
    def metadata(self) -> V1ObjectMeta: ...
