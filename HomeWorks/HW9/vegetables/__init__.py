from flask import Blueprint
from flask_restful import Api
from vegetables.routes import Vegetables

vegetables = Blueprint("vegetables", __name__)
api_vegetables = Api(vegetables)

api_vegetables.add_resource(Vegetables, "/vegetables", "/vegetables/<string:vegetable_id>")
