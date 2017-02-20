from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from app import images
from query_database import get_all_global, get_all_mainingr, get_all_mealtype, get_all_preparation

class AddCuisineForm(FlaskForm):
    title = StringField(u'title', validators=[DataRequired()])
    description = StringField(u'description', validators=[DataRequired()], widget=TextArea())
    global_ = SelectField(u'global', validators=[DataRequired()], coerce=str)
    main_ingr = SelectField(u'global', validators=[DataRequired()], coerce=str)
    preparation = SelectField(u'global', validators=[DataRequired()], coerce=str)
    meal_type = SelectField(u'global', validators=[DataRequired()], coerce=str)
    cuisine_img = FileField(u'image', validators=[FileRequired(), FileAllowed(images, 'Images only!')])

    def __init__(self, *args, **kwargs):
        super(AddCuisineForm, self).__init__(*args, **kwargs)
        self.global_.choices = [(str(item.id), item.name) for item in get_all_global()]
        self.main_ingr.choices = [(str(item.id), item.name) for item in get_all_mainingr()]
        self.meal_type.choices = [(str(item.id), item.name) for item in get_all_mealtype()]
        self.preparation.choices = [(str(item.id), item.name) for item in get_all_preparation()]



