from flask import jsonify

from app.main import db
from app.main.model.part import Part

from ..util.validate import validate

def save_new_part(data):
    response = validate(data)
    
    if response: 
        return response # not validated
    
    part = Part.query.filter_by(number=data['number'], customer_id=int(data['customer_id'])).first()
    
    if not part:
        part = Part(
            customer_id=int(data['customer_id']),
            purchase_order_id=data['purchase_order_id'],
            number=data['number'],
            name=data['name']
        )
        save_changes(part)
        db.session.refresh(part)
        data['id'] = part.id # get id of newly created data

        return data, 201
    else:
        response_object = {
            'status': 'Fail',
            'message': 'Part for the same customer already exists.',
        }
        return response_object, 409

def update_part(id, data):
    response = validate(data)
    if response: 
        return response # not validated
    part = Part.query.filter_by(id=id).first()
    if part:
        part.name=data['name']
        db.session.commit()
        return data, 204
    else:
        response_object = {
            'status': 'Not Found',
            'message': 'Part does not exist.',
        }
        return response_object, 404

def convert_part_list_to_json(part_list):
    response_object = []

    for part in part_list:
        response_object.append(part.as_dict())

    return jsonify(response_object)

def get_all_parts():
    all_parts = Part.query.all()
    return convert_part_list_to_json(all_parts), 200

def get_all_parts_by_customerID(id):
    all_parts = Part.query.filter_by(customer_id=id).all()
    return convert_part_list_to_json(all_parts), 200

def get_a_part(id):
    return Part.query.filter_by(id=id).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()