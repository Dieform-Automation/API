import unittest
import json

from app.main import db
from app.test.base import BaseTestCase

def add_part(self):
    return self.client.post(
        '/part/',
        data=json.dumps(dict(
            customer_id=1,
            name="test_part",
            number="1",
            purchase_order_id=1 
        )),
        content_type='application/json'
    )

def update_part(self):
    return self.client.put(
        '/part/1',
        data=json.dumps(dict(
            name="test_part_renamed"
        )),
        content_type='application/json'
    )

class TestPartEndpoint(BaseTestCase):

    def test_part_post_endpoint(self):
            """ Test Part Post Endpoint """
            with self.client:
                response = add_part(self)
                response_data = json.loads(response.data.decode())
                self.assertEqual(response.status_code, 201)

    def test_part_get_endpoint(self):
            """ Test Part Get Endpoint """
            with self.client:
                response = self.client.get('/part/')
                response_data = json.loads(response.data.decode())
                self.assertEqual(response.status_code, 200)
                self.assertEqual(len(response_data), 1)

    def test_part_get_by_id_endpoint(self):
            """ Test Part Get by Id Endpoint """
            with self.client:
                response = self.client.get('/part/1')
                response_data = json.loads(response.data.decode())
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response_data['id'], 1)
                self.assertEqual(response_data['number'], '123')
                self.assertEqual(response_data['name'], 'test_name')
                self.assertEqual(response_data['purchase_order_id'], 1)

    def test_part_put_endpoint(self):
            """ Test Part Put Endpoint """
            with self.client:
                response = update_part(self)
                self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()