from fastapi import FastAPI

from api import create, index

app = FastAPI()

app.include_router(create.router)
app.include_router(index.router)
