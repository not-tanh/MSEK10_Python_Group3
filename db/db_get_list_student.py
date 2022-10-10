import collections
# import json
import sqlite3

from config import DB_PATH


def getListStudent():
    with sqlite3.connect(DB_PATH) as conn:
        studentList = conn.execute(
            'SELECT * FROM student'
        )
        objects_list = []
        for row in studentList:
            d = collections.OrderedDict()
            d['sid'] = row[1]
            d['last_name'] = row[2]
            d['first_name'] = row[3]
            d['email'] = row[4]
            d['dob'] = row[5]
            d['hometown'] = row[6]
            d['gpa'] = row[7]
            objects_list.append(d)
        # res = json.dumps(objects_list)
        return objects_list
