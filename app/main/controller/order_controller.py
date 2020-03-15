from flask import request
from flask_restplus import Resource

from ..util.dto import OrderDto
from ..util.decorator import crossdomain, token_required # will be used later
from ..service.order_service import get_all_orders, save_new_order, get_an_order, get_all_orders_by_customerID, update_order

api = OrderDto.api
_new_order = OrderDto.new_order
_update_order = OrderDto.order_update

@api.route('/')
class OrderList(Resource):
    @api.doc('list_of_orders')
    @crossdomain(origin='*')
    def get(self):
        """List all orders"""
        customer_id = request.args.get('customer_id', None)
        if customer_id:
            return get_all_orders_by_customerID(int(customer_id))
        else:
            return get_all_orders()

    @api.response(201, 'Order successfully added.')
    @api.doc('add a new order')
    @crossdomain(origin='*')
    @api.expect(_new_order, validate=True)
    def post(self):
        """Creates a new order """
        data = request.json
        return save_new_order(data=data)

@api.route('/<id>')
@api.param('id', 'The Order id')
@api.response(404, 'Order not found.')
class Order(Resource):
    @api.doc('get an order')
    @crossdomain(origin='*')
    def get(self, id):
        """get an order given its id"""
        order = get_an_order(id)
        if not order:
            api.abort(404)
        else:
            return order

    @api.response(204, 'Successfully updated order.')
    @api.doc('update order')
    @crossdomain(origin='*')
    @api.expect(_update_order, validate=True)
    def put(self, id):
        """Updates an order """
        data = request.json
        return update_order(id, data=data)