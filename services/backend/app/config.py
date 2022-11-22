import os

class BaseConfig:
    DEBUG = True
    TESTING = False
    SECRET_KEY = "secret"  # new
    

class DevelopmentConfig(BaseConfig):
    pass
class TestingConfig(BaseConfig):
    pass

class ProductionConfig(BaseConfig):
    pass