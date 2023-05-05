from portfolio import db
from portfolio.user.models import UserRegister


class UserDao:
    def __init__(self) -> None:
        self.db = db

    def create_user(self, username, email, password):
        user = UserRegister(username=username, email=email)
        user.set_password(password=password)
        db.session.add(user)
        db.session.commit()


user_dao = UserDao()