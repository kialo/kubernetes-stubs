from . import V1JobTemplateSpec

class V1CronJobSpec:
    @property
    def job_template(self) -> V1JobTemplateSpec: ...
