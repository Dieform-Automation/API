from datetime import date
from .. import db

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Shipment(db.Model):
    """ Shipment model for storing Dieform shipment info """
    __tablename__ = "shipment"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, default=date.today)
    shipping_method = db.Column(db.String(255), nullable=False)

    shippedParts = relationship("ShippedPart")

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return "<Part number: '{}'>".format(self.id)