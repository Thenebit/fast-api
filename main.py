# This act as the main entry point of where every comes together
from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated, List
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
import models

app = FastAPI()

# Pydantic to validate data
class StudentBase(BaseModel):
    name: str
    email: str

class StudentModel(StudentBase):
    id: int

    class Config:
        orm_mode = True


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependecy = Annotated[Session, Depends(get_db)]

models.Base.metadata.create_all(bind=engine)

@app.post("/students/", response_model=StudentModel)
async def create_student(student: StudentBase, db: db_dependecy):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


#@app.get("/students/{student_id}", response_model=List[StudentModel])
@app.get("/students/{student_id}", response_model=StudentModel)
async def read_student(student_id: int, db: db_dependecy):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail='Student not found')
    return student