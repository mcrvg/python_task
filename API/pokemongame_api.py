import requests
import json
import random

# Get the list of pokemon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
pokemon_list = json.loads(response.text)['results']

for pokemon in pokemon_list:
    print(pokemon['name'])

# Ask the user to choose a pokemon
print('Enter your pokemon:')

# Get the user's choice
choice = input().lower()
my_pokemon = choice
print("My pokemon is", my_pokemon)

# Get the pokemon's data from the API
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(choice)
response = requests.get(url)
pokemon_data = json.loads(response.text)

# to get ability
abilities = pokemon_data['abilities'][0]
ability = abilities['ability']

# to format height and weight properly
height = int(pokemon_data['height'])
weight = int(pokemon_data['weight'])

height_formatted = height / 10
weight_formatted = weight / 10

# Print the pokemon's data
print('Name: {}'.format(pokemon_data['name']))
print('Weight: {}'.format(weight_formatted) + "(kgs)")
print('Height: {}'.format(height_formatted) + "(m)")
print('Ability: {}'.format(ability['name']))

print(my_pokemon)

#pokemon of cpu
base_url = 'https://pokeapi.co/api/v2/pokemon/'

def get_pokemon_data(pokemon_name):
    """Obtiene y devuelve los datos de un Pokémon dado."""

    url = f'{base_url}{pokemon_name}/'
    response = requests.get(url)
    return json.loads(response.text)

def get_random_pokemon():
    """Obtiene un Pokémon aleatorio y devuelve su nombre."""

    response = requests.get(f'{base_url}')
    pokemon_list = json.loads(response.text)['results']
    random_pokemon = random.choice(pokemon_list)
    return random_pokemon['name']

print (get_random_pokemon())


