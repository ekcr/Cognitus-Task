from sqlalchemy.orm import Session

from . import models, schemas


def get_data(db:Session, id : int):
    return db.query(models.Data).filter(models.Data.id == id).first()


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Data).offset(skip).limit(limit).all()


def get_text(db:Session , text:str):
    return db.query(models.Data).filter(models.Data.text == text).all()


def get_label(db:Session , label:str):
    return db.query(models.Data).filter(models.Data.label == label).all()
    