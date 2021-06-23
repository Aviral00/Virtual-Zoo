import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'udacitycloud.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'article-cms'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'aviral9125'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Aviral1403@'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'cloudarticle'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '4ms6vwqmxxsMis3KNCSK4h02l7uI+o82AQeVljhGq/OJzQU6XxmbfWyUoZ93TR8T5rPpaXGZfcTyH8K2Zuj8iQ=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
