from typing import Any, Dict, Optional

from . import V1ObjectMeta

class V1Secret:
    def __init__(
        self,
        api_version: Optional[Any] = ...,
        data: Optional[Dict[str, str]] = ...,
        immutable: Optional[Any] = ...,
        kind: Optional[Any] = ...,
        metadata: Optional[V1ObjectMeta] = ...,
        string_data: Optional[Any] = ...,
        type: Optional[Any] = ...,
        local_vars_configuration: Optional[Any] = ...,
    ) -> None: ...
    @property
    def data(self) -> Any: ...
    @property
    def metadata(self) -> V1ObjectMeta: ...
