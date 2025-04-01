from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import uuid4

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
    

