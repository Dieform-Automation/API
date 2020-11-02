
from app.main.model.customer import Customer
from app.main.model.purchase_order import PurchaseOrder
from app.main.model.part import Part
from app.main.model.receiving_order import ReceivingOrder
from app.main.model.received_part import ReceivedPart

def setup_default(db):

    setup_customer(db)
    setup_purchase_order(db)
    setup_part(db)
    setup_receiving_order(db)

def setup_customer(db):
    # customer
    customer = Customer(
        name='test name',
        email='test@test.com',
        phone='test',
        street="test",
        city="test",
        country="test",
        province="test",
        postal_code="test",
        point_of_contact="test"
    )
    db.session.add(customer)
    db.session.commit()

def setup_purchase_order(db):
    # purchase order
    purchase_order = PurchaseOrder(
        customer_id=1,
        number=1,
    )
    db.session.add(purchase_order)
    db.session.commit()

def setup_part(db):
    # purchase order
    part = Part(
        customer_id=1,
        purchase_order_id=1,
        number="123",
        name="test_name"
    )
    db.session.add(part)
    db.session.commit()

def setup_receiving_order(db):
    # purchase order
    receiving = ReceivingOrder(
        customer_id=1,
        customer_packing_slip="test_receiving_order_packing_slip_2",
    )
        
    received_part = ReceivedPart(
        part_id=1,
        receiving_order_id=1,
        part_quantity=1,
        bins=1
    )
    
    db.session.add(receiving)
    db.session.commit()