from flask import request
from flask_restplus import Resource

from ..util.dto import CustomerDto
from ..util.decorator import crossdomain, token_required # will be used later
from ..service.customer_service import get_all_customers, get_a_customer, save_new_customer, update_customer

from flask_cors import cross_origin

api = CustomerDto.api
_get_customer = CustomerDto.customer_get
_post_customer = CustomerDto.customer_post
_put_customer = CustomerDto.customer_put

@api.route('/')
class CustomerList(Resource):
    @api.doc('list_of_customers')
    @crossdomain(origin='*')
    @api.marshal_list_with(_get_customer, envelope='data')
    def get(self):
        """List all customers"""
        return get_all_customers()

    @api.response(201, 'Customer successfully added.')
    @api.doc('add a new customer')
    @crossdomain(origin='*')
    @api.expect(_post_customer, validate=True)
    def post(self):
        """Creates a new customer """
        data = request.json
        return save_new_customer(data=data)


@api.route('/<id>')
@api.param('id', 'The Customer id')
@api.response(404, 'Customer not found.')
class Customer(Resource):
    @api.doc('get a customer')
    @crossdomain(origin='*')
    @api.marshal_with(_get_customer)
    def get(self, id):
        """get a customer given its id"""
        customer = get_a_customer(id)
        if not customer:
            api.abort(404)
        else:
            return customer

    @api.response(204, 'Successfully updated customer.')
    @api.doc('update a customer')
    @crossdomain(origin='*')
    @api.expect(_put_customer, validate=True)
    def put(self, id):
        """Updates a part """
        data = request.json
        return update_customer(id, data=data)