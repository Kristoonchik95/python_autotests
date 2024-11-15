import requests
import pytest


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '892ef8bedb350a456fa09974bc04f661'
HEADER = {'Content-Type' : 'application/json' , 'trainer_token' : TOKEN}
TRAINER_ID = '8178'


def test_status_cod():
    response=requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Kris'


