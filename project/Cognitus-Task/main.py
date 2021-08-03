from typing import Optional
from fastapi import FastAPI , Request, requests
from pydantic import BaseModel
from sklearn.preprocessing import data
from .algorithm import *
from article.database import test_read_sql



class Train(BaseModel):
    data : str

app = FastAPI()

@app.get("/train")
async def train():
    text, label = test_read_sql()
    training, vectorizer = tfidf(text)
    x_train, x_test, y_train, y_test = cross_validation.train_test_split(training, label, test_size = 0.25, random_state = 0)
    model, accuracy, precision, recall = test_SVM(x_train, x_test, y_train, y_test)
    dump_model(model, 'model.pickle')
    dump_model(vectorizer, 'vectorizer.pickle')
    return ("***************")


@app.post("/predict")
async def predict(request:Request):
    model = load_model('model.pickle')
    vectorizer = load_model('vectorizer.pickle')
    data = await request.body()
    tdifd = vectorizer.transform([data])
    result = model.predict_proba(tdifd)
    
    return result

    

