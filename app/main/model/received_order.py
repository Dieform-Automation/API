import datetime
from .. import db

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class ReceivedOrder(db.Model):
    """ Received order for storing Dieform log info """
    __tablename__ = "received_order"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, ForeignKey('customer.id'))
    customer_packing_slip = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, default=datetime.datetime.utcnow)

    receivedParts = relationship("ReceivedPart")

    def __repr__(self):
        return "<Part number: '{}'>".format(self.number)