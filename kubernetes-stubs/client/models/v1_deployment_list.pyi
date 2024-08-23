from typing import List

from .v1_deployment import V1Deployment

class V1DeploymentList:
    @property
    def items(self) -> List[V1Deployment]: ...
