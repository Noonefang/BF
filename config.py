class Config:
    # 设置每次请求结束后会自动提交数据库的改动
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 静态方法
    @staticmethod
    def init_app(app):
        pass


# 测试环境
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@192.168.1.104:3306/test'
    MONGOALCHEMY_DATABASE = "Close"
    MONGOALCHEMY_SERVER = "192.168.1.184"
    MONGOALCHEMY_USER = "root"
    MONGOALCHEMY_PASSWORD = "Baofang660"


# 生产环境
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = ""


# 个人开发环境
class FangConfig(Config):
    DEBUG = True
    # mysql
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/test'
    # 查询时显示原始语句
    SQLALCHEMY_ECHO = True
    # mongodb
    MONGOALCHEMY_DATABASE = "Close"
    MONGOALCHEMY_SERVER = "192.168.1.184"
    MONGOALCHEMY_USER = "root"
    MONGOALCHEMY_PASSWORD = "Baofang660"


config = {
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': FangConfig,
}
