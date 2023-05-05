from portfolio import db


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    address = db.Column(db.Text)
    email = db.Column(db.Text, unique=True)
    phone = db.Column(db.Text, unique=True)
    about_me = db.Column(db.Text)
    dob = db.Column(db.DateTime)
