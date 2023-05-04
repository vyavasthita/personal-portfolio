import os


base_dir = os.path.abspath(os.path.dirname(__name__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'mysecret'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'sqlite:///' + os.path.join(base_dir, 'portfolio.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False