from typing import List

from . import V1NodeAddress, V1NodeCondition, V1NodeSystemInfo

class V1NodeStatus:
    @property
    def addresses(self) -> List[V1NodeAddress]: ...
    @property
    def conditions(self) -> List[V1NodeCondition]: ...
    @property
    def node_info(self) -> V1NodeSystemInfo: ...
