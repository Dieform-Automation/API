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
    part = api.model('part', {
        'id': fields.Integer(required=False, description='id'),
        'customer_id': fields.Integer(required=True, description='id of customer that ordered part'),
        'number': fields.String(required=True, description='part number (internal number used by Dieform)'),
        'name': fields.String(required=True, description='name of part'),
    })

class OrderDto:
    api = Namespace('order', description='order related operations')
    order = api.model('order', {
        'id': fields.Integer(required=False, description='id'),
        'customer_id': fields.Integer(required=True, description='id of the customer for an order'),
        'number': fields.Integer(required=True, description='order number (internal number used by Dieform)'),
    })

class CustomerDto:
    api = Namespace('customer', description='customer related operations')
    customer = api.model('customer', {
        'id': fields.Integer(required=False, description='id'),
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

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })