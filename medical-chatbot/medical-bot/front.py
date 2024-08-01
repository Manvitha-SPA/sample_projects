from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from .schemas import Question
from .database import engine, SessionLocal
from . import models,schemas
# from streamlit import input_text

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Bot(BaseModel):
    question : str

@app.post("/question")
def get_answer(question : schemas.Question, db : Session = Depends(get_db)):
    new_question = models.Question(question = question.question)
    db.add(new_question)
    db.commit()
    db.refresh(new_question)
    return new_question

@app.get('/questions')
def get_all_questions(db: Session = Depends(get_db)):
    questions = db.query(models.Question).all()
    return questions

@app.get('/question/{question_id}')
def get_question_by_id(question_id: int, db: Session = Depends(get_db)):
    question = db.query(models.Question).filter(models.Question.id == question_id).first()
    if question:
        return question
    else:
        raise HTTPException(status_code=404, detail=f"Question with ID {question_id} not found")

@app.delete('/question/{question_id}')
def delete_question(question_id: int, db: Session = Depends(get_db)):
    question = db.query(models.Question).filter(models.Question.id == question_id).first()
    if question:
        db.delete(question)
        db.commit()
        return {"message": f"Question with ID {question_id} has been deleted successfully."}
    else:
        raise HTTPException(status_code=404, detail=f"Question with ID {question_id} not found")
    

