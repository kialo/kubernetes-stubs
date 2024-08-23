from typing import List

from . import V1ListMeta, V1Pod

class V1PodList:
    @property
    def items(self) -> List[V1Pod]: ...
    @property
    def metadata(self) -> V1ListMeta: ...
