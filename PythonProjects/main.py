import requests

URL = 'https://api.pokemonbattle.ru/v2'
token = 'b3234c30385e8833142fe2082ace70ce'
auth_header = { 'Content-Type' : 'application/json',
                'trainer_token' : token }
create_body = { 
    'name': 'generate',
    'photo_id': -1
    }
trainer_id = 4333

'''create_pokemon_request = requests.post(url = f'{URL}/pokemons', headers = auth_header, json = create_body)
print(create_pokemon_request.text)

pokemon_id = create_pokemon_request.json()['id']
print(pokemon_id)

change_body = {
    "pokemon_id": pokemon_id,
    "name": "generate",
    "photo_id": -1
}

add_pokeball_body = {
    "pokemon_id": pokemon_id
}
'''
knockout_pokemon_body = {
    "pokemon_id": "42097"
}

'''change_pokemon_name_request = requests.put(url = f'{URL}/pokemons', headers = auth_header, json = change_body)
print(change_pokemon_name_request.text)'''

'''add_pokeball_request = requests.post(url = f'{URL}/trainers/add_pokeball', headers = auth_header, json = add_pokeball_body)
print(add_pokeball_request.text)'''

'''knockout_request = requests.post(url = f'{URL}/pokemons/knockout', headers = auth_header, json = knockout_pokemon_body)
print(knockout_request.text)'''

trainer_info_request = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : trainer_id})
print(trainer_info_request.text)