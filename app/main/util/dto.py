from flask_restplus import Namespace, fields

received_part = {
    'part_id': fields.Integer,
    'part_quantity': fields.Integer,
    'bins': fields.Integer
}

shipped_part = {
    'part_id': fields.Integer,
    'bins': fields.Integer,
    'quantity': fields.Integer
}

class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })

class PartDto:
    api = Namespace('part', description='part related operations')
    part_get = api.model('part_get', {
        'id': fields.Integer(required=True, description='id'),
        'customer_id': fields.Integer(required=True, description='id of customer that ordered part'),
        'purchase_order_id': fields.Integer(required=True, description='id of the purchase order'),
        'number': fields.String(required=True, description='part number (internal number used by Dieform)'),
        'name': fields.String(required=True, description='name of part'),
    })

    part_post = api.model('part_post', {
        'customer_id': fields.Integer(required=True, description='id of customer that ordered part'),
        'purchase_order_id': fields.Integer(required=True, description='id of purchase order'),
        'number': fields.String(required=True, description='part number (internal number used by Dieform)'),
        'name': fields.String(required=True, description='name of part'),
    })

    part_put = api.model('part_put', {
        'name': fields.String(required=True, description='update name of part'),
    })

class PurchaseOrderDto:
    api = Namespace('purchase_order', description='purchase order related operations')
        
    purchase_order_post = api.model('order_post', {
        'customer_id': fields.Integer(required=True, description='id of the customer for an order'),
        'number': fields.Integer(required=True, description='order number (internal number used by Dieform)'),
    })

class CustomerDto:
    api = Namespace('customer', description='customer related operations')
    customer_get = api.model('customer_get', {
        'id': fields.Integer(required=True, description='id'),
        'name': fields.String(required=True, description='name of the customer'),
        'email': fields.String(required=True, description='customer email'),
        'phone': fields.String(required=True, description='customer phone number'),
        'street': fields.String(required=True, description='customer\'s street (office address)'),
        'city': fields.String(required=True, description='customer\'s city (office address)'),
        'country': fields.String(required=True, description='customer\'s country (office address)'),
        'province': fields.String(required=True, description='customer\'s province (office address)'),
        'postal_code': fields.String(required=True, description='customer\'s postal code (office address)'),
        'point_of_contact': fields.String(required=True, description='name of the point of contact for the customer')
    })

    customer_post = api.model('customer_post', {
        'name': fields.String(required=True, description='name of the customer'),
        'email': fields.String(required=True, description='customer email'),
        'phone': fields.String(required=True, description='customer phone number'),
        'street': fields.String(required=True, description='customer\'s street (office address)'),
        'city': fields.String(required=True, description='customer\'s city (office address)'),
        'country': fields.String(required=True, description='customer\'s country (office address)'),
        'province': fields.String(required=True, description='customer\'s province (office address)'),
        'postal_code': fields.String(required=True, description='customer\'s postal code (office address)'),
        'point_of_contact': fields.String(required=False, description='name of the point of contact for the customer')
    })

    customer_put = api.model('customer_put', {
        'name': fields.String(required=False, description='name of the customer'),
        'email': fields.String(required=False, description='customer email'),
        'phone': fields.String(required=False, description='customer phone number'),
        'street': fields.String(required=False, description='customer\'s street (office address)'),
        'city': fields.String(required=False, description='customer\'s city (office address)'),
        'country': fields.String(required=False, description='customer\'s country (office address)'),
        'province': fields.String(required=False, description='customer\'s province (office address)'),
        'postal_code': fields.String(required=False, description='customer\'s postal code (office address)'),
        'point_of_contact': fields.String(required=False, description='name of the point of contact for the customer')
    })

class ReceivingOrderDto:
    api = Namespace('receiving_order', description='receiving order related operations')
    receiving_order_get = api.model('receiving_order_get', {
        'id': fields.Integer(required=True, description='id'),
        'customer_id': fields.Integer(required=True, description='id of the customer for an order'),
        'customer_packing_slip': fields.String(required=True, description='customer packing slip'),
        'date': fields.Date(required=True, description='receiving date'),
    })

    receiving_order_post = api.model('receiving_order_post', {
        'customer_id': fields.Integer(required=True, description='id of the customer for an order'),
        'customer_packing_slip': fields.String(required=True, description='customer packing slip'),
        'date': fields.Date(required=False, description='receiving date'),
        'received_parts': fields.List(fields.Nested(api.model("received_parts", received_part)))
    })

    receiving_order_put = api.model('receiving_order_put', {        
        'customer_packing_slip': fields.String(required=True, description='customer packing slip'),        
    })

class ReceivedPartDto:
    api = Namespace('received_part', description='received part related operations')
    received_part_post = api.model('received_part_post', {
        'part_id': fields.Integer(required=True, description='id of the part'),
        'receiving_order_id': fields.Integer(required=True, description='id of the receiving order'),   
        'part_quantity': fields.Integer(required=True, description='quantity of part'),   
        'bins': fields.Integer(required=True, description='number of bins'),   
    })

class ShipmentDto:
    api = Namespace('shipment', description='shipment related operations')
    shipment_post = api.model('shipment_post', {
        'date': fields.Date(required=False, description='shipment date'),
        'shipping_method': fields.String(required=True, description='the shipping method'),
        'shipped_parts': fields.List(fields.Nested(api.model("shipped_part", shipped_part)))
    })

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })