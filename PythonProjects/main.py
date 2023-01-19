import requests
import json
token = '1f3ed87626fe81796f7cea208c7787ed'

response = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'Content-Type': 'application/json',
 'trainer_token':token },
json = {
    "name": "Sara",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})

pokemon_id = response.json()['id']
print(response.text)

response_change = requests.put('https://pokemonbattle.me:5000/pokemons',headers={'Content-Type': 'application/json',
 'trainer_token':token },
 json= {
    "pokemon_id": pokemon_id,
    "name": "Serg",
    "photo": "https://dolnikov.ru/pokemons/04.png"
}  )
print(response_change.text)

response_pokeball = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball',
    headers={'Content-Type': 'application/json', 'trainer_token':token },
    json = {    "pokemon_id": pokemon_id}
    )

print(response_pokeball.text)

response_kill = requests.post('https://pokemonbattle.me:5000/pokemons/kill',
 headers={'Content-Type': 'application/json', 'trainer_token':token },
    json = {    "pokemon_id": pokemon_id}

)
print(response_kill.text)




