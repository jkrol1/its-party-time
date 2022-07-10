from typing import Dict, Union, Tuple

from app.extensions import db

EndpointResponseBody = Union[Dict[str, Union[str, int]], db.Model]
EndpointResponse = Tuple[EndpointResponseBody, int]
