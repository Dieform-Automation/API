from .. import db

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class PurchaseOrder(db.Model):
    """ Part - Order association class for storing Dieform order/part info """
    __tablename__ = "purchase_order"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, ForeignKey('customer.id'))
    number = db.Column(db.Integer, nullable=False)

    parts = relationship("Part")

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return "<PurchaseOrder '{}'>".format(self.id)