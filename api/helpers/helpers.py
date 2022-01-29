import random
from flask import make_response, jsonify

def response(data, status, name = None):
    if (name):
        return make_response(jsonify({name: data}), status)
    
    return make_response(jsonify(data), status)

def item_not_found_response(item):
    return response(f"{item} does not exist", 404, "error")

def generate_id():
    numbers = [random.randint(0, 9) for _ in range(8)]

    id = int(''.join(map(str, numbers)))

    return id