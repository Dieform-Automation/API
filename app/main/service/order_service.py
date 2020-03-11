from app.main import db
from app.main.model.order import Order

def save_new_order(data):
    order = Order.query.filter_by(number=data['number'], customer_id=int(data['customer_id'])).first()
    
    if not order:
        order = Order(
            customer_id=int(data['customer_id']),
            number=int(data['number']),
        )
        save_changes(order)
        db.session.refresh(order)
        data['id'] = order.id #get id of newly added data
        response_object = {
            'status': 'success',
            'message': 'Successfully added order.',
            'data': data
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Order for the same customer already exists. Please update current customer orders.',
        }
        return response_object, 409

def get_all_orders():
    return Order.query.all()

def get_an_order(id):
    return Order.query.filter_by(id=id).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()