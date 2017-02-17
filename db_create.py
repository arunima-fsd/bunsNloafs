from app import db
from app.models import Global, Preparation, MealType, MainIngredient

db.create_all()

global1 = Global(name='Asian')
db.session.add(global1)

global2 = Global(name='Indian')
db.session.add(global2)

global3 = Global(name='Mexican')
db.session.add(global3)

global4 = Global(name='French')
db.session.add(global4)

global5 = Global(name='Italian')
db.session.add(global5)

db.session.commit()


preparation1 = Preparation(name='Baking')
db.session.add(preparation1)


preparation2 = Preparation(name='Roasting')
db.session.add(preparation2)


preparation3 = Preparation(name='Grilling')
db.session.add(preparation3)


preparation4 = Preparation(name='Microwave')
db.session.add(preparation4)

preparation5 = Preparation(name='Deep fry')
db.session.add(preparation5)

preparation6 = Preparation(name='Broil')
db.session.add(preparation6)

db.session.commit()


mealtype1 = MealType(name='Appetizers')
db.session.add(mealtype1)


mealtype2 = MealType(name='Breakfast & Brunch')
db.session.add(mealtype2)


mealtype3 = MealType(name='Desserts')
db.session.add(mealtype3)


mealtype4 = MealType(name='Main Course')
db.session.add(mealtype4)


mealtype5 = MealType(name='Beverage')
db.session.add(mealtype5)

mealtype6 = MealType(name='Snacks')
db.session.add(mealtype6)


db.session.commit()


mainigr1 = MainIngredient(name='Apple')
db.session.add(mainigr1)



mainigr2 = MainIngredient(name='Beans')
db.session.add(mainigr2)


mainigr3 = MainIngredient(name='Beef')
db.session.add(mainigr3)


mainigr4 = MainIngredient(name='Cheese')
db.session.add(mainigr4)


mainigr5 = MainIngredient(name='Chicken')
db.session.add(mainigr5)


mainigr6 = MainIngredient(name='Eggs')
db.session.add(mainigr6)


mainigr7 = MainIngredient(name='Fish')
db.session.add(mainigr7)


mainigr8 = MainIngredient(name='Rice')
db.session.add(mainigr8)


mainigr9 = MainIngredient(name='Noodles')
db.session.add(mainigr9)


mainigr10 = MainIngredient(name='Potatoes')
db.session.add(mainigr10)

mainigr11 = MainIngredient(name='Pumpkin')
db.session.add(mainigr11)


mainigr12 = MainIngredient(name='Turkey')
db.session.add(mainigr12)


db.session.commit()
