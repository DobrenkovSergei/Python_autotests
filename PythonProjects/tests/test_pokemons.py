import requests
import pytest

def test_status_code():
    response = requests.get('https://pokemonbattle.me:5000/pokemons')
    assert response.status_code == 200

def test_fragment_of_response():
    response = requests.get('https://pokemonbattle.me:5000/pokemons', params={'pokemon_id': '3033'})
    assert response.json()['name']=='Делавэрррр'


def test_status_code_trainers():
    response = requests.get('https://pokemonbattle.me:5000/trainers')
    assert response.status_code == 200

def test_fragment_trainers():
    response = requests.get('https://pokemonbattle.me:5000/trainers',params={'trainer_id':'1643'} )
    assert response.status_code == 200


@pytest.mark.parametrize('key,value', [('trainer_name','Sergei'),('city','Samara'),('level', '3')])

def test_parametr(key,value):
     response = requests.get('https://pokemonbattle.me:5000/trainers', params= {'trainer_id': '1643'})
     assert response.json()[key] == value