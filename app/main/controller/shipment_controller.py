from flask import request
from flask_restplus import Resource

from ..util.dto import ShipmentDto
from ..util.decorator import crossdomain, token_required # will be used later
from ..service.shipment_service import get_shipment, get_all_shipments, save_new_shipment

api = ShipmentDto.api
_post_shipment = ShipmentDto.shipment_post

@api.route('/')
class Shipment(Resource):
    @api.doc('list_of_shipments')
    @crossdomain(origin='*')
    def get(self):
        """List all shipments"""
        return get_all_shipments()

    @api.response(201, 'Shipment successfully added.')
    @api.doc('add a new shipment')
    @crossdomain(origin='*')
    @api.expect(_post_shipment, validate=True)
    def post(self):
        """Creates a new shipment """
        data = request.json
        return save_new_shipment(data=data)

@api.route('/<id>')
@api.param('id', 'The shipment order id')
@api.response(404, 'Shipment not found.')
class SingleShipment(Resource):
    @api.doc('get a shipment')
    @crossdomain(origin='*')
    def get(self, id):
        """get a shipment given its id"""
        shipment = get_shipment(id)
        if not shipment:
            api.abort(404)
        else:
            return shipment