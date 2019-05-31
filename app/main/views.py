from flask import render_template, jsonify
from ..models import User
from ..mongo_models import BarM5
from . import main


@main.route('/', methods=['GET', 'POST'])
def index(name="BF"):
    return render_template('index.html', name=name)


@main.route('/mysql', methods=['GET', 'POST'])
def sql():
    user = User.query.first()
    return jsonify({"name": user.name, "id": user.id})


@main.route('/mongo', methods=['GET', 'POST'])
def mongo_test():
    user = BarM5(name="Michael")
    return jsonify({"name": user.name})
