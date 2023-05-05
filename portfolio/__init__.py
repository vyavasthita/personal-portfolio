from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from portfolio.user.user import user_blueprint
from portfolio.profile.profile import profile_blueprint
from portfolio import routes

app.register_blueprint(user_blueprint)
app.register_blueprint(profile_blueprint)