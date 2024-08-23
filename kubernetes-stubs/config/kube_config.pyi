from typing import Any, List, Optional, Tuple

def load_kube_config(
    config_file: Optional[Any] = ...,
    context: Optional[Any] = ...,
    client_configuration: Optional[Any] = ...,
    persist_config: bool = ...,
    temp_file_path: Optional[Any] = ...,
) -> None: ...
def list_kube_config_contexts(config_file: Optional[Any] = ...) -> Tuple[List[Any], Any]: ...
