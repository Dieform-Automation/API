from datetime import date
from flask import jsonify

from app.main import db
from app.main.model.receiving_order import ReceivingOrder
from app.main.service.received_part_service import save_new_received_part
from app.main.service.part_service import get_a_part

from ..util.validate import validate

def save_new_receiving_order(data):
    response = validate(data)
    
    if response: 
        return response # not validated

    receivable = ReceivingOrder.query.filter_by(customer_packing_slip=data['customer_packing_slip'], customer_id=int(data['customer_id'])).first()

    if not receivable:
        receivable = ReceivingOrder(
            customer_id=int(data['customer_id']),
            customer_packing_slip=data['customer_packing_slip'],
        )

        if 'date' in data.keys(): # since date is optional
            try:
                receivable.date = date.fromisoformat(data['date'])
            except:
                response_object = {
                    'status': 'Fail',
                    'message': 'Invalid date format. Must be a string with format: month/day/year hour:minute:second',
                }
                return response_object, 400
        
        save_changes(receivable)
        db.session.refresh(receivable)
        data['id'] = receivable.id # get id of newly created data
        data['date'] = receivable.date # get date of newly created data (when date is generated by db)

        received_parts = []

        if 'received_parts' in data.keys():
            received_parts = data['received_parts']

        for part in received_parts:
            received_part = {
                "part_id": part['part_id'],
                "receiving_order_id": receivable.id,
                "part_quantity": part['part_quantity'],
                "bins": part['bins'],
                "customer_id": data['customer_id']
            }
            response = validate(received_part)
    
            if response:
                ReceivingOrder.query.filter_by(id=receivable.id).delete()
                db.session.commit()
                return response # not validated

            save_new_received_part(received_part)
        
        return data, 201
    else:
        response_object = {
            'status': 'Fail',
            'message': 'Receiving order already exists for that customer.',
        }
        return response_object, 409

def update_receiving_order(id, data):
    response = validate(data)
    if response: 
        return response # not validated

    receivable = ReceivingOrder.query.filter_by(id=id).first()
    if receivable and 'customer_packing_slip' in data.keys():
        receivable.customer_packing_slip = data['customer_packing_slip']
        db.session.commit()
        return receivable, 204
    else:
        response_object = {
            'status': 'Not Found',
            'message': 'Receiving order could not be updated.',
        }
        return response_object, 404

def get_all_receiving_orders():
    receiving_orders = ReceivingOrder.query.all()

    return receiving_orders_as_list(receiving_orders)

def create_receiving_order_json(receiving_order):
    return {
        'id': receiving_order.id,
        'customer_id': receiving_order.customer_id,
        'customer_packing_slip': receiving_order.customer_packing_slip,
        'date': receiving_order.date,
        'received_parts': get_all_parts_from_receiving_order(receiving_order.receivedParts)
    }

def get_all_parts_from_receiving_order(received_parts):
    all_parts = []
    for received_part in received_parts:
        received_part_dict = received_part.as_dict()
        
        part = get_a_part(received_part_dict['part_id'])
        received_part_dict['part_number'] = part['number']

        all_parts.append(received_part_dict)

    return all_parts

def get_all_receiving_orders_by_customerID(id):
    receiving_orders = ReceivingOrder.query.filter_by(customer_id=id).all()

    return receiving_orders_as_list(receiving_orders)

def receiving_orders_as_list(receiving_orders):
    response_object = []

    for order in receiving_orders:
        response_object.append(create_receiving_order_json(order))

    return jsonify(response_object), 200

def get_a_receiving_order(id):
    receiving_order = ReceivingOrder.query.filter_by(id=id).first()

    if (not receiving_order):
        response_object = {
            'status': 'Not Found',
            'message': 'No receiving order could be found with id: '+ str(id),
        }
        return response_object, 404

    return create_receiving_order_json(receiving_order), 200

def save_changes(data):
    db.session.add(data)
    db.session.commit()