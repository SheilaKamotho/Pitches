import os

class Config:
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://sheila:kamo2211@localhost/pitchy'
    SECRET_KEY='SECRET_KEY'

class ProdConfig(Config):
    '''
    Pruduction  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
