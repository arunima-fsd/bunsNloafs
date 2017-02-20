from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, IMAGES, configure_uploads



#creates the application object (of class Flask)
#Flask uses this argument to determine the root
#  path of the application so that it later can find
#  resource files relative to the location of the application.


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


# Configure the image uploading via Flask-Uploads
images = UploadSet('images', IMAGES)
configure_uploads(app, images)

#to avoid circular import error


from app import views, models