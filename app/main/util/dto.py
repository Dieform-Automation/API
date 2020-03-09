from flask_restplus import Namespace, fields

class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })

class CustomerDto:
    api = Namespace('customer', description='customer related operations')
    customer = api.model('customer', {
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