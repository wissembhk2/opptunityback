from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

sql_database_url = "postgresql://postgres:postgres@localhost:5432/opptunity"
engine = create_engine(sql_database_url)
sessionLocal = sessionmaker(autocommit=False, bind=engine)
base = declarative_base()


def create_db():
    try:
        base.metadata.create_all(bind=engine)
        print("Tables created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")