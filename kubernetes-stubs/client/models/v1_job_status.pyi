from . import V1JobCondition

class V1JobStatus:
    @property
    def conditions(self) -> list[V1JobCondition]: ...
