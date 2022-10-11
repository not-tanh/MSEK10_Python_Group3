import sqlite3
import traceback

from fastapi import APIRouter, HTTPException

from student import StudentBase
from db import db_delete_student

router = APIRouter()


@router.delete('/student')
def delete_student(student_data: StudentBase):
    try:
        db_delete_student.deleteStudent(student_data)
        return {'msg': 'Deleted student successfully.'}
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail='Student ID is not valid')
    except:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail='Internal server error')
