from typing import List

from .v1_container import V1Container as V1Container
from .v1_volume import V1Volume as V1Volume

class V1PodSpec:
    @property
    def init_containers(self) -> List[V1Container]: ...
    @property
    def containers(self) -> List[V1Container]: ...
    @property
    def ephemeral_containers(self) -> List[V1Container]: ...
    @property
    def volumes(self) -> List[V1Volume]: ...
