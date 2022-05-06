import os

class Config:
    """General configuration parent class
    """
    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    """Production configuration child class

    Args:
        Config (The parent configuration class): with General production configuration settings
    """
    pass

class DevConfig(Config):
    """Devlopment configuration child class

    Args:
        Config (the parent configuration class): with General configuration settngs
    """
    DEBUG =True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}