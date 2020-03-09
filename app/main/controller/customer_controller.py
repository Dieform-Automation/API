from flask import request
from flask_restplus import Resource

from ..util.dto import CustomerDto
from ..util.decorator import token_required

api = CustomerDto.api
_customer = CustomerDto.customer

