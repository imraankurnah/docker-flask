import json
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/test', methods=['GET'])
def test():
    r = requests.get('https://google.com')
    print(r.text)
    return str(r.status_code)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
