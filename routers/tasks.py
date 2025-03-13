# CRUD Task API
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Task
from schemas import TaskCreate, TaskResponse
from database import get_db
from security import get_current_user

router = APIRouter()


@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    new_task = Task(title=task.title, description=task.description, user_id=user.id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@router.get("/", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Task).filter(Task.user_id == user.id).all()


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_task = db.query(Task).filter(Task.id == task_id, Task.user_id == user.id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    db_task.title = task.title
    db_task.description = task.description
    db.commit()
    db.refresh(db_task)
    return db_task


@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_task = db.query(Task).filter(Task.id == task_id, Task.user_id == user.id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(db_task)
    db.commit()
    return {"message": "Task deleted"}
