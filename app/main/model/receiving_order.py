import datetime
from .. import db

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class ReceivingOrder(db.Model):
    """ Receiving order for storing Dieform log info """
    __tablename__ = "receiving_order"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, ForeignKey('customer.id'))
    customer_packing_slip = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date, default=datetime.datetime.utcnow)

    receivedParts = relationship("ReceivedPart")

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return "<Part number: '{}'>".format(self.number)