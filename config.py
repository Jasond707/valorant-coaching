import os

class Config:
    # Retrieve the DATABASE_URL environment variable if set, otherwise fall back to a local SQLite database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///local.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False