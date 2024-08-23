from http import HTTPStatus
from typing import Any, Dict, Optional

class OpenApiException(Exception): ...

class ApiException(OpenApiException):
    status: HTTPStatus
    body: Optional[str]
    headers: Optional[Dict[str, str]]
    def __init__(
        self, status: Optional[Any] = ..., reason: Optional[Any] = ..., http_resp: Optional[Any] = ...
    ) -> None: ...
