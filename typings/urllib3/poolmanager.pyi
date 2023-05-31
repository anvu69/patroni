from typing import Any, Dict, Optional
from .response import HTTPResponse
class PoolManager:
    headers: Dict[str, str]
    connection_pool_kw: Dict[str, Any]
    def __init__(self, num_pools: int = 10, headers: Optional[Dict[str, str]] = None, **connection_pool_kw: Any) -> None: ...
    def urlopen(self, method: str, url: str, body: Optional[Any] = None, headers: Optional[Dict[str,str]] = None, encode_multipart: bool = True, multipart_boundary: Optional[str] = None, **kw: Any) -> HTTPResponse: ...
    def request(self, method: str, url: str, fields: Optional[Any] = None, headers: Optional[Dict[str, str]] = None, **urlopen_kw: Any) -> HTTPResponse: ...
    def clear(self) -> None: ...