import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('WTT_SECRET_KEY') or 'WANTTOTRADE'

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass

class DevelConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,
                                                         'wtt-devel.sqlite')
    print(SQLALCHEMY_DATABASE_URI)

class ProductionConfig(Config):
    SQLACHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,
                                                         'wtt-prod.sqlite')

config = {
    'development': DevelConfig,
    'production': ProductionConfig,

    'default': DevelConfig
}
