from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Universe(Base):
    #universe related information
    __tablename__ = 'universe'
    universe_id = Column(String(100), primary_key=True)

class Family(Base):
    #family related information
    __tablename__ = 'family'
    family_id = Column(String(100), primary_key=True)


class Person(Base):
    #person related information
    __tablename__ = 'person'
    person_id = Column(String(100), primary_key=True)
    power = Column(Integer)
    universe_id = Column(String(100), ForeignKey(Universe.universe_id))
    family_id = Column(String(100), ForeignKey(Family.family_id))


