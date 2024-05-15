from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)



# MODELS GO BELOW!
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    first_name = db.Column(db.String(50),
                     nullable=False,
                     unique=False)

    last_name = db.Column(db.String(50),
                          nullable=False,
                          unique=False)
    
    DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)

class Post(db.Model):
    __tablename__ = 'posts'

    post_id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    
    content = db.Column(db.Text, nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
# id, like for User
# title
# content
# created_at a date+time that should automatically default to the when the post is created
# a foreign key to the User table

    # created_at = db.Column(
    #     db.DateTime,
    #     nullable=False,
    #     default=datetime.datetime.now)
    


                     


