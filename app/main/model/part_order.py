from .. import db

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class PartOrder(db.Model):
    """ Part - Order association class for storing Dieform order/part info """
    __tablename__ = "part_order"

    id = db.Column('id', db.Integer, primary_key=True)
    part_id = db.Column(db.Integer, ForeignKey('part.id'))
    order_id = db.Column(db.Integer, ForeignKey('order.id'))
    quantity = db.Column(db.Integer, nullable=False)

    parts = relationship("Part", backref="partorder")
    orders = relationship("Order", backref="partorder")

    def __repr__(self):
        return "<PartOrder '{}'>".format(self.id)