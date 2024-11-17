# from sqlalchemy import Column, DateTime, Float, Integer, String, create_engine
# from sqlalchemy.orm import declarative_base
# import datetime
# engine = create_engine("sqlite:///projects.sqlite")
# Base = declarative_base()
#
#
# class Project(Base):
#     __tablename__ = "project"
#     id = Column(Integer, primary_key=True)
#     name = Column("name", String)
#     price = Column("price", Float)
#     created_date = Column("created_date", DateTime, default=datetime.datetime.utcnow)
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def __repr__(self):
#         return f"{self.id} {self.name} - {self.price}: {self.created_date}"
#
#
# Base.metadata.create_all(engine)

from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime, Date
from sqlalchemy.orm import declarative_base
import datetime

engine = create_engine("sqlite:///projects.sqlite") #nurodom vieta kur db sukurs

Base = declarative_base()


class Project(Base):
    __tablename__ = "project"
    id = Column(Integer, primary_key = True)
    name = Column("name", String)
    price = Column("price", Float)
    created_date = Column("created_date", DateTime, default = datetime.datetime.now )

Base.metadata.create_all(engine)

    def __init__(self, name, price):
        self.name = name
        self.price  = price

    def __str__(self)
        return f"{self.id}, {self.name} - {self.price}: {self.created_date}" #del grazaus spausdinimo