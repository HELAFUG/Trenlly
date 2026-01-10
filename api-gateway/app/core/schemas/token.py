from typing import Optional

from pydantic import BaseModel


class AccessTokenData(BaseModel):
    user_id: int
    email: Optional[str] = None
