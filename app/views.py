from app import app, images
from flask import render_template, request, url_for, redirect
from forms import AddCuisineForm
from query_database import get_all_preparation, get_all_global, get_all_mealtype, get_all_mainingr, addCuisine



@app.route('/')
@app.route('/index')
def index():
    global_ = get_all_global()
    preparation = get_all_preparation()
    meal_type = get_all_mealtype()
    main_ingr = get_all_mainingr()

    return render_template('index.html',
                           global_ = global_,
                           preparation = preparation,
                           meal_type = meal_type,
                           main_ingr = main_ingr)


@app.route('/addcuisine', methods= ['GET', 'POST'])
def add_cuisine():
    form = AddCuisineForm()
    if request.method == 'POST':
        print "Hello"
        if form.validate_on_submit():
            print form.errors
            filename = images.save(request.files['cuisine_img'])
            url = images.url(filename)
            addCuisine(form.title.data, form.description.data, int(form.global_.data),
                       int(form.preparation.data), int(form.meal_type.data), int(form.main_ingr.data),
                       filename, url)

            return redirect(url_for('index'))



    return render_template('addcuisine.html',
                           form =form)
