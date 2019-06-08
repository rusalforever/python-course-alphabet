from flask_restful import Resource
from flask import jsonify, request
import uuid

VEGETABLES = [
    {
        'id': uuid.uuid4().hex,
        'name': 'carrot',
        'color': 'orange'
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'tomato',
        'color': 'red'
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'cucumber',
        'color': 'green'
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'cauliflower',
        'color': 'various'
    },
]


class Vegetables(Resource):
    @staticmethod
    def get():
        return jsonify({
            'status': 'success',
            'vegetables': VEGETABLES
        })

    @staticmethod
    def post():
        response_object = {'status': 'success'}
        post_data = request.get_json()
        VEGETABLES.append({
            'id': uuid.uuid4().hex,
            'name': post_data.get('name'),
            'color': post_data.get('color')
        })
        response_object['message'] = 'Vegatable added!'
        return jsonify(response_object)

    @staticmethod
    def remove_vegetable(vegetable_id):
        for vegetable in VEGETABLES:
            if vegetable['id'] == vegetable_id:
                VEGETABLES.remove(vegetable)
                return True
        return False

    @staticmethod
    def put(vegetable_id):
        response_object = {'status': 'success'}
        post_data = request.get_json()
        print(vegetable_id)
        print(post_data)
        Vegetables.remove_vegetable(vegetable_id)
        VEGETABLES.append({
            'id': uuid.uuid4().hex,
            'name': post_data.get('name'),
            'color': post_data.get('color')
        })
        response_object['message'] = 'Vegatable updated!'
        return jsonify(response_object)

    @staticmethod
    def delete(vegetable_id):
        response_object = {'status': 'success'}
        Vegetables.remove_vegetable(vegetable_id)
        response_object['message'] = 'Vegatable removed!'
        return jsonify(response_object)
