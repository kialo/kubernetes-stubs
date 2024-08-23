from typing import List

from .v1_secret import V1Secret

class V1SecretList:
    @property
    def items(self) -> List[V1Secret]: ...
