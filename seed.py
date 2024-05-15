"""Seed file to make sample data for blogly db."""

from models import User, db
from app import app


db.drop_all()
db.create_all()


User.query.delete()


John_Smith = User(first_name='John', last_name="Smith")
Jackie_Smith = User(first_name='Jackie', last_name="Smith")
Harley_Quinn = User(first_name='Harley', last_name="Quinn")


db.session.add(John_Smith)
db.session.add(Jackie_Smith)
db.session.add(Harley_Quinn)


db.session.commit()
