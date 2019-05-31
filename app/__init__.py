from flask import Flask
from config import config
from app.extensions import db, bootstrap, mongo


def app_create(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
    mongo.init_app(app)
    # 注册蓝本，在此添加
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # 路由和其他处理程序定义
    # ...
    return app
