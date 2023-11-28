from flask import Flask, render_template, request, redirect
from flask_pydantic_spec import FlaskPydanticSpec

app = Flask(__name__, template_folder='template')

spec = FlaskPydanticSpec('flask', title='Python Swagg')
spec.register(app)


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God Of War', 'Luta', 'PS4')
jogo3 = Jogo('Mk', 'Luta', 'Multiplataforma')
lista = [jogo1, jogo2, jogo3]


@app.route('/')
def home():

    return render_template('lista.html', title='Jogos', jogos=lista)


@app.route('/newgame')
def newgame():
    return render_template('novo.html', title='Novos Jogos')


@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    # return render_template('lista.html', title='Jogos', jogos=lista)
    return redirect('/')

app.run(debug=True, host='127.0.0.1', port=8080)

