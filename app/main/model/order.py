from .. import db

from sqlalchemy import ForeignKey

class Order(db.Model):
    """ Order Model for storing Dieform order info """
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, ForeignKey('customer.id'))
    number = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Order number: '{}'>".format(self.number)