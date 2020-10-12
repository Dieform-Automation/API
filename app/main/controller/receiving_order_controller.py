from flask import request
from flask_restplus import Resource

from ..util.dto import ReceivingOrderDto
from ..util.decorator import crossdomain, token_required # will be used later
from ..service.receiving_order_service import get_all_receiving_orders, get_all_receiving_orders_by_customerID, save_new_receiving_order, get_a_receiving_order, update_receiving_order

api = ReceivingOrderDto.api
_post_receiving_order = ReceivingOrderDto.receiving_order_post
_get_receiving_order = ReceivingOrderDto.receiving_order_get
_put_receiving_order = ReceivingOrderDto.receiving_order_put

@api.route('/')
class ReceivingOrderList(Resource):
    @api.doc('list_of_receivingOrder')
    @crossdomain(origin='*')
    def get(self):
        """List all receiving orders"""
        customer_id = request.args.get('customer_id', None)
        if customer_id:
            return get_all_receiving_orders_by_customerID(int(customer_id))
        else:
            return get_all_receiving_orders()

    @api.response(201, 'Receivable order successfully added.')
    @api.doc('add a new receivable order')
    @crossdomain(origin='*')
    @api.expect(_post_receiving_order, validate=True)
    def post(self):
        """Creates a new receiving order """
        data = request.json
        return save_new_receiving_order(data=data)

@api.route('/<id>')
@api.param('id', 'The receiving order id')
@api.response(404, 'Receiving order not found.')
class ReceivingOrder(Resource):
    @api.doc('get a receiving order')
    @crossdomain(origin='*')    
    def get(self, id):
        """get a receiving order given its id"""
        receivable = get_a_receiving_order(id)
        if not receivable:
            api.abort(404)
        else:
            return receivable

    @api.response(204, 'Successfully updated receiving order.')
    @api.doc('update a receiving order')
    @crossdomain(origin='*')
    @api.expect(_put_receiving_order, validate=True)
    def put(self, id):
        """Updates a receiving order """
        data = request.json
        return update_receiving_order(id, data=data)