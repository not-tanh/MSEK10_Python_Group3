import sys
import traceback
import uuid
import random

from faker import Faker

from student import Student
from db.db_create_student import insertStudent

fake = Faker()

try:
    data = []
    for _ in range(int(sys.argv[1])):
        student = Student(
            **{'sid': str(uuid.uuid4()), 'first_name': fake.first_name(), 'last_name': fake.last_name(),
               'email': fake.email(), 'dob': fake.date(), 'hometown': fake.city(),
               'gpa': round(random.uniform(2, 4), 2)}
        )
        data.append(student)
    insertStudent(data)
except:
    traceback.print_exc()
    print('Usage: python data_generator.py <data_count>')
