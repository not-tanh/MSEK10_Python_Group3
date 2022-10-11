import sqlite3
import traceback

from fastapi import APIRouter, HTTPException

from student import Student
from db import db_update_student

router = APIRouter()


@router.put('/student')
def update_student(student: Student):
    try:
        db_update_student.updateStudent(student)
        return {'msg': 'Updated student successfully.'}
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail='Student ID is not valid')
    except:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail='Internal server error')
