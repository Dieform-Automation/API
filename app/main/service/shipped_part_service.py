from flask import jsonify

from app.main import db
from app.main.model.shipped_part import ShippedPart

from ..util.validate import validate

def save_new_shipped_part(data):
    response = validate(data)
    
    if response: 
        return response # not validated

    shipped_part = ShippedPart.query.filter_by(part_id=data['part_id'], shipment_id=int(data['shipment_id'])).first()

    if not shipped_part:
        shipped_part = ShippedPart(
            part_id=int(data['part_id']),
            shipment_id=data['shipment_id'],
            quantity=data['quantity'],
            bins=data['bins']
        )
        save_changes(shipped_part)
        db.session.refresh(shipped_part)
        data['id'] = shipped_part.id # get id of newly created data
        
        return data, 201
    else:
        response_object = {
            'status': 'Fail',
            'message': 'Shipped part with that id already exists for the shipment id.',
        }
        return response_object, 409

def convert_shipped_part_list_to_json(shipped_part_list):
    response_object = []

    for part in shipped_part_list:
        response_object.append(part.as_dict())

    return response_object

def get_all_shipped_parts():
    all_shipped_parts = ShippedPart.query.all()
    return jsonify(convert_shipped_part_list_to_json(all_shipped_parts)), 200

def get_shipped_part(id):
    return ShippedPart.query.filter_by(id=id).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()