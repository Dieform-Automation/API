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
        parts_for_order = dict(data['part_map'])

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
    return Order.query.all()

def get_an_order(id):
    return Order.query.filter_by(id=id).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()