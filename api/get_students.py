import sqlite3
import traceback

from fastapi import APIRouter, HTTPException
from fastapi_pagination import Page, add_pagination, paginate

from student import Student
from db import db_get_list_student as DBGetListStudent

router = APIRouter()


@router.get('/student', response_model=Page[Student])
async def get_students():
    students = DBGetListStudent.getListStudent()
    return paginate(students)

