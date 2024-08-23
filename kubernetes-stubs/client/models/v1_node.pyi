from . import V1NodeSpec, V1NodeStatus, V1ObjectMeta

class V1Node:
    @property
    def metadata(self) -> V1ObjectMeta: ...
    @property
    def spec(self) -> V1NodeSpec: ...
    @property
    def status(self) -> V1NodeStatus: ...