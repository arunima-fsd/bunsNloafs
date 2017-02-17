from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Global, Preparation, MealType, MainIngredient, Base

engine = create_engine('sqlite:///test.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

global1 = Global(name='Asian')
session.add(global1)
session.commit()

global2 = Global(name='Indian')
session.add(global2)
session.commit()

global3 = Global(name='Mexican')
session.add(global3)
session.commit()

global4 = Global(name='French')
session.add(global4)
session.commit()

global5 = Global(name='Italian')
session.add(global5)
session.commit()


preparation1 = Preparation(name='Baking')
session.add(preparation1)
session.commit()

preparation2 = Preparation(name='Roasting')
session.add(preparation2)
session.commit()

preparation3 = Preparation(name='Grilling')
session.add(preparation3)
session.commit()

preparation4 = Preparation(name='Microwave')
session.add(preparation4)
session.commit()

preparation5 = Preparation(name='Deep fry')
session.add(preparation5)
session.commit()

preparation6 = Preparation(name='Broil')
session.add(preparation6)
session.commit()



mealtype1 = MealType(name='Appetizers')
session.add(mealtype1)
session.commit()

mealtype2 = MealType(name='Breakfast & Brunch')
session.add(mealtype2)
session.commit()

mealtype3 = MealType(name='Desserts')
session.add(mealtype3)
session.commit()

mealtype4 = MealType(name='Main Course')
session.add(mealtype4)
session.commit()

mealtype5 = MealType(name='Beverage')
session.add(mealtype5)
session.commit()

mealtype6 = MealType(name='Snacks')
session.add(mealtype6)
session.commit()



mainigr1 = MainIngredient(name='Apple')
session.add(mainigr1)
session.commit()


mainigr2 = MainIngredient(name='Beans')
session.add(mainigr2)
session.commit()

mainigr3 = MainIngredient(name='Beef')
session.add(mainigr3)
session.commit()

mainigr4 = MainIngredient(name='Cheese')
session.add(mainigr4)
session.commit()

mainigr5 = MainIngredient(name='Chicken')
session.add(mainigr5)
session.commit()

mainigr6 = MainIngredient(name='Eggs')
session.add(mainigr6)
session.commit()

mainigr7 = MainIngredient(name='Fish')
session.add(mainigr7)
session.commit()

mainigr8 = MainIngredient(name='Rice')
session.add(mainigr8)
session.commit()

mainigr9 = MainIngredient(name='Noodles')
session.add(mainigr9)
session.commit()

mainigr10 = MainIngredient(name='Potatoes')
session.add(mainigr10)
session.commit()

mainigr11 = MainIngredient(name='Pumpkin')
session.add(mainigr11)
session.commit()

mainigr12 = MainIngredient(name='Turkey')
session.add(mainigr12)
session.commit()


































