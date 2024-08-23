from typing import List

from . import V1PersistentVolume

class V1PersistentVolumeList:
    @property
    def items(self) -> List[V1PersistentVolume]: ...
