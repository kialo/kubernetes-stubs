from typing import Any, Optional

class Configuration(object):
    api_key: dict[str, str]
    api_key_prefix: str
    assert_hostname: Any
    cert_file: Any
    connection_pool_maxsize: Any
    discard_unknown_keys: bool
    host: str
    key_file: Any
    logger: Any
    logger_file_handler: Any
    logger_stream_handler: Any
    password: str
    proxy: Any
    safe_chars_for_path_param: str
    ssl_ca_cert: Any
    temp_folder_path: str
    username: str
    verify_ssl: bool
    def __init__(
        self,
        host: str = ...,
        api_key: Optional[str] = ...,
        api_key_prefix: Optional[str] = ...,
        username: Optional[str] = ...,
        password: Optional[str] = ...,
        discard_unknown_keys: bool = ...,
    ) -> None: ...
