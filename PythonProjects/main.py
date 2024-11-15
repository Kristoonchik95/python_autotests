import requests
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '892ef8bedb350a456fa09974bc04f661'
HEADER = {'Content-Type' : 'application/json' , 'trainer_token' : TOKEN}
trainer_id = '8178'
body_pokemon = {
    "name": "Link",
    "photo_id": -1
}


response_pokemon = requests.post (url = f'{URL}/pokemons', headers = HEADER, json = body_pokemon)
print(response_pokemon.json())

response_json = response_pokemon.json()
key_id_pokemon = response_json['id']
print(id) 

bodyNN = {
    "pokemon_id": key_id_pokemon,
    "name": "Zelda"
}

bodyPB = {
    "pokemon_id": key_id_pokemon
}

response_newName = requests.patch(url = f'{URL}/pokemons', headers = HEADER, json = bodyNN)
print(response_newName.json())

response_pokeball = requests.post (url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = bodyPB)
print(response_pokeball.json())
