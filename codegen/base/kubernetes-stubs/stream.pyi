from .client import ApiClient
from .client.rest import RESTResponse

class WsResponse(RESTResponse): ...
class WsApiClient(ApiClient): ...
