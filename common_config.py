import os

from name import app_name

#  from datetime import timedelta

SECRET_KEY = 'iQfPvB6sZaNHqVFI5CJa9rM1xOEVHKIM0LwifT04yLsPlZhSSvaDuZXOgJFSpJVq'
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


class Config:
    NAME = app_name
    API_TITLE = 'BSidesNS'
    API_VERSION = '0'
    PROJECT_ROOT = PROJECT_ROOT
    DEBUG = False
    SECURITY_PASSWORD_SALT = 'tilda'
    SECRET_KEY = SECRET_KEY
    SECURITY_TRACKABLE = False
    JWT_SECRET_KEY = SECRET_KEY
    JWT_TOKEN_LOCATION = ['cookies']
    JWT_ACCESS_COOKIE_PATH = '/api/v0'
    JWT_REFRESH_COOKIE_PATH = '/api/v0/auth/refresh'
    JWT_SESSION_COOKIE = False
    JWT_COOKIE_SECURE = True
    #  JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=1)
    #  JWT_REFRESH_TOKEN_EXPIRES = timedelta(seconds=10)
    OPENAPI_URL_PREFIX = '/doc'
    OPENAPI_REDOC_PATH = '/redoc'
    OPENAPI_SWAGGER_UI_PATH = '/swaggerui'
    OPENAPI_SWAGGER_UI_URL = '/static/swaggerui/'
    OPENAPI_VERSION = '2.0.0'
    MEDIA_URL = '/media'
    MEDIA_PATH = f'{PROJECT_ROOT}/media'
    ACCOUNT_REQUEST_EXPIRY = 24  # in hours
    PASSWORD_RESET_EXPIRY = 2  # in hours
    DATABASE = {
        'name': 'database.db',
        'engine': 'SqliteDatabase',
    }
    MAIL = {
        #  'host': 'mail.example.com',
        #  'port': 587,
        #  'ssl': True,
        #  'username': 'someone@example.com',
        #  'password': 'Sekrit',
    }
    FROM_EMAIL = 'office@bsidesns.org'
    SUBJECTS = {
        'prefix': '[BSidesNS] ',
        'confirm': 'Account confirmation',
        'register': 'Account registration',
    }

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DEBUG = True
    JWT_COOKIE_SECURE = False
    SECURITY_SEND_REGISTER_EMAIL = False


class TestConfig(Config):
    TESTING = True
    JWT_COOKIE_SECURE = False
    DATABASE = {
        'name': 'test.db',
        'engine': 'SqliteDatabase',
    }


class ProdConfig(Config):
    pass
