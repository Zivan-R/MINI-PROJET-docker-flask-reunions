# config.py modifié. Remplace l'original
import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
            'SQLALCHEMY_DATABASE_URI',
            'mysql+pymysql://oyokai:123456@localhost/reunions'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', '123456')
