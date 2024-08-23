from . import V1ObjectMeta, V1PodSpec, V1PodStatus

class V1Pod:
    @property
    def metadata(self) -> V1ObjectMeta: ...
    @property
    def status(self) -> V1PodStatus: ...
    @property
    def spec(self) -> V1PodSpec: ...