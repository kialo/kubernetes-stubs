from typing import Any, Generic, TypeVar

from .client import ApiClient

K8sModel = TypeVar("K8sModel")

class Watch(Generic[K8sModel]):
    _raw_return_type: Any
    _stop: bool
    _api_client: ApiClient
    resource_version: str | None

    def __init__(self, return_type: K8sModel = None): ...
    def stop(self) -> None: ...
    def stream(self, func: Any, *args: Any, **kwargs: Any) -> Any: ...
    def unmarshal_event(self, data: str, response_type: Any) -> dict[str, Any]: ...
