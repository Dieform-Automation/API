from app.main import db
from app.main.model.received_part import ReceivedPart

from ..util.validate import validate

def save_new_received_part(data):
    response = validate(data)
    
    if response: 
        return response # not validated

    received_part = ReceivedPart(
        part_id=int(data['part_id']),
        receiving_order_id=data['receiving_order_id'],
        part_quantity=data['part_quantity'],
        bins=data['bins']
    )

    save_changes(received_part)
    db.session.refresh(received_part)
    data['id'] = received_part.id # get id of newly created data    
    response_object = {
        'status': 'Success',
        'message': 'Successfully added new received part.',
        'data': data
    }
    return response_object, 201
    
def save_changes(data):
    db.session.add(data)
    db.session.commit()