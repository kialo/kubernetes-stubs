from typing import List

from . import V1PersistentVolumeClaim

class V1PersistentVolumeClaimList:
    @property
    def items(self) -> List[V1PersistentVolumeClaim]: ...
