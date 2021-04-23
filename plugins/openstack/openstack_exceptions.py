# Some common builtin exeptions we might want to watch for
PYTHON_BUILTIN_EXCEPTIONS = [
    "AttributeError",
    "IndexError",
    "KeyError",
    "ValueError",
]

# https://opendev.org/openstack/oslo.db/src/branch/master/oslo_db/exception.py
OSLO_DB_EXCEPTIONS = [
    "DBError",
    "DBDuplicateEntry",
    "DBConstraintError",
    "DBReferenceError",
    "DBNonExistentConstraint",
    "DBNonExistentTable",
    "DBNonExistentDatabase",
    "DBDeadlock",
    "DBInvalidUnicodeParameter",
    "DBMigrationError",
    "DBConnectionError",
    "DBDataError",
    "DBNotSupportedError",
    "InvalidSortKey",
    "ColumnError",
    "BackendNotAvailable",
    "RetryRequest",
    "NoEngineContextEstablished",
    "ContextNotRequestedError",
    "CantStartEngineError",
]

# https://opendev.org/openstack/oslo.messaging/src/branch/master/oslo_messaging/exceptions.py
OSLO_MESSAGING_EXCEPTIONS = [
    "MessagingException",
    "MessagingTimeout",
    "MessageDeliveryFailure",
    "InvalidTarget",
    "MessageUndeliverable",
]

