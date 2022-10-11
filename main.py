from fastapi import FastAPI
from fastapi_pagination import add_pagination

from api import index, create_student, get_students, update_student, delete_student

app = FastAPI()

app.include_router(index.router)
app.include_router(create_student.router)
app.include_router(get_students.router)
add_pagination(app)
app.include_router(update_student.router)
app.include_router(delete_student.router)
