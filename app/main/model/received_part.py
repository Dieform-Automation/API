import datetime
from .. import db

from sqlalchemy import ForeignKey

class ReceivedPart(db.Model):
    __tablename__ = "received_part"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    part_id = db.Column(db.Integer, ForeignKey('part.id'))
    receiving_order_id = db.Column(db.Integer, ForeignKey('receiving_order.id'))
    quantity = db.Column(db.Integer, nullable=False)
    bins = db.Column(db.Integer, default=0)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return "<Recieved Part number: '{}'>".format(self.number)