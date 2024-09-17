import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    
    # Use the DATABASE_URL environment variable for Heroku Postgres
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
