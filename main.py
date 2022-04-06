from flask import Flask, render_template, request
import helpers

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    return render_template('search.html')