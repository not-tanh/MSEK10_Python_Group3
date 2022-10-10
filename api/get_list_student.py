import sqlite3
import traceback

from fastapi import APIRouter, HTTPException
from fastapi_pagination import Page, add_pagination, paginate

from student import Student
from db import db_get_list_student as DBGetListStudent

router = APIRouter()


@router.get('/getliststudent')
def getListStudent():
    try:
        listStudent = DBGetListStudent.getListStudent()
        return listStudent
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail='Student ID is not valid')
    except:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail='Internal server error')
