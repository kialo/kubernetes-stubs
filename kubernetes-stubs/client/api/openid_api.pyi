import kubernetes.client
import typing

class OpenidApi:
    def __init__(self, api_client: typing.Optional[kubernetes.client.ApiClient] = ...) -> None:
        ...
    def get_service_account_issuer_open_id_keyset(self) -> str:
        ...
