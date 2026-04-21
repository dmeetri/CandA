import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from main.database import get_db
from main.models import FileModel
from main.routes import router as file_router

app = FastAPI()
app.include_router(file_router)


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
