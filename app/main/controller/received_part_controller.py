from flask import request
from flask_restplus import Resource

from ..util.dto import ReceivedPartDto
from ..util.decorator import crossdomain, token_required # will be used later
from ..service.received_part_service import save_new_received_part

api = ReceivedPartDto.api
_post_received_part = ReceivedPartDto.received_part_post

@api.route('/')
class ReceivedPart(Resource):
    @api.response(201, 'Received part successfully added.')
    @api.doc('add a new received part')
    @crossdomain(origin='*')
    @api.expect(_post_received_part, validate=True)
    def post(self):
        """Creates a new received part"""
        data = request.json
        return save_new_received_part(data=data)