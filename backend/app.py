from flask import Flask, request, Response, render_template, redirect, url_for
from server import Database
from sympy import *
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

MIMITYPES = {
    ".css": "text/css",
    ".html": "text/html",
    ".js": "application/javascript",
}

__DIRNAME = os.path.abspath(os.path.dirname(__file__))


def get_file(filename):  # pragma: no cover
    try:
        return open(os.path.join(__DIRNAME, 'app', filename)).read()
    except IOError as exc:
        return str(exc)


@app.route('/', defaults={'path': ''}, methods=['POST', 'GET'])
@app.route('/<path:path>')
@app.route('/static/js/<path:path>')
@app.route('/static/css/<path:path>')
def App(path):
    print('Path - ', path)
    if request.method == 'GET':
        complete_path = os.path.join(__DIRNAME, 'app', path)
        ext = os.path.splitext(path)[1]
        MIMITYPE = MIMITYPES.get(ext, "text/html")

        if not 0 == len(path):
            return Response(get_file(complete_path), mimetype=MIMITYPE)
        else:
            return Response(get_file('index.html'), mimetype=MIMITYPE)
    if request.method == 'POST':
        return 'Hello Post'
    else:
        return {'error': 'method is undefined'}


@app.route('/sexo', methods=['GET'])
def sexo():
    # Database().setup_database()
    return {'sexo': 'sexoo'}


@app.route('/sexoo', methods=['POST'])
def sexoo():
    body = request.get_json()

    Database().insert_db(body['input1'], body['input2'], body['input3'], body['input4'])

    return body


if __name__ == '__main__':
    app.run(debug=True)
