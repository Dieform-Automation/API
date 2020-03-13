from app.main import db
from app.main.model.part import Part

def save_new_part(data):
    part = Part.query.filter_by(number=data['number'], customer_id=int(data['customer_id'])).first()
    
    if not part:
        part = Part(
            customer_id=int(data['customer_id']),
            number=data['number'],
            name=data['name']
        )
        save_changes(part)
        db.session.refresh(part)
        data['id'] = part.id #get id of newly added data
        response_object = {
            'status': 'success',
            'message': 'Successfully added part.',
            'data': data
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Part for the same customer already exists. Please update current customer parts.',
        }
        return response_object, 409

def get_all_parts():
    return Part.query.all()

def get_all_parts_by_customerID(id):
    parts = Part.query.filter_by(customer_id=id).all()
    return parts

def get_a_part(id):
    return Part.query.filter_by(id=id).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()