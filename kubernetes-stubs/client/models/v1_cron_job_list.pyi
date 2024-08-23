from . import V1CronJob, V1ListMeta

class V1CronJobList:
    @property
    def items(self) -> list[V1CronJob]: ...
    @property
    def metadata(self) -> V1ListMeta: ...
