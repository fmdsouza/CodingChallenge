from flask import Flask
import pymysql
from flask import jsonify, make_response
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
	    return 'Hello World!'

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
