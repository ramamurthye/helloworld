# Import the packages required for this app
# We use flask framework for this
# Import request package for handling headers and methods

from flask import Flask
from flask import request

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/',methods=['GET', 'POST'])
def hello_world():
    header1 = request.headers.get('X-Requested-By')
    print("Header : ",header1)
    if request.method == 'GET':
        return 'Get - Hello, World!'
    if request.method == 'POST':
        return 'POST - Hello, World!'
