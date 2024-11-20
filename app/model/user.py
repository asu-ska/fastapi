from datetime import datetime
from typing import List, Union
from pydantic import BaseModel

class User(BaseModel):
    id: int = 0
    name: str
    signup_ts: datetime|None = None
    friends: List[int] = []