# Since there are many many exception types we need to cherry-pick the ones we
# care about to avoid search expresssions becoming too huge.
# e.g. sed -rn 's/^class\s+(\S+)\(.+/    "\1",/p' nova/exception.py
NOVA_EXCEPTIONS = [
    "ConvertedException",
    "NovaException",
    "EncryptionFailure",
    "VirtualInterfaceCreateException",
    "VirtualInterfaceMacAddressException",
    "VirtualInterfacePlugException",
    "VirtualInterfaceUnplugException",
    "GlanceConnectionFailed",
    "CinderConnectionFailed",
    "UnsupportedCinderAPIVersion",
    "CinderAPIVersionNotAvailable",
    "Forbidden",
    "ForbiddenWithAccelerators",
    "AdminRequired",
    "PolicyNotAuthorized",
    "ImageNotActive",
    "ImageNotAuthorized",
    "Invalid",
    "InvalidConfiguration",
    "InvalidBDM",
    "InvalidBDMSnapshot",
    "InvalidBDMVolume",
    "InvalidBDMImage",
    "InvalidBDMBootSequence",
    "InvalidBDMLocalsLimit",
    "InvalidBDMEphemeralSize",
    "InvalidBDMSwapSize",
    "InvalidBDMFormat",
    "InvalidBDMForLegacy",
    "InvalidBDMVolumeNotBootable",
    "TooManyDiskDevices",
    "InvalidBDMDiskBus",
    "InvalidAttribute",
    "ValidationError",
    "VolumeAttachFailed",
    "VolumeDetachFailed",
    "MultiattachNotSupportedByVirtDriver",
    "MultiattachNotSupportedOldMicroversion",
    "MultiattachToShelvedNotSupported",
    "MultiattachSwapVolumeNotSupported",
    "VolumeNotCreated",
    "ExtendVolumeNotSupported",
    "VolumeEncryptionNotSupported",
    "VolumeTaggedAttachNotSupported",
    "VolumeTaggedAttachToShelvedNotSupported",
    "NetworkInterfaceTaggedAttachNotSupported",
    "InvalidKeypair",
    "InvalidRequest",
    "InvalidInput",
    "InvalidVolume",
    "InvalidVolumeAccessMode",
    "StaleVolumeMount",
    "InvalidMetadata",
    "InvalidMetadataSize",
    "InvalidPortRange",
    "InvalidIpProtocol",
    "InvalidContentType",
    "InvalidAPIVersionString",
    "VersionNotFoundForAPIMethod",
    "InvalidGlobalAPIVersion",
    "ApiVersionsIntersect",
    "InvalidParameterValue",
    "InvalidAggregateAction",
    "InvalidAggregateActionAdd",
    "InvalidAggregateActionDelete",
    "InvalidAggregateActionUpdate",
    "InvalidAggregateActionUpdateMeta",
    "InvalidSortKey",
    "InvalidStrTime",
    "InvalidNUMANodesNumber",
    "InvalidName",
    "InstanceInvalidState",
    "InstanceNotRunning",
    "InstanceNotInRescueMode",
    "InstanceNotRescuable",
    "InstanceNotReady",
    "InstanceSuspendFailure",
    "InstanceResumeFailure",
    "InstancePowerOnFailure",
    "InstancePowerOffFailure",
    "InstanceRebootFailure",
    "InstanceTerminationFailure",
    "InstanceDeployFailure",
    "MultiplePortsNotApplicable",
    "InvalidFixedIpAndMaxCountRequest",
    "ServiceUnavailable",
    "ServiceNotUnique",
    "ComputeResourcesUnavailable",
    "HypervisorUnavailable",
    "ComputeServiceUnavailable",
    "ComputeServiceInUse",
    "UnableToMigrateToSelf",
    "OperationNotSupportedForSEV",
    "OperationNotSupportedForVTPM",
    "OperationNotSupportedForVDPAInterface",
    "InvalidHypervisorType",
    "HypervisorTooOld",
    "DestinationHypervisorTooOld",
    "ServiceTooOld",
    "TooOldComputeService",
    "DestinationDiskExists",
    "InvalidDevicePath",
    "DevicePathInUse",
    "InvalidCPUInfo",
    "InvalidIpAddressError",
    "InvalidDiskFormat",
    "InvalidDiskInfo",
    "DiskInfoReadWriteFail",
    "ImageUnacceptable",
    "ImageBadRequest",
    "ImageImportImpossible",
    "ImageQuotaExceeded",
    "InstanceUnacceptable",
    "InvalidUUID",
    "InvalidID",
    "ConstraintNotMet",
    "NotFound",
    "VolumeAttachmentNotFound",
    "VolumeNotFound",
    "VolumeTypeNotFound",
    "UndefinedRootBDM",
    "BDMNotFound",
    "VolumeBDMNotFound",
    "VolumeBDMIsMultiAttach",
    "VolumeBDMPathNotFound",
    "DeviceDetachFailed",
    "DeviceNotFound",
    "SnapshotNotFound",
    "DiskNotFound",
    "VolumeDriverNotFound",
    "VolumeDriverNotSupported",
    "InvalidImageRef",
    "AutoDiskConfigDisabledByImage",
    "ImageNotFound",
    "ImageDeleteConflict",
    "PreserveEphemeralNotSupported",
    "InstanceMappingNotFound",
    "InvalidCidr",
    "NetworkNotFound",
    "PortNotFound",
    "NetworkNotFoundForBridge",
    "NetworkNotFoundForInstance",
    "NetworkAmbiguous",
    "UnableToAutoAllocateNetwork",
    "NetworkRequiresSubnet",
    "ExternalNetworkAttachForbidden",
    "NetworkMissingPhysicalNetwork",
    "VifDetailsMissingVhostuserSockPath",
    "VifDetailsMissingMacvtapParameters",
    "DatastoreNotFound",
    "PortInUse",
    "PortRequiresFixedIP",
    "PortNotUsable",
    "PortNotUsableDNS",
    "PortBindingFailed",
    "PortBindingDeletionFailed",
    "PortBindingActivationFailed",
    "PortUpdateFailed",
    "AttachSRIOVPortNotSupported",
    "FixedIpNotFoundForAddress",
    "FixedIpNotFoundForInstance",
    "FixedIpAlreadyInUse",
    "FixedIpAssociatedWithMultipleInstances",
    "FixedIpInvalidOnHost",
    "NoMoreFixedIps",
    "FloatingIpNotFound",
    "FloatingIpNotFoundForAddress",
    "FloatingIpMultipleFoundForAddress",
    "FloatingIpPoolNotFound",
    "NoMoreFloatingIps",
    "FloatingIpAssociated",
    "NoFloatingIpInterface",
    "FloatingIpAssociateFailed",
    "FloatingIpBadRequest",
    "KeypairNotFound",
    "ServiceNotFound",
    "ConfGroupForServiceTypeNotFound",
    "ServiceBinaryExists",
    "ServiceTopicExists",
    "HostNotFound",
    "ComputeHostNotFound",
    "HostBinaryNotFound",
    "InvalidQuotaValue",
    "InvalidQuotaMethodUsage",
    "QuotaNotFound",
    "QuotaExists",
    "QuotaResourceUnknown",
    "ProjectUserQuotaNotFound",
    "ProjectQuotaNotFound",
    "QuotaClassNotFound",
    "QuotaClassExists",
    "OverQuota",
    "SecurityGroupNotFound",
    "SecurityGroupNotFoundForProject",
    "SecurityGroupExists",
    "SecurityGroupCannotBeApplied",
    "NoUniqueMatch",
    "NoActiveMigrationForInstance",
    "MigrationNotFound",
    "MigrationNotFoundByStatus",
    "MigrationNotFoundForInstance",
    "InvalidMigrationState",
    "ConsoleLogOutputException",
    "ConsoleNotAvailable",
    "ConsoleTypeInvalid",
    "ConsoleTypeUnavailable",
    "ConsolePortRangeExhausted",
    "FlavorNotFound",
    "FlavorNotFoundByName",
    "FlavorAccessNotFound",
    "FlavorExtraSpecUpdateCreateFailed",
    "CellTimeout",
    "SchedulerHostFilterNotFound",
    "FlavorExtraSpecsNotFound",
    "ComputeHostMetricNotFound",
    "FileNotFound",
    "ClassNotFound",
    "InstanceTagNotFound",
    "KeyPairExists",
    "InstanceExists",
    "FlavorExists",
    "FlavorIdExists",
    "FlavorAccessExists",
    "InvalidSharedStorage",
    "InvalidLocalStorage",
    "StorageError",
    "MigrationError",
    "MigrationPreCheckError",
    "MigrationSchedulerRPCError",
    "MalformedRequestBody",
    "ConfigNotFound",
    "PasteAppNotFound",
    "CannotResizeToSameFlavor",
    "ResizeError",
    "CannotResizeDisk",
    "FlavorMemoryTooSmall",
    "FlavorDiskTooSmall",
    "FlavorDiskSmallerThanImage",
    "FlavorDiskSmallerThanMinDisk",
    "VolumeSmallerThanMinDisk",
    "BootFromVolumeRequiredForZeroDiskFlavor",
    "NoValidHost",
    "RequestFilterFailed",
    "InvalidRoutedNetworkConfiguration",
    "MaxRetriesExceeded",
    "QuotaError",
    "TooManyInstances",
    "FloatingIpLimitExceeded",
    "MetadataLimitExceeded",
    "OnsetFileLimitExceeded",
    "OnsetFilePathLimitExceeded",
    "OnsetFileContentLimitExceeded",
    "KeypairLimitExceeded",
    "SecurityGroupLimitExceeded",
    "PortLimitExceeded",
    "AggregateNotFound",
    "AggregateNameExists",
    "AggregateHostNotFound",
    "AggregateMetadataNotFound",
    "AggregateHostExists",
    "InstancePasswordSetFailed",
    "InstanceNotFound",
    "InstanceInfoCacheNotFound",
    "MarkerNotFound",
    "CouldNotFetchImage",
    "CouldNotUploadImage",
    "TaskAlreadyRunning",
    "TaskNotRunning",
    "InstanceIsLocked",
    "ConfigDriveInvalidValue",
    "ConfigDriveUnsupportedFormat",
    "ConfigDriveMountFailed",
    "ConfigDriveUnknownFormat",
    "ConfigDriveNotFound",
    "InterfaceAttachFailed",
    "InterfaceAttachFailedNoNetwork",
    "InterfaceAttachPciClaimFailed",
    "InterfaceAttachResourceAllocationFailed",
    "InterfaceDetachFailed",
    "InstanceUserDataMalformed",
    "InstanceUpdateConflict",
    "UnknownInstanceUpdateConflict",
    "UnexpectedTaskStateError",
    "UnexpectedDeletingTaskStateError",
    "InstanceActionNotFound",
    "InstanceActionEventNotFound",
    "InstanceEvacuateNotSupported",
    "DBNotAllowed",
    "UnsupportedVirtType",
    "UnsupportedHardware",
    "UnsupportedRescueBus",
    "UnsupportedRescueDevice",
    "UnsupportedRescueImage",
    "Base64Exception",
    "BuildAbortException",
    "RescheduledException",
    "ShadowTableExists",
    "InstanceFaultRollback",
    "OrphanedObjectError",
    "ObjectActionError",
    "InstanceGroupNotFound",
    "InstanceGroupIdExists",
    "InstanceGroupSaveException",
    "ResourceMonitorError",
    "PciDeviceWrongAddressFormat",
    "PciDeviceInvalidDeviceName",
    "PciDeviceNotFoundById",
    "PciDeviceNotFound",
    "PciDeviceInvalidStatus",
    "PciDeviceVFInvalidStatus",
    "PciDevicePFInvalidStatus",
    "PciDeviceInvalidOwner",
    "PciDeviceRequestFailed",
    "PciDevicePoolEmpty",
    "PciInvalidAlias",
    "PciRequestAliasNotDefined",
    "PciConfigInvalidWhitelist",
    "PciRequestFromVIFNotFound",
    "InternalError",
    "PciDeviceDetachFailed",
    "PciDeviceUnsupportedHypervisor",
    "KeyManagerError",
    "VolumesNotRemoved",
    "VolumeRebaseFailed",
    "InvalidVideoMode",
    "RngDeviceNotExist",
    "RequestedVRamTooHigh",
    "SecurityProxyNegotiationFailed",
    "RFBAuthHandshakeFailed",
    "RFBAuthNoAvailableScheme",
    "InvalidWatchdogAction",
    "LiveMigrationNotSubmitted",
    "SelectionObjectsWithOldRPCVersionNotSupported",
    "LiveMigrationURINotAvailable",
    "UnshelveException",
    "MismatchVolumeAZException",
    "UnshelveInstanceInvalidState",
    "ImageVCPULimitsRangeExceeded",
    "ImageVCPUTopologyRangeExceeded",
    "ImageVCPULimitsRangeImpossible",
    "InvalidArchitectureName",
    "ImageNUMATopologyIncomplete",
    "ImageNUMATopologyForbidden",
    "ImageNUMATopologyRebuildConflict",
    "ImagePCINUMAPolicyForbidden",
    "ImageNUMATopologyAsymmetric",
    "ImageNUMATopologyCPUOutOfRange",
    "ImageNUMATopologyCPUDuplicates",
    "ImageNUMATopologyCPUsUnassigned",
    "ImageNUMATopologyMemoryOutOfRange",
    "InvalidHostname",
    "NumaTopologyNotFound",
    "MigrationContextNotFound",
    "SocketPortRangeExhaustedException",
    "SocketPortInUseException",
    "ImageSerialPortNumberInvalid",
    "ImageSerialPortNumberExceedFlavorValue",
    "SerialPortNumberLimitExceeded",
    "InvalidImageConfigDrive",
    "InvalidHypervisorVirtType",
    "InvalidMachineType",
    "InvalidMachineTypeUpdate",
    "UnsupportedMachineType",
    "InvalidVirtualMachineMode",
    "InvalidToken",
    "TokenInUse",
    "InvalidConnectionInfo",
    "InstanceQuiesceNotSupported",
    "InstanceAgentNotEnabled",
    "QemuGuestAgentNotEnabled",
    "SetAdminPasswdNotSupported",
    "MemoryPageSizeInvalid",
    "MemoryPageSizeForbidden",
    "MemoryPageSizeNotSupported",
    "CPUPinningInvalid",
    "CPUUnpinningInvalid",
    "CPUPinningUnknown",
    "CPUUnpinningUnknown",
    "ImageCPUPinningForbidden",
    "ImageCPUThreadPolicyForbidden",
    "ImagePMUConflict",
    "UnsupportedPolicyException",
    "CellMappingNotFound",
    "NUMATopologyUnsupported",
    "MemoryPagesUnsupported",
    "InvalidImageFormat",
    "UnsupportedImageModel",
    "HostMappingNotFound",
    "HostMappingExists",
    "RealtimeConfigurationInvalid",
    "CPUThreadPolicyConfigurationInvalid",
    "RequestSpecNotFound",
    "UEFINotSupported",
    "SecureBootNotSupported",
    "TriggerCrashDumpNotSupported",
    "UnsupportedHostCPUControlPolicy",
    "LibguestfsCannotReadKernel",
    "RealtimeMaskNotFoundOrInvalid",
    "OsInfoNotFound",
    "BuildRequestNotFound",
    "AttachInterfaceNotSupported",
    "AttachInterfaceWithQoSPolicyNotSupported",
    "NetworksWithQoSPolicyNotSupported",
    "CreateWithPortResourceRequestOldVersion",
    "InvalidReservedMemoryPagesOption",
    "ResourceProviderInUse",
    "ResourceProviderRetrievalFailed",
    "ResourceProviderAggregateRetrievalFailed",
    "ResourceProviderTraitRetrievalFailed",
    "ResourceProviderCreationFailed",
    "ResourceProviderDeletionFailed",
    "ResourceProviderUpdateFailed",
    "ResourceProviderNotFound",
    "ResourceProviderSyncFailed",
    "PlacementAPIConnectFailure",
    "PlacementAPIConflict",
    "ResourceProviderUpdateConflict",
    "InvalidResourceClass",
    "InvalidInventory",
    "InventoryInUse",
    "UsagesRetrievalFailed",
    "NotSupportedWithOption",
    "Unauthorized",
    "NeutronAdminCredentialConfigurationInvalid",
    "InvalidEmulatorThreadsPolicy",
    "InvalidCPUAllocationPolicy",
    "InvalidCPUThreadAllocationPolicy",
    "BadRequirementEmulatorThreadsPolicy",
    "InvalidNetworkNUMAAffinity",
    "InvalidPCINUMAAffinity",
    "PowerVMAPIFailed",
    "TraitRetrievalFailed",
    "TraitCreationFailed",
    "CannotMigrateToSameHost",
    "VirtDriverNotReady",
    "InvalidPeerList",
    "InstanceDiskMappingFailed",
    "NewMgmtMappingNotFoundException",
    "NoDiskDiscoveryException",
    "UniqueDiskDiscoveryException",
    "DeviceDeletionException",
    "OptRequiredIfOtherOptValue",
    "AllocationCreateFailed",
    "AllocationUpdateFailed",
    "AllocationMoveFailed",
    "AllocationDeleteFailed",
    "TooManyComputesForHost",
    "CertificateValidationFailed",
    "InstanceRescueFailure",
    "InstanceUnRescueFailure",
    "IronicAPIVersionNotAvailable",
    "ZVMDriverException",
    "ZVMConnectorError",
    "NoResourceClass",
    "ResourceProviderAllocationRetrievalFailed",
    "ConsumerAllocationRetrievalFailed",
    "ReshapeFailed",
    "ReshapeNeeded",
    "FlavorImageConflict",
    "MissingDomainCapabilityFeatureException",
    "HealPortAllocationException",
    "MoreThanOneResourceProviderToHealFrom",
    "NoResourceProviderToHealFrom",
    "UnableToQueryPorts",
    "UnableToUpdatePorts",
    "UnableToRollbackPortUpdates",
    "AssignedResourceNotFound",
    "PMEMNamespaceConfigInvalid",
    "GetPMEMNamespacesFailed",
    "VPMEMCleanupFailed",
    "RequestGroupSuffixConflict",
    "AmbiguousResourceProviderForPCIRequest",
    "UnexpectedResourceProviderNameForPCIRequest",
    "DeviceProfileError",
    "AcceleratorRequestOpFailed",
    "AcceleratorRequestBindingFailed",
    "InvalidLibvirtGPUConfig",
    "RequiredMixedInstancePolicy",
    "RequiredMixedOrRealtimeCPUMask",
    "MixedInstanceNotSupportByComputeService",
    "InvalidMixedInstanceDedicatedMask",
    "ProviderConfigException",
]

