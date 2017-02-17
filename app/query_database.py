from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Global, Preparation, MealType, MainIngredient


engine = create_engine('sqlite:///test.db')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()


def get_all_global():
    items = session.query(Global).all()
    return items

def get_all_preparation():
    items = session.query(Preparation).all()
    return items

def get_all_mealtype():
    items = session.query(MealType).all()
    return items

def get_all_mainingr():
    items = session.query(MainIngredient).all()
    return items

