import sqlite3
from typing import Union, List

from config import DB_PATH
from student import Student


def insertStudent(students: Union[Student, List[Student]]):
    with sqlite3.connect(DB_PATH) as conn:
        if type(students) is Student:
            students = [students]
        conn.executemany(
            'INSERT INTO student '
            '(sid, last_name, first_name, email, dob, hometown, gpa) '
            'VALUES (?, ?, ?, ?, ?, ?, ?)',
            [(s.sid, s.last_name, s.first_name,
             s.email, str(s.dob), s.hometown, s.gpa) for s in students]
        )
        conn.commit()
