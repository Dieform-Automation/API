from .. import db

from sqlalchemy.orm import relationship

class Customer(db.Model):
    """ Customer Model for storing Dieform customer information """
    __tablename__ = "customer"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    street = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(255), nullable=False)
    province = db.Column(db.String(255), nullable=False)
    postal_code = db.Column(db.String(255), nullable=False)
    point_of_contact = db.Column(db.String(255), nullable=True)

    parts = relationship("Part")
    purchaseOrders = relationship("PurchaseOrder")
    receivingOrders = relationship("ReceivingOrder")

    def __repr__(self):
        return "<Customer '{}'>".format(self.name)