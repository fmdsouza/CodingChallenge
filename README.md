# CodingChallenge
Developing a simple REST API

Added a simple sample_app.py file just to check if flask instrallation is proper and able to make a REST call.

Pre-requisites:
Python should be already installed. Perform the following steps in the folder where you want to save your changes.

$ mkdir REST_api
$ cd REST_api
$ virtualenv flask
New python executable in flask/bin/python
Installing setuptools............................done.
Installing pip...................done.

$ cd flask/Scripts
$pip.exe install flask

Write a sample application to test if everything works fine.
$ python.exe ../sample_app.py

Examples for GET requests:

The main code will be executed using the below command:
$python configure_object_store.py

With this the server will be running and it displays the ip address and the port on which the service will be running.

To access the service, below are the links which are exposed:

1. To fetch all the records: 
using browser ---> http://localhost:5000/api/v1.0/resources/get
using curl ---> curl -i http://localhost:5000/api/v1.0/resources/get

2. To fetch a particular record based on the record id:
using browser ---> http://localhost:5000/api/v1.0/resources/get/1
using curl ---> curl -i http://localhost:5000/api/v1.0/resources/get/1

Example for POST method:
using curl --> curl -i -H "Content-Type: application/json" -X POST -d '{"name": "Eric Williams", "phone":"560-555-5153", "address": "806 1st St., Faketown AK 86847", "email":"laurawilliams@bogusemail.com"}' http://localhost:5000/api/v1.0/resources/post

Example for PUT method:
curl -i -H "Content-Type: application/json" -X PUT -d '{"email":"abc.def@gmail.com"}' http://localhost:5000/api/v1.0/resources/put/3

Example for DELETE method:
curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/api/v1.0/resources/delete/3
