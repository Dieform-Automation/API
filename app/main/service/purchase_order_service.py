from app.main import db
from app.main.model.purchase_order import PurchaseOrder

from ..util.validate import validate

def save_new_order(data):
    response = validate(data)
    if response: 
        return response # not validated

    order = PurchaseOrder(
        customer_id=int(data['customer_id']),
        number=int(data['number']),
    )

    try:
        save_changes(order)
        db.session.refresh(order)
        data['id'] = order.id # get id of newly added data
        
        response_object = {
            'status': 'Success',
            'message': 'Successfully added order.',
            'data': data
        }
        return response_object, 201
    except:
        response_object = {
            'status': 'Fail',
            'message': 'Failed to create order. Internal server error.',
        }
        return response_object, 500

def get_all_orders():
    orders = PurchaseOrder.query.all()
    response_object = {'orders': []}

    for order in orders:
        response_object['orders'].append(create_purchase_order_json(order))

    return response_object, 200

def get_an_order(id):    
    purchase_order = PurchaseOrder.query.filter_by(id=id).first()
    
    if purchase_order:
        part_order = create_purchase_order_json(purchase_order)
        return part_order, 200
    
    return None

def get_all_purchase_orders_by_customerID(customer_id):
    return PurchaseOrder.query.filter_by(customer_id=customer_id).all()

def get_all_parts_by_order_number(order_number):
    purchase_order = PurchaseOrder.query.filter_by(number=order_number).first()
    response_object = {'parts': purchase_order.parts}
    
    return response_object, 200

# ----helpers
def create_purchase_order_json(purchase_order):
    return {
        'id': purchase_order.id,
        'customer_id': purchase_order.customer_id,
        'number': purchase_order.number,
        'parts': get_all_parts_from_purchase_order(purchase_order.parts)
    }

def get_all_parts_from_purchase_order(parts):
    all_parts = []
    for part in parts:
        all_parts.append(part.as_dict())
    
    return all_parts

def save_changes(data):
    db.session.add(data)
    db.session.commit()