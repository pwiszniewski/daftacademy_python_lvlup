from flask import Flask
from flask import request
from flask import json, jsonify
from multiprocessing import Value

counter = Value('i', 0)
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Zad5'

@app.route('/method', methods=['GET', 'POST', 'PUT', 'DELETE'])
def request_info():
    return f'{request.method}'

@app.route('/show_data', methods=['POST'])
def show_json_data():
    return json.dumps(request.json)

@app.route('/pretty_print_name', methods=['POST'])
def show_pretty_json_data():
    json_data = json.dumps(request.json)
    dict_data = json.loads(json_data)
    return 'Na imię mu {}, a nazwisko jego {}'.format(dict_data["name"], dict_data["surename"])

@app.route('/counter')
def count_up():
    with counter.get_lock():
        counter.value += 1
    return str(counter.value)

if __name__ == '__main__':
    app.run(debug=False)
