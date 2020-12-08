from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    r = requests.get('https://pokeapi.co/api/v2/pokedex/2')
    pokemon = r.json()

    res = requests.get('https://pokeapi.co/api/v2/pokemon/1')
    poke = res.json()

    return render_template('index.html', pokemon=pokemon, poke=poke, title='PyDex')

if __name__ == "__main__":
  app.run()