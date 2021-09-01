from typing import Optional
from fastapi import FastAPI , Request, requests
from numpy.lib.function_base import vectorize
from pydantic import BaseModel
# from sklearn.preprocessing import data
from algorithm import *
from celery import Celery
import redis
from celery.result import AsyncResult
from fastapi import FastAPI, BackgroundTasks
from work_celery.celery_app import celery_app
import logging
import os

log = logging.getLogger(__name__)

class Train(BaseModel):
    data : str

app = FastAPI()



def celery_on_message(body):
    log.warn(body)

def background_on_message(task):
    log.warn(task.get(on_message=celery_on_message, propagate=False))



@app.get("/train")
async def train():
    if not bool(os.getenv('DOCKER')):
        task_name = "work_celery.celery_worker.test_celery"
    else:
        task_name = "work_celery.celery_worker.test_celery"

    task = celery_app.send_task(task_name)
    
    print(task)
    
    return {"message": "train started"}


@app.post("/predict")
async def predict(request:Request):

    model = load_model('model')
    vectorizer = load_model('vectorizer')

    data = await request.body()
    tdifd = vectorizer.transform([data])
    result = model.predict_proba(tdifd)

    
    return result

    

