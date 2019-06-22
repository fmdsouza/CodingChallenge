#!flask/bin/python
from flask import Flask

##sample code to check if simple call is working or not.

app = Flask(__name__)

@app.route('/')
def index():
        return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
