from typing import Any, Optional

from kubernetes.client.api_client import ApiClient as ApiClient

class CustomObjectsApi:
    api_client: ApiClient = ...
    def __init__(self, api_client: Optional[ApiClient] = ...) -> None: ...
    def get_namespaced_custom_object(
        self, group: str, version: str, namespace: str, plural: str, name: str
    ) -> dict[str, Any]: ...
    def patch_namespaced_custom_object(
        self,
        group: str,
        version: str,
        namespace: str,
        plural: str,
        name: str,
        body: dict[str, Any],
        *args: Any,
        field_manager: str,
    ) -> dict[str, Any]: ...
    def list_namespaced_custom_object(
        self, group: str, version: str, namespace: str, plural: str, **kwargs: Any
    ) -> dict[str, Any]: ...
