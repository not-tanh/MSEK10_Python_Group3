import sqlite3
import traceback

from fastapi import APIRouter, HTTPException

from student import Student
from db import db_create_student as db_create

router = APIRouter()


@router.post('/student')
def create_student(student_data: Student):
    try:
        db_create.insertStudent(student_data)
        return {'msg': 'Created student successfully.'}
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail='Student ID is not valid')
    except:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail='Internal server error')
