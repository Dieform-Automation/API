import unittest
import json

from app.main import db
from app.test.base import BaseTestCase

def add_purchase_order(self):
    return self.client.post(
        '/purchase_order/',
        data=json.dumps(dict(
            customer_id=1,
            number=2,
        )),
        content_type='application/json'
    )

class TestPurchaseOrderEndpoint(BaseTestCase):

    def test_purchase_order_post_endpoint(self):
            """ Test Purchase Order Post Endpoint """
            with self.client:
                response = add_purchase_order(self)
                response_data = json.loads(response.data.decode())
                self.assertEqual(response.status_code, 201)

    def test_purchase_order_get_endpoint(self):
            """ Test Purchase Order Get Endpoint """
            with self.client:
                response = self.client.get('/purchase_order/')
                response_data = json.loads(response.data.decode())
                self.assertEqual(response.status_code, 200)
                self.assertEqual(len(response_data), 1)

    def test_purchase_order_get_by_id_endpoint(self):
            """ Test Purchase Order Get by Id Endpoint """
            with self.client:
                response = self.client.get('/purchase_order/1')
                response_data = json.loads(response.data.decode())
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response_data['id'], 1)
                self.assertEqual(response_data['customer_id'], 1)
                self.assertEqual(response_data['number'], 1)

if __name__ == '__main__':
    unittest.main()