from app import app
from flask import render_template
import query_database



@app.route('/')
@app.route('/index')
def index():
    global_ = query_database.get_all_global()
    preparation = query_database.get_all_preparation()
    meal_type = query_database.get_all_mealtype()
    main_ingr = query_database.get_all_mainingr()

    return render_template('index.html',
                           global_ = global_,
                           preparation = preparation,
                           meal_type = meal_type,
                           main_ingr = main_ingr)


@app.route('/addcuisine')
def add_cuisine():
    return render_template('addcuisine.html')
