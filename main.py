from flask import Flask, render_template, request
import helpers

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    search_term =  request.args.get("global-keywords")

    properties = [
            {'uprn': 10013705907, 'address': '159, Idwal Street, Upper Leadworth'},
            {'uprn': 10013705990, 'address': '177, Owain Road, Upper Leadworth'},
            {'uprn': 10013706214, 'address': '152, Castle Street, Upper Leadworth'},
            {'uprn': 10013706215, 'address': '15, Mountain Drive, Upper Leadworth'},
            {'uprn': 10013706216, 'address': '174, Mountain Road, Upper Leadworth'},
            {'uprn': 10013706218, 'address': '38, Highstreet, Upper Leadworth'},
            {'uprn': 10013706219, 'address': '133, Pleasant Drive, Upper Leadworth'},
            {'uprn': 10013706220, 'address': '141, Mountain Drive, Upper Leadworth'},
            {'uprn': 10013706221, 'address': '90, Idwal Court, Upper Leadworth'},
            {'uprn': 10013706222, 'address': '32, Idwal Court, Upper Leadworth'},
            {'uprn': 10013706223, 'address': '178, Pleasant Road, Upper Leadworth'},
            {'uprn': 10013706224, 'address': '199, Mountain Court, Upper Leadworth'},
            {'uprn': 10013706225, 'address': '194, Highstreet, Upper Leadworth'},
            {'uprn': 10013706226, 'address': '100, Owain Court, Upper Leadworth'},
            {'uprn': 10013706227, 'address': '190, Glyndŵr Street, Upper Leadworth'},
            {'uprn': 10013706229, 'address': '114, Glyndŵr Bank, Upper Leadworth'},
            {'uprn': 10013706230, 'address': '107, Glyndŵr Bank, Upper Leadworth'}
    ]

    return render_template('search.html', search_term=search_term, properties=properties)