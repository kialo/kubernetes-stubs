from datetime import datetime
from typing import Any, Dict, List, Optional

from . import V1OwnerReference

class V1ObjectMeta:
    def __init__(
        self,
        annotations: Optional[Any] = ...,
        creation_timestamp: Optional[Any] = ...,
        deletion_grace_period_seconds: Optional[Any] = ...,
        deletion_timestamp: Optional[Any] = ...,
        finalizers: Optional[Any] = ...,
        generate_name: Optional[Any] = ...,
        generation: Optional[Any] = ...,
        labels: Optional[Any] = ...,
        managed_fields: Optional[Any] = ...,
        name: Optional[Any] = ...,
        namespace: Optional[Any] = ...,
        owner_references: Optional[Any] = ...,
        resource_version: Optional[Any] = ...,
        self_link: Optional[Any] = ...,
        uid: Optional[Any] = ...,
        local_vars_configuration: Optional[Any] = ...,
    ) -> None: ...
    @property
    def annotations(self) -> dict[str, str]: ...
    @property
    def name(self) -> str: ...
    @property
    def namespace(self) -> str: ...
    @property
    def creation_timestamp(self) -> datetime: ...
    @property
    def deletion_timestamp(self) -> datetime: ...
    @property
    def labels(self) -> Dict[str, str]: ...
    @property
    def uid(self) -> str: ...
    @property
    def owner_references(self) -> List[V1OwnerReference]: ...
    @property
    def resource_version(self) -> str: ...
