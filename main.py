from flask import Flask, render_template, request
import helpers
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    search_term =  request.args.get("global-keywords")

    properties = [
            {'uprn': 45, 'address': '159, Idwal Street, Upper Leadworth, Clwyd'},
            {'uprn': 46, 'address': '177, Owain Road, Upper Leadworth, Clwyd'},
            {'uprn': 47, 'address': '152, Castle Street, Upper Leadworth, Clwyd'},
            {'uprn': 48, 'address': '15, Mountain Drive, Upper Leadworth, Clwyd'},
            {'uprn': 49, 'address': '174, Mountain Road, Upper Leadworth, Clwyd'},
            {'uprn': 50, 'address': '38, Highstreet, Upper Leadworth, Clwyd'},
            {'uprn': 51, 'address': '133, Pleasant Drive, Upper Leadworth, Clwyd'},
            {'uprn': 52, 'address': '141, Mountain Drive, Upper Leadworth, Clwyd'},
            {'uprn': 53, 'address': '90, Idwal Court, Upper Leadworth, Clwyd'},
            {'uprn': 54, 'address': '32, Idwal Court, Upper Leadworth, Clwyd'},
            {'uprn': 55, 'address': '178, Pleasant Road, Upper Leadworth, Clwyd'},
            {'uprn': 56, 'address': '199, Mountain Court, Upper Leadworth, Clwyd'},
            {'uprn': 57, 'address': '194, Highstreet, Upper Leadworth, Clwyd'},
            {'uprn': 58, 'address': '100, Owain Court, Upper Leadworth, Clwyd'},
            {'uprn': 59, 'address': '190, Glyndŵr Street, Upper Leadworth, Clwyd'},
            {'uprn': 60, 'address': '114, Glyndŵr Bank, Upper Leadworth, Clwyd'},
            {'uprn': 61, 'address': '107, Glyndŵr Bank, Upper Leadworth, Clwyd'}
    ]

    return render_template('search.html', search_term=search_term, properties=properties)

@app.route('/property/<int:platform_id>', methods=['GET'])
def property(platform_id):
    if isinstance(platform_id, int):
        response = requests.post('https://land-property-platform.herokuapp.com/property_info', data = json.dumps({'platform_property_id':platform_id}))
        data = response.json()
    return render_template('property.html', data=data)