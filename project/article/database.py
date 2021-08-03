from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas
from databases import Database

def test_read_sql():

    SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/django_app"
    database = Database(SQLALCHEMY_DATABASE_URL)

    engine = create_engine(
        SQLALCHEMY_DATABASE_URL
    )

    database.connect()


    df = pandas.read_sql_query(
        "SELECT * FROM article_textdata",con=engine)
    return df['text'].tolist(), df['label'].tolist()

    