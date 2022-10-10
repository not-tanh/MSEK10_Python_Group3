from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()


@router.get('/')
def index():
    return FileResponse('./src/page/index.html')
