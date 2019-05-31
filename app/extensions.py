# 扩展放入这里
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_mongoalchemy  import MongoAlchemy

mongo = MongoAlchemy()
bootstrap = Bootstrap()
db = SQLAlchemy()
