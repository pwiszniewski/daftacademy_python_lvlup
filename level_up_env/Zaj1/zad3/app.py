from flask import Flask
from flask import request
from flask import json

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Touched for the very first time.'


@app.route('/method', methods=['GET', 'POST', 'PUT', 'DELETE'])
def request_info():
    return f'{request.method}'

@app.route('/show_data', methods=['POST'])
def show_json_data():
    return json.dumps(request.json)


if __name__ == '__main__':
    app.run(debug=False)
