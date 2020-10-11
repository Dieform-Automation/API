import datetime
from .. import db

from sqlalchemy import ForeignKey

class ReceivedPart(db.Model):
    """ Receiving Model for storing Dieform log info """
    __tablename__ = "received_part"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    part_id = db.Column(db.Integer, ForeignKey('part.id'))
    receiving_order_id = db.Column(db.Integer, ForeignKey('receiving_order.id'))
    part_quantity = db.Column(db.Integer, nullable=False)
    bins = db.Column(db.Integer, default=0)

    def __repr__(self):
        return "<Recieved Part number: '{}'>".format(self.number)