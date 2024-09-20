import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_default_secret_key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://default:9vYLHpDX1WyF@ep-royal-cell-a4yyqmhc-pooler.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require'
    SQLALCHEMY_TRACK_MODIFICATIONS = False