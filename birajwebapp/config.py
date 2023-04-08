import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY','dev')
    DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/data')
    PLOTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/plots')
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@benford_db:5432/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
