from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)
app.secret_key = 'Mega_charizard_X'
API = "https://pokeapi.co/api/v2/pokemon/"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search_pokemon():
    pokemon_name = request.form.get('pokemon_name', '').strip()

if not pokemon_name:
    flash('por favor ingresa un nombre de pokemon', 'error')
    return redirect(url_for('index'))

try:
    resp = requests.get(f"{API}{pokemon_name}")
    if resp.status_code == 200:
    pokemon_data = resp.json()

        poke_info = {
            'name': pokemon_data['name'].tittle(),
            'id': pokemon_data['id'],
            'height': pokemon_data['height'] / 10, 
            'weight': pokemon_data['weight'] / 10,
            'image': pokemon_data['sprites']['front_default'],
            'types': [t['ability']['name'].title() for t in pokemon_data['types']],
            'abilites': [a['ability']['name'].title() for a in pokemon_data['abilites']],
        }
        return render_template('pokemon2.html', pokemon = poke_info)
    else:
        flash(f'pokemon "{pokemon_name}" no fue encontrado', 'error')
        return redirect(url_for('index'))
except requests.exceptions.RequestException as e:
    flash('Error al buscar el pokemon', 'error')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)