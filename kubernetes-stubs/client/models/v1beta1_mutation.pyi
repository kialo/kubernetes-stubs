import kubernetes.client
import typing

class V1beta1Mutation:
    apply_configuration: typing.Optional[kubernetes.client.V1beta1ApplyConfiguration]
    json_patch: typing.Optional[kubernetes.client.V1beta1JSONPatch]
    patch_type: str

    def __init__(
        self,
        *,
        apply_configuration: typing.Optional[
            kubernetes.client.V1beta1ApplyConfiguration
        ] = ...,
        json_patch: typing.Optional[kubernetes.client.V1beta1JSONPatch] = ...,
        patch_type: str,
    ) -> None: ...
    def to_dict(self) -> V1beta1MutationDict: ...

class V1beta1MutationDict(typing.TypedDict, total=False):
    applyConfiguration: kubernetes.client.V1beta1ApplyConfigurationDict
    jsonPatch: kubernetes.client.V1beta1JSONPatchDict
    patchType: str
