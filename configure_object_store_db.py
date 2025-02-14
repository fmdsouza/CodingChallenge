from flask import Flask
import pymysql
from flask import jsonify, make_response
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api/v2.0/resources/delete/<int:resource_id>', methods=['DELETE'])
def delete_resource(resource_id):
    try:
        conn = pymysql.connect("localhost", "root", "Arthur_123", "TestDB")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM resources WHERE id=%s", (resource_id))
        conn.commit()
        resp = jsonify('User deleted successfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.route('/api/v2.0/resources/put/<int:resource_id>', methods=['PUT'])
def update_resource(resource_id):
    try:
        conn = pymysql.connect("localhost", "root", "Arthur_123", "TestDB")
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM resources WHERE id=%s", resource_id)
        row = cursor.fetchone()
        
        if not request.json:
            abort(400)
        if 'name' in request.json and type(request.json['name']) != unicode:
            abort(400)
        if 'address' in request.json and type(request.json['address']) is not unicode:
            abort(400)
        if 'email' in request.json and type(request.json['email']) is not unicode:
            abort(400)
        if 'phone' in request.json and type(request.json['phone']) is not unicode:
            abort(400)

        name = request.json.get('name', row['name'])
        address = request.json.get('address', row['address'])
        email = request.json.get('email', row['email'])
        phone = request.json.get('phone', row['phone'])

        # save edits
        sql = "UPDATE resources SET name=%s, email=%s, address=%s, phone=%s WHERE id=%s"
        data = (name, email, address, phone, resource_id)
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        resp = jsonify('User updated successfully!')
        resp.status_code = 200
        return resp
        #else:
        #return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.route('/api/v2.0/resources/post', methods=['POST'])
def create_resource():
    try:
        if not request.json:
            abort(400)
        name = request.json['name']
        email = request.json.get('email', "")
        phone = request.json.get('phone', "")
        address = request.json.get('address', "")
        # validate the received values
        if name and email and phone and address and request.method == 'POST':
            # save edits
            sql = "INSERT INTO resources(name, email, phone, address) VALUES(%s, %s, %s, %s)"
            data = (name, email, phone, address,)
            conn = pymysql.connect("localhost", "root", "Arthur_123", "TestDB")
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/api/v2.0/resources/get/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):
    try:
        conn = pymysql.connect("localhost", "root", "Arthur_123", "TestDB")
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM resources WHERE id=%s", resource_id)
        row = cursor.fetchone()
        if not row:
            return not_found()    
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        abort(404)
    finally:
        cursor.close() 
        conn.close()

@app.route('/api/v2.0/resources/get', methods=['GET'])
def get_resources():
    try:
        conn = pymysql.connect("localhost", "root", "Arthur_123", "TestDB")
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM resources")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

if __name__=="__main__":
    #app.run()
    app.run(host="0.0.0.0", port="5000")
