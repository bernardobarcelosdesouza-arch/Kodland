from flask import Flask, request
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1>'

@app.route("/random_fact")
def random_fact():
    facts = [
    "Polvos têm três corações e sangue azulado!",
    "Existem mais estrelas no universo observável do que grãos de areia em muitas estimativas de todas as praias da Terra.",
    "O mel, quando armazenado corretamente, pode permanecer conservado por milhares de anos.",
    "Um raio pode aquecer o ar ao seu redor a temperaturas superiores às da superfície do Sol!",
    "Tubarões existem há mais tempo que as árvores: seus ancestrais surgiram há mais de 400 milhões de anos."
    ]

    return f'<h1>Random Fact</h1><p>{random.choice(facts)}</p>'


@app.route("/secret")
def secret():
    caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    comprimento = int(request.args.get("comprimento", 8))

    senha = ""

    for i in range(comprimento):
        senha += random.choice(caracteres)

    return "Senha gerada: " + senha

app.run(debug=True)
