from time import sleep
from typing import List

from celery import current_task
from sqlalchemy.sql.expression import label
from .celery_app import celery_app
from algorithm import *
from sql_app import crud
from sql_app.database import SessionLocal
from sql_app.schemas import DataBase 
from sql_app.models import Data
from sql_app.database import SessionLocal, engine


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@celery_app.task(acks_late=True)
def test_celery() -> str:

    db = SessionLocal
    
    get_datatext = crud.get_text(db,text='text')
    get_datalabel = crud.get_label(db,label='label')
    
    text = List[get_datatext]
    label = List [get_datalabel]


    training, vectorizer = tfidf(text)
    x_train, x_test, y_train, y_test = train_test_split(training, label, test_size = 0.25, random_state = 0)
    model, accuracy, precision, recall = test_SVM(x_train, x_test, y_train, y_test)
    

    dump_model(model, 'model.pickle',"model")
    dump_model(vectorizer, 'vectorizer.pickle',"vectorizer")
    
    return f"Success"