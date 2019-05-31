from flask import Flask
from flask_mongoalchemy import MongoAlchemy
app = Flask(__name__)
app.config['MONGOALCHEMY_DATABASE'] = 'Close'
app.config['MONGOALCHEMY_SERVER'] = '192.168.1.184'
app.config['MONGOALCHEMY_USER'] = 'root'
app.config['MONGOALCHEMY_PASSWORD'] = 'Baofang660'
db = MongoAlchemy(app)

class BarM5(db.Document):
    name = db.StringField()
print(BarM5(name="Michael").name)