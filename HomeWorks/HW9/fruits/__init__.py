from flask import Blueprint
from flask_restful import Api
from fruits.routes import Fruits

fruits = Blueprint("fruits", __name__)
api_fruits = Api(fruits)

api_fruits.add_resource(Fruits, "/fruits", "/fruits/<string:fruit_id>")
