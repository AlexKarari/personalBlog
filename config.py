class Config:
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alexander:lazypass@localhost/blog'

config_options ={"production":ProdConfig,"default":DevConfig}

