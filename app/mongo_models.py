from .extensions import mongo

class BarM5(mongo.Document):
    name = mongo.StringField()
