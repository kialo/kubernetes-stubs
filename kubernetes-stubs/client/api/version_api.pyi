import kubernetes.client
import typing

class VersionApi:
    def __init__(self, api_client: typing.Optional[kubernetes.client.ApiClient] = ...) -> None:
        ...
    def get_code(self) -> kubernetes.client.VersionInfo:
        ...
