import kubernetes.client
import typing

class V1alpha1Mutation:
    apply_configuration: typing.Optional[kubernetes.client.V1alpha1ApplyConfiguration]
    json_patch: typing.Optional[kubernetes.client.V1alpha1JSONPatch]
    patch_type: str

    def __init__(
        self,
        *,
        apply_configuration: typing.Optional[
            kubernetes.client.V1alpha1ApplyConfiguration
        ] = ...,
        json_patch: typing.Optional[kubernetes.client.V1alpha1JSONPatch] = ...,
        patch_type: str,
    ) -> None: ...
    def to_dict(self) -> V1alpha1MutationDict: ...

class V1alpha1MutationDict(typing.TypedDict, total=False):
    applyConfiguration: kubernetes.client.V1alpha1ApplyConfigurationDict
    jsonPatch: kubernetes.client.V1alpha1JSONPatchDict
    patchType: str
