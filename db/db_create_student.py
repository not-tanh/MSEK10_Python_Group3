import sqlite3

from config import DB_PATH
from student import Student


def insertStudent(s: Student):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            'INSERT INTO student '
            '(sid, last_name, first_name, email, dob, hometown, gpa) '
            'VALUES (?, ?, ?, ?, ?, ?, ?)',
            (s.sid, s.last_name, s.first_name,
             s.email, str(s.dob), s.hometown, s.gpa)
        )
        conn.commit()
