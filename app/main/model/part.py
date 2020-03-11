from .. import db

from sqlalchemy import ForeignKey

class Part(db.Model):
    """ Part Model for storing Dieform parts info """
    __tablename__ = "part"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, ForeignKey('customer.id'))
    number = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return "<Part number: '{}'>".format(self.number)