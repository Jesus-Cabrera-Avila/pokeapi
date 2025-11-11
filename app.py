from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

API = "https://pokeapi.co/api/v2/pokemon/"
app = Flask(__name__)
app.secret_key = 'Mega_charizard_X'

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search_pokemon():
    pokemon_name = request.form.get('pokemon_name', '').strip()

if not pokemon_name:
    flash('por favor ingresa un nombre de pokemon', 'error')
    return redirect(url_for('index'))

resp = requests.get(f"{API}{pokemon_name}")

if resp.status_code == 200:
    pokemon_data = resp.json()
    return render_template('pokemon.html', pokemon = pokemon_)

if __name__ == '__main__':
    app.run(debug=True)