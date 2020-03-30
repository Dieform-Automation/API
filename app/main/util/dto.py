from flask_restplus import Namespace, fields

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
        'number': fields.String(required=True, description='part number (internal number used by Dieform)'),
        'name': fields.String(required=True, description='name of part'),
    })

    part_post = api.model('part_post', {
        'customer_id': fields.Integer(required=True, description='id of customer that ordered part'),
        'number': fields.String(required=True, description='part number (internal number used by Dieform)'),
        'name': fields.String(required=True, description='name of part'),
    })

    part_put = api.model('part_put', {
        'name': fields.String(required=True, description='update name of part'),
    })

class OrderDto:
    api = Namespace('order', description='order related operations')
    order_get = api.model('order_get', {
        'id': fields.Integer(required=True, description='id'),
        'customer_id': fields.Integer(required=True, description='id of the customer for an order'),
        'number': fields.Integer(required=True, description='order number (internal number used by Dieform)'),
        'part_map': fields.Raw(required=False, description='part ids mapped to their quantity')
    })
    
    order_post = api.model('order_post', {
        'customer_id': fields.Integer(required=True, description='id of the customer for an order'),
        'number': fields.Integer(required=True, description='order number (internal number used by Dieform)'),
        'part_map': fields.Raw(required=False, description='part ids mapped to their quantity')
    })

    order_put = api.model('order_put', {
        'part_map': fields.Raw(required=True, description='part ids mapped to their quantity')
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

class ReceivingDto:
    api = Namespace('receiving', description='receiving related operations')
    receiving_get = api.model('receiving_get', {
        'id': fields.Integer(required=True, description='id'),
        'customer_id': fields.Integer(required=True, description='id of the customer for an order'),
        'part_id': fields.Integer(required=True, description='id of the part for an order'),
        'customer_packing_slip': fields.String(required=True, description='customer packing slip'),
        'part_quantity': fields.Integer(required=True, description='number of parts in the order'),
        'date': fields.Date(required=True, description='receiving date'),
    })

    receiving_post = api.model('receiving_post', {
        'customer_id': fields.Integer(required=True, description='id of the customer for an order'),
        'part_id': fields.Integer(required=True, description='id of the part for an order'),
        'customer_packing_slip': fields.String(required=True, description='customer packing slip'),
        'part_quantity': fields.Integer(required=True, description='number of parts in the order'),
        'date': fields.Date(required=False, description='receiving date'),
    })

    receiving_put = api.model('receiving_put', {
        'customer_id': fields.Integer(required=False, description='id of the customer for an order'),
        'part_id': fields.Integer(required=False, description='id of the part for an order'),
        'customer_packing_slip': fields.String(required=False, description='customer packing slip'),
        'part_quantity': fields.Integer(required=False, description='number of parts in the order'),
        'date': fields.Date(required=False, description='receiving date'),
    })

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })