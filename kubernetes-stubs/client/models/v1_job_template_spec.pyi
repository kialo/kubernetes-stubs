from . import V1JobSpec

class V1JobTemplateSpec:
    @property
    def spec(self) -> V1JobSpec: ...
