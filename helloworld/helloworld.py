# Import the packages required for this app

from flask import Flask,jsonify,request
from datetime import datetime

app = Flask(__name__)

## Set to 'False' for debug off
app.config["DEBUG"] = True

## Handles GET and POST requests on /
@app.route('/',methods=['GET', 'POST'])

## Function definition
def hello_world():

    #Get Accept Header and URL from Request
    header1 = request.headers.get('Accept')
    url = request.url

    # Debug statement to check the URL and Accept Header
    if app.debug:
        print(datetime.fromtimestamp(datetime.timestamp(datetime.now())), " -- ", url," -- The accept header is : ",header1)

    # Handle GET requests
    if request.method == 'GET':
        if header1 == 'application/json':
            if app.debug:
                print(datetime.fromtimestamp(datetime.timestamp(datetime.now())), " -- ", url," -- This is GET request with required Header")
            return jsonify(message='Hello, World')
        else:
            if app.debug:
                print(datetime.fromtimestamp(datetime.timestamp(datetime.now())), " -- ", url," -- This is GET request with NO required Header")
            return "<p>Hello, World</p>\n"

    # Handle POST requests
    if request.method == 'POST':
        if header1 == 'application/json':
            if app.debug:
                print(datetime.fromtimestamp(datetime.timestamp(datetime.now())), " -- ", url," -- This is POST request with required Header")
            return jsonify(message='Hello, World')
        else:
            if app.debug:
                print(datetime.fromtimestamp(datetime.timestamp(datetime.now())), " -- ", url," -- This is POST request with NO required Header")
            return "<p>Hello, World</p>\n"

app.run(host='0.0.0.0', port='5000')
