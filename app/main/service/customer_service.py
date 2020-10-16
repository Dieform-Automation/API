from flask import jsonify 
from app.main import db
from app.main.model.customer import Customer

from ..util.validate import validate

def save_new_customer(data):
    response = validate(data)
    if response: 
        return response # not validated

    customer = Customer.query.filter_by(name=data['name']).first()
    if not customer:
        new_customer = Customer(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            street=data['street'],
            city=data['city'],
            country=data['country'],
            province=data['province'],
            postal_code=data['postal_code'],
            point_of_contact=data['point_of_contact']
        )
        save_changes(new_customer)
        db.session.refresh(new_customer)
        data['id'] = new_customer.id #get id of newly added data
        
        return data, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Customer with the same name already exists. Please update current customer profile.',
        }
        return response_object, 409

def update_customer(id, data):
    response = validate(data)
    if response: 
        return response # not validated

    customer = Customer.query.filter_by(id=id).first()
    if customer:
        for k in data.keys():
            setattr(customer, k, data[k])

        db.session.commit()
        
        return data, 204
    else:
        response_object = {
            'status': 'Not Found',
            'message': 'Customer does not exist.',
        }
        return response_object, 404

def convert_customer_list_to_json(customer_list):
    response_object = []

    for customer in customer_list:
        response_object.append(customer.as_dict())

    return response_object

def get_all_customers():
    all_customers = Customer.query.all()
    return jsonify(convert_customer_list_to_json(all_customers)), 200

def get_a_customer(id):
    return Customer.query.filter_by(id=id).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()