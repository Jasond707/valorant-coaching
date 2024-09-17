import os

class Config:
    # Replace this with your actual Heroku Postgres URL
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://u7u7afd5vrc59s:pbd6e4bcfedc2d38cabc6fff5566268b1e5ea9bbe6a056a7c6a725137464ddef4@c9uss87s9bdb8n.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/dddvu8l8cjo5tb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
