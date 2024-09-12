import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6a9bc7516936cb4bfd8e31405a58cf88'
HEADER = {'Content-Type' :'application/json', 'trainer_token':TOKEN}
TRAINER_ID = 5522
level = 5

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params={'level': level})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params= {'trainer_id':TRAINER_ID})
    assert response_get.json()["data"][0]['trainer_name'] == 'Shpatel'


