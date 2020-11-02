import unittest
import json

from app.main import db
from app.test.base import BaseTestCase

def add_receiving_order(self):
    return self.client.post(
        '/receiving_order/',
        data=json.dumps(dict(
            customer_id=1,
            customer_packing_slip="test_receiving_order_packing_slip",
            received_parts=[dict(
                part_id=1,
                part_quantity=2,
                bins=1
            )]
        )),
        content_type='application/json'
    )

class TestReceivingOrderEndpoint(BaseTestCase):

    def test_receiving_order_post_endpoint(self):
            """ Test Receiving Order Post Endpoint """
            with self.client:
                response = add_receiving_order(self)
                response_data = json.loads(response.data.decode())
                self.assertEqual(response.status_code, 201)

    def test_receiving_order_get_endpoint(self):
            """ Test Receiving Order Get Endpoint """
            with self.client:
                response = self.client.get('/receiving_order/')
                response_data = json.loads(response.data.decode())
                self.assertEqual(response.status_code, 200)
                self.assertEqual(len(response_data), 1)

    def test_receiving_order_get_by_id_endpoint(self):
            """ Test Receiving Order Get by Id Endpoint """
            with self.client:
                response = self.client.get('/receiving_order/1')
                response_data = json.loads(response.data.decode())
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response_data['id'], 1)
                self.assertEqual(response_data['customer_id'], 1)

if __name__ == '__main__':
    unittest.main()