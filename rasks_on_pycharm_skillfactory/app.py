from flask import Flask, request, jsonify
from datetime import datetime
import pickle
from sklearn.linear_model import LinearRegression
import numpy as np

app = Flask(__name__)


@app.route('/hello')
def hello_func():
    name = request.args.get('name')
    return f'hello {name}!'


@app.route('/time')
def current_time():
    # datetime object containing current date and time
    now = datetime.now()

    print("now =", now)

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%H:%M:%S")

    return f'{dt_string}'


@app.route('/add', methods=['POST'])
def add():
    num = request.json.get('num')
    if num > 10:
        return 'too much', 400
    return jsonify({
        'result': num + 1
    })


# @app.route('/predict', methods=['GET'])
# def predict():
#     with open('model/hw1.pkl', 'rb') as pkl_file:
#         pckl = pickle.load(pkl_file)
#         print(pckl)
#
#     return 'OK'


@app.route('/predict', methods=['POST'])
def predict():
    numbers = request.json
    print(request.json)

    with open('model/hw1.pkl', 'rb') as pkl_file:
        model = pickle.load(pkl_file)

    prediction = model.predict(np.array(numbers).reshape(1, -1))[0]
    print(type(prediction))
    print(prediction)

    json_back = jsonify({
        'prediction': prediction
    })

    print(json_back)

    return json_back


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run('localhost', 5000)
