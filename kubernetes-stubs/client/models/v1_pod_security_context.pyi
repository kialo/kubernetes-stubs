import kubernetes.client
import typing

class V1PodSecurityContext:
    app_armor_profile: typing.Optional[kubernetes.client.V1AppArmorProfile]
    fs_group: typing.Optional[int]
    fs_group_change_policy: typing.Optional[str]
    run_as_group: typing.Optional[int]
    run_as_non_root: typing.Optional[bool]
    run_as_user: typing.Optional[int]
    se_linux_options: typing.Optional[kubernetes.client.V1SELinuxOptions]
    seccomp_profile: typing.Optional[kubernetes.client.V1SeccompProfile]
    supplemental_groups: typing.Optional[list[int]]
    supplemental_groups_policy: typing.Optional[str]
    sysctls: typing.Optional[list[kubernetes.client.V1Sysctl]]
    windows_options: typing.Optional[kubernetes.client.V1WindowsSecurityContextOptions]

    def __init__(
        self,
        *,
        app_armor_profile: typing.Optional[kubernetes.client.V1AppArmorProfile] = ...,
        fs_group: typing.Optional[int] = ...,
        fs_group_change_policy: typing.Optional[str] = ...,
        run_as_group: typing.Optional[int] = ...,
        run_as_non_root: typing.Optional[bool] = ...,
        run_as_user: typing.Optional[int] = ...,
        se_linux_options: typing.Optional[kubernetes.client.V1SELinuxOptions] = ...,
        seccomp_profile: typing.Optional[kubernetes.client.V1SeccompProfile] = ...,
        supplemental_groups: typing.Optional[list[int]] = ...,
        supplemental_groups_policy: typing.Optional[str] = ...,
        sysctls: typing.Optional[list[kubernetes.client.V1Sysctl]] = ...,
        windows_options: typing.Optional[
            kubernetes.client.V1WindowsSecurityContextOptions
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1PodSecurityContextDict: ...

class V1PodSecurityContextDict(typing.TypedDict, total=False):
    appArmorProfile: kubernetes.client.V1AppArmorProfileDict
    fsGroup: int
    fsGroupChangePolicy: str
    runAsGroup: int
    runAsNonRoot: bool
    runAsUser: int
    seLinuxOptions: kubernetes.client.V1SELinuxOptionsDict
    seccompProfile: kubernetes.client.V1SeccompProfileDict
    supplementalGroups: list[int]
    supplementalGroupsPolicy: str
    sysctls: list[kubernetes.client.V1SysctlDict]
    windowsOptions: kubernetes.client.V1WindowsSecurityContextOptionsDict
