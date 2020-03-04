import os

POSTGRES_URL = os.environ["POSTGRES_URL"]
POSTGRES_USER = os.environ["POSTGRES_USER"]
POSTGRES_PW = os.environ["POSTGRES_PW"]
POSTGRES_DB = os.environ["POSTGRES_DB"]
SSL_MODE = os.environ["POSTGRES_SSL_MODE"]
ROOT_CERT = os.environ["POSTGRES_ROOT_CERT"]
SSL_CERT = os.environ["POSTGRES_SSL_CERT"]
SSL_KEY = os.environ["POSTGRES_SSL_KEY"]

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}?sslmode={ssl_mode}&sslrootcert={root_cert}&sslcert={ssl_cert}&sslkey={ssl_key}'.format(
                user=POSTGRES_USER,
                pw=POSTGRES_PW,
                url=POSTGRES_URL,
                db=POSTGRES_DB,
                ssl_mode=SSL_MODE,
                root_cert=ROOT_CERT,
                ssl_cert=SSL_CERT,
                ssl_key=SSL_KEY)

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = DB_URL
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db') #local db for testing
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = DB_URL


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY