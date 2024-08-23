from .v1_deployment_spec import V1DeploymentSpec
from .v1_object_meta import V1ObjectMeta

class V1Deployment:
    @property
    def metadata(self) -> V1ObjectMeta: ...
    @property
    def spec(self) -> V1DeploymentSpec: ...
