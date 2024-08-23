from . import V1PodSpec

class V1PodTemplateSpec:
    @property
    def spec(self) -> V1PodSpec: ...
