from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Global(Base):
    __tablename__ = 'global'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)


class Preparation(Base):
    __tablename__ = 'preparation'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)

class MealType(Base):
    __tablename__ = 'mealtype'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)

class MainIngredient(Base):
    __tablename__ = 'mainingredient'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)





engine = create_engine('sqlite:///test.db')
Base.metadata.create_all(engine)

