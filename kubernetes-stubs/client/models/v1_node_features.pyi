import typing

class V1NodeFeatures:
    supplemental_groups_policy: typing.Optional[bool]

    def __init__(
        self, *, supplemental_groups_policy: typing.Optional[bool] = ...
    ) -> None: ...
    def to_dict(self) -> V1NodeFeaturesDict: ...

class V1NodeFeaturesDict(typing.TypedDict, total=False):
    supplementalGroupsPolicy: bool
