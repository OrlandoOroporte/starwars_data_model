import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__="user"
    id = Column(Integer,primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    

class Planet(Base):
    __tablename__="planet"
    id = Column(Integer,primary_key=True)
    name = Column(String(250),nullable=False,unique=True)
    size = Column(String(250),nullable=False)
    population = Column(String(250),nullable=False)
    surface = Column(String(250),nullable=False)
    

class People(Base):
    __tablename__="people"
    id = Column(Integer, primary_key=True)
    name = Column(String(250),nullable=False,unique=True)
    color_eyes = Column(String(250),nullable=False)
    color_hair = Column(String(250),nullable=False)
    height = Column(String(250),nullable=False)

class Favorites(Base):
    __tablename__="favorites"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey("user.id"))
    people_id = Column(Integer,ForeignKey("people.id"))
    planet_id = Column(Integer,ForeignKey("planet.id"))
    user = relationship(User)


# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')