from app.main.model.received_part import ReceivedPart
from app.main.model.customer import Customer
from app.main.model.part import Part
from app.main.model.purchase_order import PurchaseOrder
from app.main.model.shipment import Shipment

def validate(data):
    for k in data:
        if k == 'customer_id' and not validate_id(Customer, data['customer_id']):
            response_object = {
                'status': 'Fail',
                'message': 'Customer does not exist.',
            }
            return response_object
        
        if k == 'purchase_order_id' and 'customer_id' in data.keys():    

            if (not validate_id(PurchaseOrder, data['purchase_order_id'])):
                response_object = {
                    'status': 'Fail',
                    'message': 'Purchase order does not exist.',
                }
                return response_object

            result = PurchaseOrder.query.filter_by(customer_id=data['customer_id'])
            
            if (not result):
                response_object = {
                    'status': 'Fail',
                    'message': 'Purchase order does not belong to customer.',
                }
                return response_object

        if k == 'part_id' and 'customer_id' in data.keys():
            if (not validate_id(Part, data['part_id'])):
                response_object = {
                    'status': 'Fail',
                    'message': 'Part id does not exist.',
                }
                return response_object

            result = Part.query.filter_by(customer_id=data['customer_id']).first()
            
            if (not result):
                response_object = {
                    'status': 'Fail',
                    'message': 'Part with id '+ str(data['part_id']) + ' does not belong to customer.',
                }
                return response_object

        if k == 'part_id' and not validate_id(Part, data['part_id']):
            response_object = {
                'status': 'Fail',
                'message': 'Part does not exist.',
            }
            return response_object

        if k == 'shipment_id' and not validate_id(Shipment, data['shipment_id']):
            response_object = {
                'status': 'Fail',
                'message': 'Shipment does not exist.',
            }
            return response_object

def validate_id(model, id):
    result = model.query.filter_by(id=id).first()
    if result:
        return True

    return False

def validate_part_customer(customer_id, part_id):
    part = Part.query.filter_by(id=part_id).first()
    return customer_id == part.customer_id