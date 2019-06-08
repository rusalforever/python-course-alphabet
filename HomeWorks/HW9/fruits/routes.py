from flask_restful import Resource
from flask import jsonify, request
import uuid

FRUITS = [
    {
        'id': uuid.uuid4().hex,
        'name': 'apple',
        'color': 'green'
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'banana',
        'color': 'yellow'
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'strawberry',
        'color': 'red'
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'blueberry',
        'color': 'blue'
    },
]


class Fruits(Resource):
    @staticmethod
    def get():
        return jsonify({
            'status': 'success',
            'fruits': FRUITS
        })

    @staticmethod
    def post():
        response_object = {'status': 'success'}
        post_data = request.get_json()
        FRUITS.append({
            'id': uuid.uuid4().hex,
            'name': post_data.get('name'),
            'color': post_data.get('color')
        })
        response_object['message'] = 'Fruit added!'
        return jsonify(response_object)

    @staticmethod
    def remove_fruit(fruit_id):
        for fruit in FRUITS:
            if fruit['id'] == fruit_id:
                FRUITS.remove(fruit)
                return True
        return False

    @staticmethod
    def put(fruit_id):
        response_object = {'status': 'success'}
        post_data = request.get_json()
        print(fruit_id)
        print(post_data)
        Fruits.remove_fruit(fruit_id)
        FRUITS.append({
            'id': uuid.uuid4().hex,
            'name': post_data.get('name'),
            'color': post_data.get('color')
        })
        response_object['message'] = 'Fruit updated!'
        return jsonify(response_object)

    @staticmethod
    def delete(fruit_id):
        response_object = {'status': 'success'}
        Fruits.remove_fruit(fruit_id)
        response_object['message'] = 'Fruit removed!'
        return jsonify(response_object)
