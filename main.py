from fastapi import FastAPI
from fastapi_pagination import add_pagination

from api import create_student, index, get_list_student, update_student, get_list_student_pagination

app = FastAPI()

app.include_router(index.router)
app.include_router(create_student.router)
# app.include_router(get_list_student.router)
app.include_router(get_list_student_pagination.router)
add_pagination(app)
app.include_router(update_student.router)
