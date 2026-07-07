from pydantic import BaseModel
from typing import List

class UserProfile(BaseModel):
    name: str
    profession: str
    skills: List[str]
    interests: List[str]
    bio: str

class EventDetails(BaseModel):
    title: str
    description: str