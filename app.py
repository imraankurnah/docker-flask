import json
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/test', methods=['GET'])
def test():
    r = requests.get('https://google.com')
    print(r.text)
    return str(r.status_code)
