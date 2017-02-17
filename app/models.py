from app import db


class Global(db.Model):
    __tablename__ = 'global'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), index=True, unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Global %r>' % (self.name)


class Preparation(db.Model):
    __tablename__ = 'preparation'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), index=True, unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Preparation %r>' % (self.name)


class MealType(db.Model):
    __tablename__ = 'mealtype'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), index=True, unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<MealType %r>' % (self.name)


class MainIngredient(db.Model):
    __tablename__ = 'mainingredient'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), index=True, unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Main Ingredient %r>' % (self.name)


class Cuisine(db.Model):
    __tablename__ = "cuisine"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(400), nullable=False)
    global_ = db.Column(db.Integer, db.ForeignKey('global.id'), nullable=False)
    preparation = db.Column(db.Integer, db.ForeignKey('preparation.id'), nullable=False)
    mealtype = db.Column(db.Integer, db.ForeignKey('mealtype.id'), nullable=False)
    main_ingr = db.Column(db.Integer, db.ForeignKey('mainingredient.id'), nullable=False)
    image_filename = db.Column(db.String, default=None, nullable=True)
    image_url = db.Column(db.String, default=None, nullable=True)


    def __init__(self, title, description, global_, preparation, mealtype, main_ingr, image_filename=None, image_url=None):
        self.title = title
        self.description = description
        self.global_ = global_
        self.preparation = preparation
        self.mealtype = mealtype
        self.main_ingr = main_ingr
        self.image_filename = image_filename
        self.image_url = image_url


    def __repr__(self):
        return '<id: {}, title: {}, main ingredient: {}>'.format(self.id, self.title, self.main_ingr)





