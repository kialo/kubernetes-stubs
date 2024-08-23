from .. import V1ContainerState

class V1ContainerStatus:
    @property
    def ready(self) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def state(self) -> V1ContainerState: ...