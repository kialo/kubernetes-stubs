import kubernetes.client
import typing

class V1EnvVarSource:
    config_map_key_ref: typing.Optional[kubernetes.client.V1ConfigMapKeySelector]
    field_ref: typing.Optional[kubernetes.client.V1ObjectFieldSelector]
    resource_field_ref: typing.Optional[kubernetes.client.V1ResourceFieldSelector]
    secret_key_ref: typing.Optional[kubernetes.client.V1SecretKeySelector]

    def __init__(
        self,
        *,
        config_map_key_ref: typing.Optional[
            kubernetes.client.V1ConfigMapKeySelector
        ] = ...,
        field_ref: typing.Optional[kubernetes.client.V1ObjectFieldSelector] = ...,
        resource_field_ref: typing.Optional[
            kubernetes.client.V1ResourceFieldSelector
        ] = ...,
        secret_key_ref: typing.Optional[kubernetes.client.V1SecretKeySelector] = ...,
    ) -> None: ...
    def to_dict(self) -> V1EnvVarSourceDict: ...

class V1EnvVarSourceDict(typing.TypedDict, total=False):
    configMapKeyRef: kubernetes.client.V1ConfigMapKeySelectorDict
    fieldRef: kubernetes.client.V1ObjectFieldSelectorDict
    resourceFieldRef: kubernetes.client.V1ResourceFieldSelectorDict
    secretKeyRef: kubernetes.client.V1SecretKeySelectorDict
