from typing import List

from .v1_namespace import V1Namespace

class V1NamespaceList:
    @property
    def items(self) -> List[V1Namespace]: ...
