import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KET') or 'you-will-never-guess'
