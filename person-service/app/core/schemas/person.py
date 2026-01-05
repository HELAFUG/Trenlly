from typing import Optional

from pydantic import BaseModel


class PersonBase(BaseModel):
    email: str
    name: str
    age: int


class PersonCreate(PersonBase):
    password: str
    last_name: Optional[str] = None


class Person(PersonBase):
    id: int
    last_name: Optional[str] = None
