from datetime import date

from pydantic import BaseModel, EmailStr


class StudentBase(BaseModel):
    sid: str


class Student(StudentBase):
    last_name: str
    first_name: str
    email: EmailStr
    dob: date
    hometown: str
    gpa: float
