from typing import Any, Optional

from pydantic import BaseModel


class CommonResponse(BaseModel):
    status: int
    message: str = 'success'
    data: Optional[Any] = None
