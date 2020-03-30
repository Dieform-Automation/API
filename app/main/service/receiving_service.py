import datetime

from app.main import db
from app.main.model.receiving import Receiving

def save_new_receiving_order(data):
    receivable = Receiving.query.filter_by(part_id=data['part_id'], customer_id=int(data['customer_id'])).first()

    if not receivable:
        receivable = Receiving(
            customer_id=int(data['customer_id']),
            part_id=int(data['part_id']),
            customer_packing_slip=data['customer_packing_slip'],
            part_quantity=int(data['part_quantity']),
        )

        if data['date']: # since date is optional
            receivable.date = datetime.datetime.date(data['date'])

        save_changes(receivable)
        db.session.refresh(receivable)
        data['id'] = receivable.id # get id of newly created data
        response_object = {
            'status': 'Success',
            'message': 'Successfully added new receiving order.',
            'data': data
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'Fail',
            'message': 'Receiving order with that part for that customer already exists.',
        }
        return response_object, 409

def update_receiving_order(id, data):
    receiving = Receiving.query.filter_by(id=id).first()
    if receiving:
        for k in data.keys():
            setattr(receiving, k, data[k])

        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully updated receiving order.',
            'data': data
        }
        return response_object, 204
    else:
        response_object = {
            'status': 'Not Found',
            'message': 'Receiving order does not exist.',
        }
        return response_object, 404

def get_all_receiving():
    return Receiving.query.all()

def get_all_receiving_by_customerID(id):
    return Receiving.query.filter_by(customer_id=id).all()

def get_a_receiving_order(id):
    return Receiving.query.filter_by(id=id).first()    

def save_changes(data):
    db.session.add(data)
    db.session.commit()