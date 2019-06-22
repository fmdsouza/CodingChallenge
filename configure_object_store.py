#!flask/bin/python
from flask import Flask, jsonify, make_response, abort, request


app = Flask(__name__)

resources = [
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

@app.route('/api/v1.0/resources', methods=['POST'])
def create_resource():
    if not request.json or not 'name' in request.json:
        abort(400)
    resource = {
        'id': resources[-1]['id'] + 1,
        'name': request.json['name'],
        'email': request.json.get('email', ""),
        'phone': request.json.get('phone', ""),
        'address': request.json.get('address', "")
    }
    resources.append(resource)
    return jsonify({'resource': resource}), 201

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/api/v1.0/resources/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):
    resource = [resource for resource in resources if resource['id'] == resource_id]
    if len(resource) == 0:
        abort(404)
    return jsonify({'resource': resource[0]})

@app.route('/api/v1.0/resources', methods=['GET'])
def get_resources():
    return jsonify({'resources': resources})

if __name__ == '__main__':
    app.run(debug=True)