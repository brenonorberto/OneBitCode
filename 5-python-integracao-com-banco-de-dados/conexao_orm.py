from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

user = 'postgres'
password = 'br211201'
host = 'localhost'
database = 'blog'

DATABASE_URL = f'postgresql://{user}:{password}@{host}/{database}'

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()