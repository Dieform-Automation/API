from flask import request
from flask_restplus import Resource

from ..util.dto import ReceivingDto
from ..util.decorator import crossdomain, token_required # will be used later
from ..service.receiving_service import get_all_receiving, get_all_receiving_by_customerID, save_new_receiving_order, get_a_receiving_order, update_receiving_order

api = ReceivingDto.api
_post_receiving = ReceivingDto.receiving_post
_get_receiving = ReceivingDto.receiving_get
_put_receiving = ReceivingDto.receiving_put

@api.route('/')
class ReceivingList(Resource):
    @api.doc('list_of_receiving')
    @crossdomain(origin='*')
    @api.marshal_list_with(_get_receiving, envelope='data')
    def get(self):
        """List all receiving"""
        customer_id = request.args.get('customer_id', None)
        if customer_id:
            return get_all_receiving_by_customerID(int(customer_id))
        else:
            return get_all_receiving()

    @api.response(201, 'Receivable order successfully added.')
    @api.doc('add a new receivable order')
    @crossdomain(origin='*')
    @api.expect(_post_receiving, validate=True)
    def post(self):
        """Creates a new receiving order """
        data = request.json
        return save_new_receiving_order(data=data)

@api.route('/<id>')
@api.param('id', 'The receiving order id')
@api.response(404, 'Receivable not found.')
class Receivable(Resource):
    @api.doc('get a receivable order')
    @crossdomain(origin='*')
    @api.marshal_with(_get_receiving)
    def get(self, id):
        """get a receivable order given its id"""
        receivable = get_a_receiving_order(id)
        if not receivable:
            api.abort(404)
        else:
            return receivable

    @api.response(204, 'Successfully updated receivable order.')
    @api.doc('update a receivable order')
    @crossdomain(origin='*')
    @api.expect(_put_receiving, validate=True)
    def put(self, id):
        """Updates a receivable order """
        data = request.json
        return update_receiving_order(id, data=data)