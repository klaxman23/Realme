from pydantic import BaseModel
from typing import List, Optional

class Student(BaseModel):
    roll_no: int
    age: int
    blood_group: str
    first_name: str
    last_name: str
    marks: float