import json
from django.shortcuts import render
from flask import Flask, Response, jsonify, render_template, request

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/show', methods=['GET'])
def show():
    with open('Store.json') as f:
        data = json.loads(f.read())
    return Response(render_template('show.html', data=data))


@app.route('/post', methods=['POST'])
def process_form():
    with open('Store.json') as f:
        data = json.loads(f.read())

    data[len(data)] = request.form

    with open('Store.json', 'w') as f:

        json.dump(data, f)

    return render_template('index.html')


if __name__ == "__main__":
    app.run()
