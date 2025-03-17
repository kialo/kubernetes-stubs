import kubernetes.client
import typing

class V1Volume:
    aws_elastic_block_store: typing.Optional[
        kubernetes.client.V1AWSElasticBlockStoreVolumeSource
    ]
    azure_disk: typing.Optional[kubernetes.client.V1AzureDiskVolumeSource]
    azure_file: typing.Optional[kubernetes.client.V1AzureFileVolumeSource]
    cephfs: typing.Optional[kubernetes.client.V1CephFSVolumeSource]
    cinder: typing.Optional[kubernetes.client.V1CinderVolumeSource]
    config_map: typing.Optional[kubernetes.client.V1ConfigMapVolumeSource]
    csi: typing.Optional[kubernetes.client.V1CSIVolumeSource]
    downward_api: typing.Optional[kubernetes.client.V1DownwardAPIVolumeSource]
    empty_dir: typing.Optional[kubernetes.client.V1EmptyDirVolumeSource]
    ephemeral: typing.Optional[kubernetes.client.V1EphemeralVolumeSource]
    fc: typing.Optional[kubernetes.client.V1FCVolumeSource]
    flex_volume: typing.Optional[kubernetes.client.V1FlexVolumeSource]
    flocker: typing.Optional[kubernetes.client.V1FlockerVolumeSource]
    gce_persistent_disk: typing.Optional[
        kubernetes.client.V1GCEPersistentDiskVolumeSource
    ]
    git_repo: typing.Optional[kubernetes.client.V1GitRepoVolumeSource]
    glusterfs: typing.Optional[kubernetes.client.V1GlusterfsVolumeSource]
    host_path: typing.Optional[kubernetes.client.V1HostPathVolumeSource]
    image: typing.Optional[kubernetes.client.V1ImageVolumeSource]
    iscsi: typing.Optional[kubernetes.client.V1ISCSIVolumeSource]
    name: str
    nfs: typing.Optional[kubernetes.client.V1NFSVolumeSource]
    persistent_volume_claim: typing.Optional[
        kubernetes.client.V1PersistentVolumeClaimVolumeSource
    ]
    photon_persistent_disk: typing.Optional[
        kubernetes.client.V1PhotonPersistentDiskVolumeSource
    ]
    portworx_volume: typing.Optional[kubernetes.client.V1PortworxVolumeSource]
    projected: typing.Optional[kubernetes.client.V1ProjectedVolumeSource]
    quobyte: typing.Optional[kubernetes.client.V1QuobyteVolumeSource]
    rbd: typing.Optional[kubernetes.client.V1RBDVolumeSource]
    scale_io: typing.Optional[kubernetes.client.V1ScaleIOVolumeSource]
    secret: typing.Optional[kubernetes.client.V1SecretVolumeSource]
    storageos: typing.Optional[kubernetes.client.V1StorageOSVolumeSource]
    vsphere_volume: typing.Optional[kubernetes.client.V1VsphereVirtualDiskVolumeSource]

    def __init__(
        self,
        *,
        aws_elastic_block_store: typing.Optional[
            kubernetes.client.V1AWSElasticBlockStoreVolumeSource
        ] = ...,
        azure_disk: typing.Optional[kubernetes.client.V1AzureDiskVolumeSource] = ...,
        azure_file: typing.Optional[kubernetes.client.V1AzureFileVolumeSource] = ...,
        cephfs: typing.Optional[kubernetes.client.V1CephFSVolumeSource] = ...,
        cinder: typing.Optional[kubernetes.client.V1CinderVolumeSource] = ...,
        config_map: typing.Optional[kubernetes.client.V1ConfigMapVolumeSource] = ...,
        csi: typing.Optional[kubernetes.client.V1CSIVolumeSource] = ...,
        downward_api: typing.Optional[
            kubernetes.client.V1DownwardAPIVolumeSource
        ] = ...,
        empty_dir: typing.Optional[kubernetes.client.V1EmptyDirVolumeSource] = ...,
        ephemeral: typing.Optional[kubernetes.client.V1EphemeralVolumeSource] = ...,
        fc: typing.Optional[kubernetes.client.V1FCVolumeSource] = ...,
        flex_volume: typing.Optional[kubernetes.client.V1FlexVolumeSource] = ...,
        flocker: typing.Optional[kubernetes.client.V1FlockerVolumeSource] = ...,
        gce_persistent_disk: typing.Optional[
            kubernetes.client.V1GCEPersistentDiskVolumeSource
        ] = ...,
        git_repo: typing.Optional[kubernetes.client.V1GitRepoVolumeSource] = ...,
        glusterfs: typing.Optional[kubernetes.client.V1GlusterfsVolumeSource] = ...,
        host_path: typing.Optional[kubernetes.client.V1HostPathVolumeSource] = ...,
        image: typing.Optional[kubernetes.client.V1ImageVolumeSource] = ...,
        iscsi: typing.Optional[kubernetes.client.V1ISCSIVolumeSource] = ...,
        name: str,
        nfs: typing.Optional[kubernetes.client.V1NFSVolumeSource] = ...,
        persistent_volume_claim: typing.Optional[
            kubernetes.client.V1PersistentVolumeClaimVolumeSource
        ] = ...,
        photon_persistent_disk: typing.Optional[
            kubernetes.client.V1PhotonPersistentDiskVolumeSource
        ] = ...,
        portworx_volume: typing.Optional[
            kubernetes.client.V1PortworxVolumeSource
        ] = ...,
        projected: typing.Optional[kubernetes.client.V1ProjectedVolumeSource] = ...,
        quobyte: typing.Optional[kubernetes.client.V1QuobyteVolumeSource] = ...,
        rbd: typing.Optional[kubernetes.client.V1RBDVolumeSource] = ...,
        scale_io: typing.Optional[kubernetes.client.V1ScaleIOVolumeSource] = ...,
        secret: typing.Optional[kubernetes.client.V1SecretVolumeSource] = ...,
        storageos: typing.Optional[kubernetes.client.V1StorageOSVolumeSource] = ...,
        vsphere_volume: typing.Optional[
            kubernetes.client.V1VsphereVirtualDiskVolumeSource
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1VolumeDict: ...

class V1VolumeDict(typing.TypedDict, total=False):
    awsElasticBlockStore: kubernetes.client.V1AWSElasticBlockStoreVolumeSourceDict
    azureDisk: kubernetes.client.V1AzureDiskVolumeSourceDict
    azureFile: kubernetes.client.V1AzureFileVolumeSourceDict
    cephfs: kubernetes.client.V1CephFSVolumeSourceDict
    cinder: kubernetes.client.V1CinderVolumeSourceDict
    configMap: kubernetes.client.V1ConfigMapVolumeSourceDict
    csi: kubernetes.client.V1CSIVolumeSourceDict
    downwardAPI: kubernetes.client.V1DownwardAPIVolumeSourceDict
    emptyDir: kubernetes.client.V1EmptyDirVolumeSourceDict
    ephemeral: kubernetes.client.V1EphemeralVolumeSourceDict
    fc: kubernetes.client.V1FCVolumeSourceDict
    flexVolume: kubernetes.client.V1FlexVolumeSourceDict
    flocker: kubernetes.client.V1FlockerVolumeSourceDict
    gcePersistentDisk: kubernetes.client.V1GCEPersistentDiskVolumeSourceDict
    gitRepo: kubernetes.client.V1GitRepoVolumeSourceDict
    glusterfs: kubernetes.client.V1GlusterfsVolumeSourceDict
    hostPath: kubernetes.client.V1HostPathVolumeSourceDict
    image: kubernetes.client.V1ImageVolumeSourceDict
    iscsi: kubernetes.client.V1ISCSIVolumeSourceDict
    name: str
    nfs: kubernetes.client.V1NFSVolumeSourceDict
    persistentVolumeClaim: kubernetes.client.V1PersistentVolumeClaimVolumeSourceDict
    photonPersistentDisk: kubernetes.client.V1PhotonPersistentDiskVolumeSourceDict
    portworxVolume: kubernetes.client.V1PortworxVolumeSourceDict
    projected: kubernetes.client.V1ProjectedVolumeSourceDict
    quobyte: kubernetes.client.V1QuobyteVolumeSourceDict
    rbd: kubernetes.client.V1RBDVolumeSourceDict
    scaleIO: kubernetes.client.V1ScaleIOVolumeSourceDict
    secret: kubernetes.client.V1SecretVolumeSourceDict
    storageos: kubernetes.client.V1StorageOSVolumeSourceDict
    vsphereVolume: kubernetes.client.V1VsphereVirtualDiskVolumeSourceDict
