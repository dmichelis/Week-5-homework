from flask import Blueprint, request, jsonify
from car_inventory.helpers import token_required
from car_inventory.models import User, Car, CarSchema, cars_schema, db, car_schema

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return {'some':'value'}


@api.route('/cars', methods = ['POST'])
@token_required
def create_car(current_user_token):
    car_make = request.json['car_make']
    car_model = request.json['car_model']
    car_year = request.json['car_year']
    car_color = request.json['car_color']
    user_token = current_user_token.token

    car = Car(car_make, car_model, car_year, car_color, user_token = user_token)

    db.session.add(car)
    db.session.commit()

    response = car_schema.dump(car)
    return jsonify(response)


@api.route('/cars', methods = ['GET'])
@token_required
def get_cars(current_user_token):
    owner = current_user_token.token
    cars = Car.query.filter_by(user_token = owner).all()
    response = cars_schema.dump(cars)
    return jsonify(response)



@api.route('/cars/<id>', methods = ['GET'])
@token_required
def get_car(current_user_token, id):
    car = Car.query.get(id)
    response = car_schema.dump(car)
    return jsonify(response)


@api.route('/cars/<id>', methods = ['POST', 'PUT'])
@token_required
def update_car(current_user_token, id):
    car = Car.query.get(id)

    car.car_make = request.json['car_make']
    car.car_model = request.json['car_model']
    car.car_year = request.json['car_year']
    car.car_color = request.json['car_color']
    car.user_token = current_user_token.token

    db.session.commit()
    response = car_schema.dump(car)
    return jsonify(response)



@api.route('/cars/<id>', methods = ['DELETE'])
@token_required
def delete_car(current_user_token, id):
    car = Car.query.get(id)
    db.session.delete(car)
    db.session.commit()
    response = car_schema.dump(car)
    return jsonify(response)
