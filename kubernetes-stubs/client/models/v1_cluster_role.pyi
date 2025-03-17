import kubernetes.client
import typing

class V1ClusterRole:
    aggregation_rule: typing.Optional[kubernetes.client.V1AggregationRule]
    api_version: str
    kind: str
    metadata: kubernetes.client.V1ObjectMeta
    rules: typing.Optional[list[kubernetes.client.V1PolicyRule]]

    def __init__(
        self,
        *,
        aggregation_rule: typing.Optional[kubernetes.client.V1AggregationRule] = ...,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        rules: typing.Optional[list[kubernetes.client.V1PolicyRule]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ClusterRoleDict: ...

class V1ClusterRoleDict(typing.TypedDict, total=False):
    aggregationRule: kubernetes.client.V1AggregationRuleDict
    apiVersion: str
    kind: str
    metadata: kubernetes.client.V1ObjectMetaDict
    rules: list[kubernetes.client.V1PolicyRuleDict]
