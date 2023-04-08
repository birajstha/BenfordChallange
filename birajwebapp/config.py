import os

class Config:
    """
    A class to store configuration variables for the web application.
    """
    
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')
    """
    A secret key used to securely sign the session cookie and other data. This key should be kept secret.
    """
    
    DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/data')
    """
    A string representing the path to the directory where uploaded data files are stored.
    """
    
    PLOTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/plots')
    """
    A string representing the path to the directory where generated plots are saved.
    """
    
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@benford_db:5432/postgres'
    """
    A string representing the URI of the database to be used by the web application. The default database used here is
    PostgreSQL.

    For running locally use >> SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/postgres'
    """
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    """
    This flag is used to disable the modification tracker of the Flask-SQLAlchemy 
    extension to save memory and improve performance.
    """
