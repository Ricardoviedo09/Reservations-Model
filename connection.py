from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:@localhost/reservation")

Session = sessionmaker(engine)
session = Session()

Base = declarative_base()    