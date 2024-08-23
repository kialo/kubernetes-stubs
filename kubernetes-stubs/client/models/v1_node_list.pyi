from typing import List

from . import V1ListMeta, V1Node

class V1NodeList:
    @property
    def items(self) -> List[V1Node]: ...
    @property
    def metadata(self) -> V1ListMeta: ...
