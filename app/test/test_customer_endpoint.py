import unittest
import json

from app.main import db
from app.test.base import BaseTestCase

def add_customer(self):
    return self.client.post(
        '/customer/',
        data=json.dumps(dict(
            name='test name 2',
            email='test_new@test.com',
            phone='test',
            street="test",
            city="test",
            country="test",
            province="test",
            postal_code="test",
            point_of_contact="test"
        )),
        content_type='application/json'
    )

def update_customer(self):
    return self.client.put(
        '/customer/1',
        data=json.dumps(dict(
            name="new name",
            phone="new phone number"
        )),
        content_type='application/json'
    )

class TestCustomerEndpoint(BaseTestCase):

    def test_customer_post_endpoint(self):
            """ Test Customer Post Endpoint """
            with self.client:
                response = add_customer(self)
                response_data = json.loads(response.data.decode())
                self.assertEqual(response.status_code, 201)

    def test_customer_get_endpoint(self):
            """ Test Customer Get Endpoint """
            with self.client:
                response = self.client.get('/customer/')
                response_data = json.loads(response.data.decode())
                self.assertEqual(response.status_code, 200)
                self.assertEqual(len(response_data), 1)

    def test_customer_get_by_id_endpoint(self):
            """ Test Customer Get by Id Endpoint """
            with self.client:
                response = self.client.get('/customer/1')
                response_data = json.loads(response.data.decode())
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response_data['id'], 1)
                self.assertEqual(response_data['name'], 'test name')
                self.assertEqual(response_data['email'], 'test@test.com')

    def test_customer_put_endpoint(self):
            """ Test Customer Put Endpoint """
            with self.client:
                response = update_customer(self)
                self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()