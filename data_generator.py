import sys
import traceback
import random

from faker import Faker

from student import Student
from db.db_create_student import insertStudent

fake = Faker()

try:
    for _ in range(int(sys.argv[1])):
        while True:
            try:
                student = Student(
                    **{'sid': f'MSE{random.randint(1, 10000)}', 'first_name': fake.first_name(), 'last_name': fake.last_name(),
                       'email': fake.email(), 'dob': fake.date(), 'hometown': fake.city(),
                       'gpa': round(random.uniform(2, 4), 2)}
                )
                insertStudent(student)
                break
            except:
                print('Duplicated ID. Try different ID')

except:
    traceback.print_exc()
    print('Usage: python data_generator.py <data_count>')
