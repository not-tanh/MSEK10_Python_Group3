import sqlite3
from typing import Union, List

from config import DB_PATH
from student import StudentBase


def deleteStudent(sid):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            'DELETE FROM student WHERE sid = ?', (sid,)
        )
        conn.commit()