# From https://github.com/openstack/octavia/blob/master/octavia/common/exceptions.py
OCTAVIA_EXCEPTIONS = [
    "OctaviaException",
    "APIException",
    "NotFound",
    "PolicyForbidden",
    "InvalidOption",
    "InvalidFilterArgument",
    "DisabledOption",
    "L7RuleValidation",
    "SingleCreateDetailsMissing",
    "InvalidHMACException",
    "MissingArguments",
    "NetworkConfig",
    "NeedsPassphrase",
    "UnreadableCert",
    "UnreadablePKCS12",
    "MisMatchedKey",
    "CertificateRetrievalException",
    "CertificateStorageException",
    "CertificateGenerationException",
    "DuplicateListenerEntry",
    "DuplicateMemberEntry",
    "DuplicateHealthMonitor",
    "DuplicatePoolEntry",
    "PoolInUseByL7Policy",
    "ImmutableObject",
    "LBPendingStateError",
    "TooManyL7RulesOnL7Policy",
    "ComputeBuildException",
    "ComputeBuildQueueTimeoutException",
    "ComputeDeleteException",
    "ComputeGetException",
    "ComputeStatusException",
    "ComputeGetInterfaceException",
    "IDAlreadyExists",
    "RecordAlreadyExists",
    "NoReadyAmphoraeException",
    "ImageGetException",
    "ComputeWaitTimeoutException",
    "ComputePortInUseException",
    "ComputeUnknownException",
    "InvalidTopology",
    "InvalidL7PolicyAction",
    "InvalidL7PolicyArgs",
    "InvalidURL",
    "InvalidURLPath",
    "InvalidString",
    "InvalidRegex",
    "InvalidL7Rule",
    "ServerGroupObjectCreateException",
    "ServerGroupObjectDeleteException",
    "InvalidAmphoraOperatingSystem",
    "QuotaException",
    "ProjectBusyException",
    "MissingProjectID",
    "MissingAPIProjectID",
    "InvalidSubresource",
    "ValidationException",
    "VIPValidationException",
    "InvalidSortKey",
    "InvalidSortDirection",
    "InvalidMarker",
    "InvalidLimit",
    "MissingVIPSecurityGroup",
    "ProviderNotEnabled",
    "ProviderNotFound",
    "ProviderDriverError",
    "ProviderNotImplementedError",
    "ProviderUnsupportedOptionError",
    "InputFileError",
    "ObjectInUse",
    "ProviderFlavorMismatchError",
    "VolumeDeleteException",
    "VolumeGetException",
    "NetworkServiceError",
    "InvalidIPAddress",
]

