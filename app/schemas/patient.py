from pydantic import BaseModel
from typing import List, Optional


class HumanName(BaseModel):
    family: Optional[str] = None
    given: Optional[List[str]] = None


class Patient(BaseModel):
    resourceType: str
    id: Optional[str] = None
    name: Optional[List[HumanName]] = None
    gender: Optional[str] = None
    birthDate: Optional[str] = None