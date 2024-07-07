import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
token = 'b3234c30385e8833142fe2082ace70ce'
auth_header = { 'Content-Type' : 'application/json',
                'trainer_token' : token }
trainer_id = 4333

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : trainer_id})
    assert response.status_code == 200

def test_part_of_response():
     response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : trainer_id})
     assert response.json()['data'][0]['trainer_name'] == 'Альфарий'
