from portfolio import db
from werkzeug.security import generate_password_hash, check_password_hash

class UserRegister(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text)
    email = db.Column(db.Text, unique=True)
    password_hash = db.Column(db.Text)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)