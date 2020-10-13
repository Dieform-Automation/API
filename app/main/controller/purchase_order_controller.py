from flask import request
from flask_restplus import Resource

from ..util.dto import PurchaseOrderDto
from ..util.decorator import crossdomain, token_required # will be used later
from ..service.purchase_order_service import get_all_orders, save_new_order, get_an_order, get_all_purchase_orders_by_customerID

api = PurchaseOrderDto.api
_post_order = PurchaseOrderDto.purchase_order_post

@api.route('/')
class PurchaseOrderList(Resource):
    @api.doc('list_of_orders')
    @crossdomain(origin='*')
    def get(self):
        """List all orders"""
        customer_id = request.args.get('customer_id', None)
        if customer_id:
            return get_all_purchase_orders_by_customerID(int(customer_id))
        else:
            return get_all_orders()

    @api.response(201, 'Purchase order successfully added.')
    @api.doc('add a new purchase order')
    @crossdomain(origin='*')
    @api.expect(_post_order, validate=True)
    def post(self):
        """Creates a new order """
        data = request.json
        return save_new_order(data=data)

@api.route('/<id>')
@api.param('id', 'The purchase order id')
@api.response(404, 'Purchase order not found.')
class PurchaseOrder(Resource):
    @api.doc('get an order')
    @crossdomain(origin='*')
    def get(self, id):
        """get a purchase order given its id"""
        order = get_an_order(id)
        if not order:
            api.abort(404)
        else:
            return order