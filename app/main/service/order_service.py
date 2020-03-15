from app.main import db
from app.main.model.order import Order
from app.main.model.customer import Customer
from app.main.model.part import Part
from app.main.model.part_order import PartOrder

def save_new_order(data):
    order = Order.query.filter_by(number=data['number'], customer_id=int(data['customer_id'])).first()
    customer = Customer.query.filter_by(id=data['customer_id']).first()
    
    if not customer:
        response_object = {
            'status': 'Not Found',
            'message': 'Customer does not exists.',
        }
        return response_object, 404

    if not order:
        parts_for_order = dict(data['part_map']) or []

        # check if parts in order exist
        for part_id in parts_for_order.keys():
            part = Part.query.filter_by(id=int(part_id)).first()
            if not part:
                response_object = {
                'status': 'Not Found',
                'message': 'Part does not exists.',
                }
                return response_object, 404

        order = Order(
            customer_id=int(data['customer_id']),
            number=int(data['number']),
        )
        save_changes(order)
        db.session.refresh(order)
        data['id'] = order.id # get id of newly added data
        
        # populate part_order assoc. with new order id
        for part_id in parts_for_order.keys():
            part_order = PartOrder(
                part_id = part_id,
                order_id = order.id,
                quantity = int(parts_for_order[part_id])
            )
            save_changes(part_order)

        response_object = {
            'status': 'Success',
            'message': 'Successfully added order.',
            'data': data
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'Fail',
            'message': 'Order for the same customer already exists.',
        }
        return response_object, 409

def get_all_orders():
    orders = Order.query.all()
    response_object = {'orders': []}

    for order in orders:
        response_object['orders'].append(create_part_order_json(order))

    return response_object, 200

def get_an_order(id):    
    order = Order.query.filter_by(id=id).first()
    
    if order:
        part_order = create_part_order_json(order)
        return part_order
    
    return None

def get_all_parts_by_orderID(id):
    part_orders = PartOrder.query.filter_by(order_id=id).all()
    parts = {}

    for part in part_orders:
        parts[str(part.part_id)] = part.quantity

    return parts

def get_all_orders_by_customerID(id):
    return Order.query.filter_by(customer_id=id).all()

def update_order(id, data):
    parts = get_all_parts_by_orderID(id)
    new_parts = data['part_map']

    if not new_parts:
        response_object = {
            'status': 'Not Found',
            'message': 'No parts found.',
        }
        return response_object, 404

    for k in new_parts.keys():

        if k in parts and new_parts[k] != parts[k]: # update quantity
            part_order = PartOrder.query.filter_by(order_id=id, part_id=int(k)).first()
            part_order.quantity = new_parts[k]
            db.session.commit()
        elif k not in parts: # create new part-order assoc.
            part_order = PartOrder(
                part_id = int(k),
                order_id = id,
                quantity = int(new_parts[k])
            )
            save_changes(part_order)
        
    for k in parts:
        if k not in new_parts: # remove old parts
            PartOrder.query.filter_by(order_id=id, part_id=int(k)).delete()
            db.session.commit()

    response_object = {
            'status': 'success',
            'message': 'Successfully updated part.',
            'data': data
        }
    return response_object, 204
    

# ----helpers

def create_part_order_json(order):
    return {
        'id': order.id,
        'customer_id': order.customer_id,
        'number': order.number,
        'part_map': get_all_parts_by_orderID(order.id)
    }

def save_changes(data):
    db.session.add(data)
    db.session.commit()