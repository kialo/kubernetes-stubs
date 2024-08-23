from . import V1PodTemplateSpec

class V1JobSpec:
    @property
    def template(self) -> V1PodTemplateSpec: ...
    @property
    def active_deadline_seconds(self) -> int: ...
