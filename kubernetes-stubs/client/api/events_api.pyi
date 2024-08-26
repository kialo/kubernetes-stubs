import kubernetes.client
import typing

class EventsApi:
    def __init__(self, api_client: typing.Optional[kubernetes.client.ApiClient] = ...) -> None:
        ...
    def get_api_group(self) -> kubernetes.client.V1APIGroup:
        ...