# From https://github.com/openstack/manila/blob/master/manila/exception.py
MANILA_EXCEPTIONS = [
    "ConvertedException",
    "Error",
    "ManilaException",
    "NetworkException",
    "NetworkBindException",
    "NetworkBadConfigurationException",
    "BadConfigurationException",
    "NotAuthorized",
    "AdminRequired",
    "PolicyNotAuthorized",
    "Conflict",
    "Invalid",
    "InvalidRequest",
    "InvalidResults",
    "InvalidInput",
    "InvalidContentType",
    "InvalidHost",
    "InvalidParameterValue",
    "InvalidUUID",
    "InvalidDriverMode",
    "InvalidAPIVersionString",
    "VersionNotFoundForAPIMethod",
    "InvalidGlobalAPIVersion",
    "InvalidCapacity",
    "NotFound",
    "MessageNotFound",
    "Found",
    "InUse",
    "AvailabilityZoneNotFound",
    "ShareNetworkNotFound",
    "ShareNetworkSubnetNotFound",
    "ShareServerNotFound",
    "ShareServerNotFoundByFilters",
    "InvalidShareNetwork",
    "ShareServerInUse",
    "ShareServerMigrationError",
    "ShareServerMigrationFailed",
    "InvalidShareServer",
    "ShareMigrationError",
    "ShareMigrationFailed",
    "ShareDataCopyFailed",
    "ShareDataCopyCancelled",
    "ServiceIPNotFound",
    "AdminIPNotFound",
    "ShareServerNotCreated",
    "ShareServerNotReady",
    "ServiceNotFound",
    "ServiceIsDown",
    "HostNotFound",
    "SchedulerHostFilterNotFound",
    "SchedulerHostWeigherNotFound",
    "HostBinaryNotFound",
    "InvalidReservationExpiration",
    "InvalidQuotaValue",
    "QuotaNotFound",
    "QuotaExists",
    "QuotaResourceUnknown",
    "ProjectUserQuotaNotFound",
    "ProjectShareTypeQuotaNotFound",
    "ProjectQuotaNotFound",
    "QuotaClassNotFound",
    "QuotaUsageNotFound",
    "ReservationNotFound",
    "OverQuota",
    "MigrationNotFound",
    "MigrationNotFoundByStatus",
    "FileNotFound",
    "MigrationError",
    "MalformedRequestBody",
    "ConfigNotFound",
    "PasteAppNotFound",
    "NoValidHost",
    "WillNotSchedule",
    "QuotaError",
    "ShareSizeExceedsAvailableQuota",
    "SnapshotSizeExceedsAvailableQuota",
    "ShareSizeExceedsLimit",
    "ShareLimitExceeded",
    "SnapshotLimitExceeded",
    "ShareNetworksLimitExceeded",
    "ShareGroupsLimitExceeded",
    "ShareGroupSnapshotsLimitExceeded",
    "ShareReplicasLimitExceeded",
    "ShareReplicaSizeExceedsAvailableQuota",
#    "GlusterfsException",
    "InvalidShare",
    "ShareBusyException",
    "InvalidShareInstance",
    "ManageInvalidShare",
    "ManageShareServerError",
    "UnmanageInvalidShare",
    "PortLimitExceeded",
    "ShareAccessExists",
    "ShareAccessMetadataNotFound",
    "ShareSnapshotAccessExists",
    "InvalidSnapshotAccess",
    "InvalidShareAccess",
    "InvalidShareAccessLevel",
    "InvalidShareAccessType",
    "ShareBackendException",
    "ExportLocationNotFound",
    "ShareNotFound",
    "ShareSnapshotNotFound",
    "ShareSnapshotInstanceNotFound",
    "ShareSnapshotNotSupported",
    "ShareGroupSnapshotNotSupported",
    "ShareSnapshotIsBusy",
    "InvalidShareSnapshot",
    "InvalidShareSnapshotInstance",
    "ManageInvalidShareSnapshot",
    "UnmanageInvalidShareSnapshot",
    "ShareMetadataNotFound",
    "InvalidMetadata",
    "InvalidMetadataSize",
    "SecurityServiceNotFound",
    "InvalidSecurityService",
    "ShareNetworkSecurityServiceAssociationError",
    "ShareNetworkSecurityServiceDissociationError",
    "SecurityServiceFailedAuth",
    "InvalidVolume",
    "InvalidShareType",
    "InvalidShareGroupType",
    "InvalidExtraSpec",
    "VolumeNotFound",
    "VolumeSnapshotNotFound",
    "ShareTypeNotFound",
    "ShareGroupTypeNotFound",
    "ShareTypeAccessNotFound",
    "ShareGroupTypeAccessNotFound",
    "ShareTypeNotFoundByName",
    "ShareGroupTypeNotFoundByName",
    "ShareTypeExtraSpecsNotFound",
    "ShareGroupTypeSpecsNotFound",
    "ShareTypeInUse",
    "IPAddressInUse",
    "ShareGroupTypeInUse",
    "ShareTypeExists",
    "ShareTypeDoesNotExist",
    "DefaultShareTypeNotConfigured",
    "ShareGroupTypeExists",
    "ShareTypeAccessExists",
    "ShareGroupTypeAccessExists",
    "ShareTypeCreateFailed",
    "ShareTypeUpdateFailed",
    "ShareGroupTypeCreateFailed",
    "ManageExistingShareTypeMismatch",
    "ShareExtendingError",
    "ShareShrinkingError",
    "ShareShrinkingPossibleDataLoss",
    "InstanceNotFound",
    "BridgeDoesNotExist",
    "ServiceInstanceException",
    "ServiceInstanceUnavailable",
    "StorageResourceException",
    "StorageResourceNotFound",
    "SnapshotResourceNotFound",
    "SnapshotUnavailable",
#    "NetAppException",
#    "VserverNotFound",
#    "VserverNotSpecified",
#    "VserverNotReady",
#    "EMCPowerMaxXMLAPIError",
#    "EMCPowerMaxLockRequiredException",
#    "EMCPowerMaxInvalidMoverID",
#    "EMCVnxXMLAPIError",
#    "EMCVnxLockRequiredException",
#    "EMCVnxInvalidMoverID",
#    "EMCUnityError",
#    "HPE3ParInvalidClient",
#    "HPE3ParInvalid",
#    "HPE3ParUnexpectedError",
#    "GPFSException",
#    "GPFSGaneshaException",
    "GaneshaCommandFailure",
    "InvalidSqliteDB",
    "SSHException",
#    "HDFSException",
#    "MapRFSException",
#    "ZFSonLinuxException",
    "QBException",
    "QBRpcException",
    "SSHInjectionThreat",
#    "HNASBackendException",
#    "HNASConnException",
#    "HNASSSCIsBusy",
#    "HNASSSCContextChange",
#    "HNASDirectoryNotEmpty",
#    "HNASItemNotFoundException",
#    "HNASNothingToCloneException",
    "ShareGroupNotFound",
    "ShareGroupSnapshotNotFound",
    "ShareGroupSnapshotMemberNotFound",
    "InvalidShareGroup",
    "InvalidShareGroupSnapshot",
    "DriverNotInitialized",
    "ShareResourceNotFound",
    "ShareUmountException",
    "ShareMountException",
    "ShareCopyDataException",
    "ReplicationException",
    "ShareReplicaNotFound",
#    "TegileAPIException",
    "StorageCommunicationException",
    "EvaluatorParseException",
#    "HSPBackendException",
#    "HSPTimeoutException",
#    "HSPItemNotFoundException",
#    "NexentaException",
    "LockCreationFailed",
    "LockingFailed",
    "GaneshaException",
#    "InfortrendCLIException",
#    "InfortrendNASException",
#    "ZadaraUnknownCmd",
#    "ZadaraSessionRequestException",
#    "ZadaraBadHTTPResponseStatus",
#    "ZadaraFailedCmdWithDump",
#    "ZadaraVPSANoActiveController",
#    "ZadaraServerCreateFailure",
#    "ZadaraAttachmentsNotFound",
#    "ZadaraManilaInvalidAccessKey",
#    "ZadaraVPSAVolumeShareFailed",
#    "ZadaraInvalidShareAccessType",
#    "ZadaraShareNotFound",
#    "ZadaraExtendShareFailed",
#    "ZadaraInvalidProtocol",
#    "ZadaraShareNotValid",
#    "ZadaraVPSASnapshotCreateFailed",
#    "ZadaraVPSASnapshotManageFailed",
#    "ZadaraServerNotFound",
]