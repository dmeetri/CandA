import uvicorn

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from api.deps import get_db
from models.user import User
from schemas.user import UserCreate, UserResponse

app = FastAPI()


@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(email=user.email, name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host="127.0.0.1",
        port=8000,
        reload=True,
    )