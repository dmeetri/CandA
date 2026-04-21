from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from main.schemas import FileRead, FileCreate
from main.database import get_db

router = APIRouter(
    prefix="/files",
    tags=["Files"]
)

@router.post('/', response_model=FileRead)
def create_file(file_in: FileCreate, db: Session = Depends(get_db)):
    pass

@router.get('/', response_model=list[FileRead])
def get_files(db: Session = Depends(get_db)):
    pass

@router.get('/', response_model=FileRead)
def get_file(db: Session = Depends(get_db)):
    pass
