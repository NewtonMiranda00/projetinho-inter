from flask import Flask, request, render_template, redirect, url_for
from server import DataBase
from sympy import *
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route('/excluirdb')
def excluirdb():
    DataBase().criar_tabela()
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def homepage(fofo=None):
    if request.method == 'POST':
        fofo = request.form['nm']
        DataBase().inserir_na_tabela(fofo)
        return render_template('index.html', fofo=fofo)

    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
