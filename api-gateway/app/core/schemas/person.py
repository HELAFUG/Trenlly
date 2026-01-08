from typing import Optional
from pydantic import BaseModel,EmailStr
class PersonBase(BaseModel):
    email:EmailStr
    age:int
    name:str

class PersonCreate(PersonBase):
    password:str
    last_name:Optional[str]=None

class Person(PersonBase):
    id:int
    last_name:Optional[str]=None
