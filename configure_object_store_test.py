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
    
    def test_get_resources(self):
        result = [{
        'id': 1,
        'name': u'John Smith',
        'email': u'john.smith@gmail.com', 
        'phone': u'800-555-5669',
        'address': u'969 High St., Atlantis VA 34075'}]
        
        with app.app_context():
            res = get_resources()
            data = json.loads(res.get_data(as_text=True))
            self.assertEqual(data['resources'], result)
            
    def test_get_resource(self):
        with app.app_context():
            res = get_resource(1)
            data = json.loads(res.get_data(as_text=True))
            self.assertEqual(data['resource'], self.sample_records[0])
            
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
