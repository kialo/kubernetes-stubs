from . import V1CronJobSpec, V1ObjectMeta

class V1CronJob:
    @property
    def metadata(self) -> V1ObjectMeta: ...
    @property
    def spec(self) -> V1CronJobSpec: ...
