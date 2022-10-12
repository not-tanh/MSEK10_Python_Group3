import traceback

from fastapi import APIRouter, HTTPException
from fastapi_pagination import Page, paginate

from student import Student
from db import db_get_list_student

router = APIRouter()


@router.get('/student', response_model=Page[Student])
async def get_students():
    try:
        students = db_get_list_student.getListStudent()
        return paginate(students)
    except:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail='Internal server error')


