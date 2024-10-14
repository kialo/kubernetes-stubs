import kubernetes.client
import typing

class V1PersistentVolumeSpec:
    access_modes: typing.Optional[list[str]]
    aws_elastic_block_store: typing.Optional[
        kubernetes.client.V1AWSElasticBlockStoreVolumeSource
    ]
    azure_disk: typing.Optional[kubernetes.client.V1AzureDiskVolumeSource]
    azure_file: typing.Optional[kubernetes.client.V1AzureFilePersistentVolumeSource]
    capacity: typing.Optional[dict[str, str]]
    cephfs: typing.Optional[kubernetes.client.V1CephFSPersistentVolumeSource]
    cinder: typing.Optional[kubernetes.client.V1CinderPersistentVolumeSource]
    claim_ref: typing.Optional[kubernetes.client.V1ObjectReference]
    csi: typing.Optional[kubernetes.client.V1CSIPersistentVolumeSource]
    fc: typing.Optional[kubernetes.client.V1FCVolumeSource]
    flex_volume: typing.Optional[kubernetes.client.V1FlexPersistentVolumeSource]
    flocker: typing.Optional[kubernetes.client.V1FlockerVolumeSource]
    gce_persistent_disk: typing.Optional[
        kubernetes.client.V1GCEPersistentDiskVolumeSource
    ]
    glusterfs: typing.Optional[kubernetes.client.V1GlusterfsPersistentVolumeSource]
    host_path: typing.Optional[kubernetes.client.V1HostPathVolumeSource]
    iscsi: typing.Optional[kubernetes.client.V1ISCSIPersistentVolumeSource]
    local: typing.Optional[kubernetes.client.V1LocalVolumeSource]
    mount_options: typing.Optional[list[str]]
    nfs: typing.Optional[kubernetes.client.V1NFSVolumeSource]
    node_affinity: typing.Optional[kubernetes.client.V1VolumeNodeAffinity]
    persistent_volume_reclaim_policy: typing.Optional[str]
    photon_persistent_disk: typing.Optional[
        kubernetes.client.V1PhotonPersistentDiskVolumeSource
    ]
    portworx_volume: typing.Optional[kubernetes.client.V1PortworxVolumeSource]
    quobyte: typing.Optional[kubernetes.client.V1QuobyteVolumeSource]
    rbd: typing.Optional[kubernetes.client.V1RBDPersistentVolumeSource]
    scale_io: typing.Optional[kubernetes.client.V1ScaleIOPersistentVolumeSource]
    storage_class_name: typing.Optional[str]
    storageos: typing.Optional[kubernetes.client.V1StorageOSPersistentVolumeSource]
    volume_attributes_class_name: typing.Optional[str]
    volume_mode: typing.Optional[str]
    vsphere_volume: typing.Optional[kubernetes.client.V1VsphereVirtualDiskVolumeSource]

    def __init__(
        self,
        *,
        access_modes: typing.Optional[list[str]] = ...,
        aws_elastic_block_store: typing.Optional[
            kubernetes.client.V1AWSElasticBlockStoreVolumeSource
        ] = ...,
        azure_disk: typing.Optional[kubernetes.client.V1AzureDiskVolumeSource] = ...,
        azure_file: typing.Optional[
            kubernetes.client.V1AzureFilePersistentVolumeSource
        ] = ...,
        capacity: typing.Optional[dict[str, str]] = ...,
        cephfs: typing.Optional[kubernetes.client.V1CephFSPersistentVolumeSource] = ...,
        cinder: typing.Optional[kubernetes.client.V1CinderPersistentVolumeSource] = ...,
        claim_ref: typing.Optional[kubernetes.client.V1ObjectReference] = ...,
        csi: typing.Optional[kubernetes.client.V1CSIPersistentVolumeSource] = ...,
        fc: typing.Optional[kubernetes.client.V1FCVolumeSource] = ...,
        flex_volume: typing.Optional[
            kubernetes.client.V1FlexPersistentVolumeSource
        ] = ...,
        flocker: typing.Optional[kubernetes.client.V1FlockerVolumeSource] = ...,
        gce_persistent_disk: typing.Optional[
            kubernetes.client.V1GCEPersistentDiskVolumeSource
        ] = ...,
        glusterfs: typing.Optional[
            kubernetes.client.V1GlusterfsPersistentVolumeSource
        ] = ...,
        host_path: typing.Optional[kubernetes.client.V1HostPathVolumeSource] = ...,
        iscsi: typing.Optional[kubernetes.client.V1ISCSIPersistentVolumeSource] = ...,
        local: typing.Optional[kubernetes.client.V1LocalVolumeSource] = ...,
        mount_options: typing.Optional[list[str]] = ...,
        nfs: typing.Optional[kubernetes.client.V1NFSVolumeSource] = ...,
        node_affinity: typing.Optional[kubernetes.client.V1VolumeNodeAffinity] = ...,
        persistent_volume_reclaim_policy: typing.Optional[str] = ...,
        photon_persistent_disk: typing.Optional[
            kubernetes.client.V1PhotonPersistentDiskVolumeSource
        ] = ...,
        portworx_volume: typing.Optional[
            kubernetes.client.V1PortworxVolumeSource
        ] = ...,
        quobyte: typing.Optional[kubernetes.client.V1QuobyteVolumeSource] = ...,
        rbd: typing.Optional[kubernetes.client.V1RBDPersistentVolumeSource] = ...,
        scale_io: typing.Optional[
            kubernetes.client.V1ScaleIOPersistentVolumeSource
        ] = ...,
        storage_class_name: typing.Optional[str] = ...,
        storageos: typing.Optional[
            kubernetes.client.V1StorageOSPersistentVolumeSource
        ] = ...,
        volume_attributes_class_name: typing.Optional[str] = ...,
        volume_mode: typing.Optional[str] = ...,
        vsphere_volume: typing.Optional[
            kubernetes.client.V1VsphereVirtualDiskVolumeSource
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1PersistentVolumeSpecDict: ...

class V1PersistentVolumeSpecDict(typing.TypedDict, total=False):
    accessModes: list[str]
    awsElasticBlockStore: kubernetes.client.V1AWSElasticBlockStoreVolumeSourceDict
    azureDisk: kubernetes.client.V1AzureDiskVolumeSourceDict
    azureFile: kubernetes.client.V1AzureFilePersistentVolumeSourceDict
    capacity: dict[str, str]
    cephfs: kubernetes.client.V1CephFSPersistentVolumeSourceDict
    cinder: kubernetes.client.V1CinderPersistentVolumeSourceDict
    claimRef: kubernetes.client.V1ObjectReferenceDict
    csi: kubernetes.client.V1CSIPersistentVolumeSourceDict
    fc: kubernetes.client.V1FCVolumeSourceDict
    flexVolume: kubernetes.client.V1FlexPersistentVolumeSourceDict
    flocker: kubernetes.client.V1FlockerVolumeSourceDict
    gcePersistentDisk: kubernetes.client.V1GCEPersistentDiskVolumeSourceDict
    glusterfs: kubernetes.client.V1GlusterfsPersistentVolumeSourceDict
    hostPath: kubernetes.client.V1HostPathVolumeSourceDict
    iscsi: kubernetes.client.V1ISCSIPersistentVolumeSourceDict
    local: kubernetes.client.V1LocalVolumeSourceDict
    mountOptions: list[str]
    nfs: kubernetes.client.V1NFSVolumeSourceDict
    nodeAffinity: kubernetes.client.V1VolumeNodeAffinityDict
    persistentVolumeReclaimPolicy: str
    photonPersistentDisk: kubernetes.client.V1PhotonPersistentDiskVolumeSourceDict
    portworxVolume: kubernetes.client.V1PortworxVolumeSourceDict
    quobyte: kubernetes.client.V1QuobyteVolumeSourceDict
    rbd: kubernetes.client.V1RBDPersistentVolumeSourceDict
    scaleIO: kubernetes.client.V1ScaleIOPersistentVolumeSourceDict
    storageClassName: str
    storageos: kubernetes.client.V1StorageOSPersistentVolumeSourceDict
    volumeAttributesClassName: str
    volumeMode: str
    vsphereVolume: kubernetes.client.V1VsphereVirtualDiskVolumeSourceDict
