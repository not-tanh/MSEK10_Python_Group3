# import collections
# import json
import sqlite3

from config import DB_PATH
from student import Student


def updateStudent(s: Student):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            'UPDATE student set last_name = ?, first_name = ?, email = ?, dob = ?, hometown = ?, gpa = ? where sid = ?',
            (s.last_name, s.first_name,
             s.email, str(s.dob), s.hometown, s.gpa,
             s.sid)
        )
        conn.commit()
        if conn:
            return 'Updated successfully'
        else:
            return 'Updated fail'
