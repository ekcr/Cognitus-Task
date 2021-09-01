from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Data (Base):
    __tablename__='article_textdata'
    id = Column(Integer, primary_key=True, index=True)
    text  = Column (String ,unique=True, index=True) 
    label = Column (String ,unique=True, index=True)

