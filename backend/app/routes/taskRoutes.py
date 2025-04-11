from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import uuid4
from typing import List
import json

from .. import schemas, models
from ..database import SessionLocal
from ..tasks import taskQueue

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.TaskSummary)
def createTask(task: schemas.TaskInfo,db:Session = Depends(get_db)):
    filtersJson = json.dumps(task.model_dump())
    dbTask = models.Task(status="pending", filters=filtersJson)
    db.add(dbTask)
    db.commit()
    db.refresh(dbTask)

    taskQueue(dbTask.id,filtersJson)

    return dbTask

@router.get("/{task_id}/data",response_model = List[schemas.TaskData])
def getTaskData(task_id:int,db:Session = Depends(get_db)):
    task = db.query(models.Task).get(task_id)

    if not task:
        raise HTTPException(status_code=404,detail="Task not found")
    
    return db.query(models.DataRow).filter(models.DataRow.task_id == task_id).all()

    if task.status != "completed":
        raise HTTPException(status_code=400,detail="Task is not completed")
    
    data = db.query(models.DataRow).filter(models.DataRow.task_id == task_id).all()
    return data
    

