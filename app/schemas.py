import json
from pydantic import BaseModel
from typing import Optional

class ApplicationBase(BaseModel):
    id: Optional[int]
    name: str
    company: str
    position: str
    type: str
    salary_lower: Optional[int]
    salary_upper: Optional[int]
    technical_skills: Optional[dict]
    summary: Optional[str]
    other_app_info: Optional[dict]
    is_active: Optional[bool]
    status: Optional[str]

class ApplicationCreate(ApplicationBase):
    pass

class ApplicationUpdate(ApplicationBase):
    pass