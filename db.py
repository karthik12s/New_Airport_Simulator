

from sqlalchemy import create_engine,Column,Integer,String,Sequence
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
URL = f'{os.getenv("db_conn_string", "postgresql://postgres:postgres@localhost:5432/airport_db")}'
print(URL,type(URL))
engine = create_engine(str(URL))

# Session = sessionmaker(bind=engine)
# sesssion = Session()

# Base = declarative_base()

# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer,Sequence("user_id"),primary_key = True)
#     name = Column(String(50))
#     email = Column(String(50))

# # Base.metadata.create_all(engine)
# user1 = User(name =  "A",email = "1@gmail.com")


# sesssion.add_all([user1])
# sesssion.commit()

