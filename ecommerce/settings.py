from os import environ

from dotenv import load_dotenv

if environ.get('FLASK_ENV'):
    path = '.env' if environ['FLASK_ENV'] != 'test' else '.env.test'    
    load_dotenv(path, override=True)


class Settings:
    SECRET_KEY = environ.get('SECRET_KEY') or 'SECRET'
