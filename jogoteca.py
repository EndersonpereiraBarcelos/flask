from flask import Flask, render_template

app = Flask(__name__, template_folder='template')


@app.route('/')
def ola():
    lista = ['Tetris', 'God Of War', 'Valorant']
    return render_template('lista.html', title='Jogos', jogos=lista)


app.run(debug=True, host='127.0.0.1', port=8080)
