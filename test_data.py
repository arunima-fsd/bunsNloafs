from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Global, Preparation, MealType, MainIngredient


engine = create_engine('sqlite:///test.db')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()



items = session.query(Global).all()
for item in items:
    print item.name


items = session.query(Preparation).all()
for item in items:
    print item.name


items = session.query(MealType).all()
for item in items:
    print item.name


items = session.query(MainIngredient).all()
for item in items:
    print item.name