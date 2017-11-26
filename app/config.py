from flask_env import MetaFlaskEnv

class BaseConf(MetaFlaskEnv):
    pass

class DevConf(BaseConf):
    DEBUG = True

class ProdConf(BaseConf):
    DEBUG = False

class TestConf(BaseConf):
    DEBUG = True
    TESTING = True

config = {
    'development': DevConf,
    'testing': TestConf,
    'production': ProdConf,

    'default': DevConf
}
