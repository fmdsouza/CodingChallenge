#!flask/bin/python
import unittest
import json
from configure_object_store import *

class RestApiTest(unittest.TestCase):
    def setUp(self):
        self.sample_records = [
    {
        'id': 1,
        'name': u'John Smith',
        'email': u'john.smith@gmail.com', 
        'phone': u'800-555-5669',
        'address': u'969 High St., Atlantis VA 34075'
    },
    {
        'id': 2,
        'name': u'Dave Martin',
        'email': u'davemartin@bogusemail.com', 
        'phone': u'615-555-7164',
        'address': u'173 Main St., Springfield RI 55924'
    }
    ]

    def test_delete_resource(self):
        with app.app_context():
            res = delete_resource(2)
            data = json.loads(res.get_data(as_text=True))
            self.assertEqual(data, {'result': True})

    def test_delete_resource_negative(self):
        response = app.test_client().delete('/api/v1.0/resources/delete/10')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 404)

    def test_get_resources(self):
        response = app.test_client().get('/api/v1.0/resources/get')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)

    def test_get_resources_negative(self):
        response = app.test_client().get('/api/v1.0/resources/get/')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 404)
                    
    def test_get_resource(self):
        with app.app_context():
            res = get_resource(1)
            data = json.loads(res.get_data(as_text=True))
            self.assertEqual(data['resource'], self.sample_records[0])

    def test_get_resource_negative(self):
        response = app.test_client().get('/api/v1.0/resources/get/10')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data, {"error": "Not found"})

    def test_create_resource(self):
        input_json = {"name": "Eric Williams", "phone":"560-555-5153", "address": "806 1st St., Faketown AK 86847", "email":"laurawilliams@bogusemail.com"}
        response = app.test_client().post('/api/v1.0/resources/post',
        data=json.dumps(input_json),
        content_type='application/json',
    )

        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['resource'], {u'id': 3, u'phone': u'560-555-5153', u'email': u'laurawilliams@bogusemail.com', u'name': u'Eric Williams', u'address': u'806 1st St., Faketown AK 86847'})
        self.assertEqual(response.status_code, 201)

    def test_update_resource(self):
        input_json = {"email":"abc.def@gmail.com"}
        response = app.test_client().put('/api/v1.0/resources/put/3',
        data=json.dumps(input_json),
        content_type='application/json',)

        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['resource']['email'], input_json['email'])      

    def test_update_resource_negative(self):
        input_json = {"email":"abc.def@gmail.com"}
        response = app.test_client().put('/api/v1.0/resources/put/6',
        data=json.dumps(input_json),
        content_type='application/json',)

        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data, {"error": "Not found"})


if __name__ == "__main__":
    unittest.main()
