from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Touched for the very first time.'


@app.route('/method', methods=['GET', 'POST', 'PUT', 'DELETE'])
def request_info():
    return f'{request.method}'


if __name__ == '__main__':
    app.run(debug=False)
