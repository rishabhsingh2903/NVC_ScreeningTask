import threading
import time
import json
from typing import List
from queue import Queue

from .database import SessionLocal
from . import models
from .dataSources import loadFilteredData

task_queue = Queue = Queue()

def taskQueue(taskId:int,filters:str):
    task_queue.put((taskId,filters))

def taskWorker():
    while True:
        taskId,filters = task_queue.get()
        try :
            processTask(taskId,filters)
        finally:
            task_queue.task_done()

def processTask(taskId:int,filters:str):
    db = SessionLocal()
    try:
        task = db.query(models.Task).get(taskId)
        task.status = 'In_Progress'
        db.commit()

        time.sleep(5)

        ExtractedFilters = json.loads(filters)
        rows = loadFilteredData(ExtractedFilters)


        for row in rows:
            data = models.DataRow(task_id=taskId,**row)
            db.add(data)

        time.sleep(2)
        task.status = 'Completed'
        db.commit()

    finally:
        db.close()
    
worker_thread = threading.Thread(target=taskWorker,daemon=True)
worker_thread.start()

    
    