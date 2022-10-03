from datetime import date
from pydantic import BaseModel


class StudentBase(BaseModel):
    sid: str


class Student(StudentBase):
    last_name: str
    first_name: str
    email: str
    dob: date
    hometown: str
    gpa: float
