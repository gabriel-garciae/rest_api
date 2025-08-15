from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    area: str
    job_description: str
    role: int
    salary: float
    is_active: bool
    last_evaluation: Optional[str]