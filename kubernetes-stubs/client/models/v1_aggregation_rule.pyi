import kubernetes.client
import typing

class V1AggregationRule:
    cluster_role_selectors: typing.Optional[list[kubernetes.client.V1LabelSelector]]

    def __init__(
        self,
        *,
        cluster_role_selectors: typing.Optional[
            list[kubernetes.client.V1LabelSelector]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1AggregationRuleDict: ...

class V1AggregationRuleDict(typing.TypedDict, total=False):
    clusterRoleSelectors: list[kubernetes.client.V1LabelSelectorDict]
