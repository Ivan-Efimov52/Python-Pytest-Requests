import requests


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6a9bc7516936cb4bfd8e31405a58cf88'
HEADER = {'Content-Type' :'application/json', 'trainer_token':TOKEN}


body = {
    "trainer_token": TOKEN,
    "name": "Бульбазавр",
    "photo_id": 1
}

body_patch = {
    "pokemon_id": "70279",
    "name": "Shpatel1"
}

body_pokeball = {
    "pokemon_id": "70279"
}

'''response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body)
print(response.text)

message = response.json()['message']
print(message)'''

'''response_patch = requests.patch(url = f'{URL}/pokemons', headers = HEADER, json = body_patch)
print(response_patch.text)'''

'''response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_add_pokeball.text)'''