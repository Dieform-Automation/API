import datetime
from .. import db

from sqlalchemy import ForeignKey

class Receiving(db.Model):
    """ Receiving Model for storing Dieform log info """
    __tablename__ = "receiving"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, ForeignKey('customer.id'))
    part_id = db.Column(db.Integer, ForeignKey('part.id'))
    customer_packing_slip = db.Column(db.String(255), nullable=False)
    part_quantity = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date(), default=datetime.datetime.now())

    def __repr__(self):
        return "<Part number: '{}'>".format(self.number)