# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import declarative_base
#
# Base = declarative_base()
#
# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True)
#     username = Column(String)
#     email = Column(String)
#
#     def __repr__(self):
#         return f"<User(id={self.id}, username={self.username}, email={self.email})>"
#
#

from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String, Text, Boolean


# engine = create_engine("sqlite:///european_database.sqlite")
# conn = engine.connect()

# metadate = MetaData()
# division = Table('divisions', metadate, autoload_with=engine)
#
# # print(repr(metadate.tables['divisions']))
# #
# # print(division.columns.keys())
#
# query = division.select()
#
# execution = conn.execute(query)
# # print(execution.fetchone())
# print(execution.fetchall())

engine = create_engine("sqlite:///datacamp.sqlite")
conn = engine.connect()
metadate = MetaData()

Student = Table("Student", metadate,
          Column('Id', Integer(), primary_key=True),
                Column('Name', String(255), nullable=False),
                Column('Major', String(255), default="Math"),
                Column('Pass', Boolean(), default=True)
                )

metadate.create_all(engine)
#
# from sqlalchemy import insert
# query = insert(Student).values(Id=1, Name="Mattew", Major="English", Pass=True)
# print(query)

# execution = conn.execute(query)
# conn.commit()

# query1 = Student.select()
# execution1 = conn.execute(query1)
# print(execution1.fetchall())

# values_list = [
#     {'Id':'2', 'Name':'Nisha', 'Major':"Science", 'Pass':False},
#     {'Id':'3', 'Name':'Natasha', 'Major':"Math", 'Pass':True},
#     {'Id':'4', 'Name':'Ben', 'Major':"English", 'Pass':False}
# ]
#
#
# query = insert(Student).values(values_list)
# print(query)
# execution = conn.execute(query)
# conn.commit()

# query = Student.select().where(Student.columns.Major == "English")
# print(query)
#
# execution = conn.execute(query)
# print(execution.fetchall())

# query = Student.select().where(Student.columns.Pass == True)
# print(query)
#
# print(conn.execute(query).fetchall())

from sqlalchemy import and_, or_

# query = Student.select().where(or_(Student.columns.Major == "English",
#                                     Student.columns.Pass == True))
#
# print(conn.execute(query).fetchall())

# from sqlalchemy import desc
# query = Student.select().order_by(desc(Student.columns.Name))
# print(query)
# print(conn.execute(query).fetchall())
from sqlalchemy import func

# query = Student.select([func.count(Student.columns.Id), Student.columns.Pass]).group_by(Student.columns.Pass)
# print(conn.execute(query).fetchall())

# from sqlalchemy import
# query = Student.select().where(Student.columns.Major.in_(["English", "Math"]))
#
# result = conn.execute(query).fetchall()
# print(result)
#
# import pandas as pd
#
# data = pd.DataFrame(result)
# print(data)

from sqlalchemy import update

# query = Student.update().values(Pass=False).where(Student.columns.Id == "3")
# print(query)
# conn.execute(query)
# conn.commit()

# query = Student.delete().where(Student.columns.Name == "Ben")
# print(query)
# conn.execute(query)
# conn.commit()

metadate.drop_all(engine, [Student])

# from sqlalchemy import create_engine
# from sqlalchemy import MetaData, Table, Column, Integer, String, Text, Boolean
# import sqlalchemy
#
#
# engine = create_engine("sqlite:///european_database.sqlite")
# conn = engine.connect()
#
# metadate = MetaData()
# division = Table('divisions', metadate, autoload_with=engine)
# mathces = Table("matchs", metadate, autoload_with=engine)
#
# from sqlalchemy import join
# query = division.select()
# div_mat = join(division, mathces, division.columns.division == mathces.columns.Div)
#
# query = div_mat.select()
#
# execution = conn.execute(query)
# print(execution.fetchmany(10))

import sqlalchemy as db

# query = db.select([division, mathces]).select_from(division.join(mathces, division.columns.division == mathces.columns.Div))
# print(query)
#
# execution = conn.execute(query)
# print(execution.fetchmany(10))




