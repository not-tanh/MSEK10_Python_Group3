import sqlite3
import traceback

from fastapi import APIRouter, HTTPException

from student import Student
from db import db_update_student as DBUpdateStudent

router = APIRouter()


@router.put('/updatestudent')
def updateStudent(student: Student):
    try:
        result = DBUpdateStudent.updateStudent(student)

        return result
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail='Student ID is not valid')
    except:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail='Internal server error')
