from app import db
from models import Global, Preparation, MainIngredient, MealType, Cuisine



def get_all_global():
    items = db.session.query(Global).all()
    return items

def get_all_preparation():
    items = db.session.query(Preparation).all()
    return items

def get_all_mealtype():
    items = db.session.query(MealType).all()
    return items

def get_all_mainingr():
    items = db.session.query(MainIngredient).all()
    return items

def addCuisine(title, description, global_, preparation, meal_type, main_ingr, filename, url):
    cuisine = Cuisine(title=title, description=description, global_=global_, preparation=preparation,
                      mealtype=meal_type, main_ingr=main_ingr, image_filename=filename, image_url=url)
    db.session.add(cuisine)
    db.session.commit()
